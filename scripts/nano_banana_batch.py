from __future__ import annotations

import argparse
import base64
import csv
import json
import os
import sys
import time
import urllib.error
import urllib.request
from io import BytesIO
from pathlib import Path
from typing import Any

from PIL import Image, ImageOps


DEFAULT_ROOT = Path(r"C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2")
INTERACTIONS_URL = "https://generativelanguage.googleapis.com/v1beta/interactions"


def find_file(root: Path, pattern: str) -> Path:
    matches = sorted(root.glob(pattern))
    if not matches:
        raise FileNotFoundError(f"No file matched {pattern!r} under {root}")
    return matches[0]


def load_rows(root: Path) -> list[dict[str, str]]:
    guide = find_file(root, "00_*")
    management = guide / "나노바나나_작업관리표_v2.csv"
    if not management.exists():
        management = guide / "나노바나나_작업순서_A우선_검증포함.csv"
    with management.open("r", encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def prompt_path(root: Path, row: dict[str, str]) -> Path:
    guide = find_file(root, "00_*")
    action_folder = "전면재생성" if row["action"] == "전면 재생성" else "부분수정"
    path = guide / "작업프롬프트_개별" / row["priority"] / action_folder / f"{row['code']}.txt"
    if not path.exists():
        raise FileNotFoundError(f"Missing prompt file for {row['code']}: {path}")
    return path


def source_path(root: Path, row: dict[str, str]) -> Path:
    if row.get("input_abs"):
        path = Path(row["input_abs"])
        if path.exists():
            return path
    return root / Path(row["workpack_source"])


def output_path(root: Path, row: dict[str, str]) -> Path:
    if row.get("output_abs"):
        return Path(row["output_abs"])
    return root / "03_수정완료" / f"Part{row['part']}" / row["output_filename"]


def image_input(path: Path) -> dict[str, str]:
    data = base64.b64encode(path.read_bytes()).decode("utf-8")
    return {"type": "image", "mime_type": "image/png", "data": data}


def build_prompt(row: dict[str, str], prompt_text: str) -> str:
    part = int(row["part"])
    guide_detail = ""
    if "통합 가이드 세부 지침:" in prompt_text:
        guide_detail = prompt_text.split("통합 가이드 세부 지침:", 1)[1].split("기본 프롬프트:", 1)[0].strip()
    title_guard = ""
    if part >= 2:
        title_guard = (
            "\nPart2~Part5 제목 금지 규칙(가장 중요):\n"
            "- 그림 안에 전체 제목, 주제 제목, 상단 제목 배너를 절대 넣지 않는다.\n"
            f"- `{row['code']}` 같은 그림 코드, `[P3-F15 ...]` 같은 대괄호 제목, 파일명, 버전 문자열을 절대 넣지 않는다.\n"
            f"- `{row['title']}` 문구는 작업 이해용 주제일 뿐이며 이미지 안에 그대로 쓰지 않는다.\n"
            "- 첫 줄부터 기능성 패널, 표, 흐름도 요소로 시작한다.\n"
            "- 허용되는 제목은 표 머리글, 패널 기능명, 단계명처럼 도식 내부 구성요소를 설명하는 짧은 라벨뿐이다.\n"
        )
    return (
        "정보보안기사 시험 대비용 한국어 교육 도식이다.\n"
        "첨부한 원본은 색상, 선 굵기, 아이콘 스타일, 전체적인 편집 분위기만 참고한다.\n"
        "원본의 잘못된 구조, 잘못된 화살표, 오탈자, 깨진 한글은 복사하지 않는다.\n\n"
        f"작업 이해용 주제(이미지에 제목으로 쓰지 말 것): {row['title']}\n"
        f"현재 문제: {row['issue']}\n"
        f"반드시 반영할 수정 내용: {row['required_correction']}\n\n"
        f"세부 지침:\n{guide_detail}\n\n"
        f"{title_guard}\n"
        "추가 실행 규칙:\n"
        "- 이 요청은 단일 이미지 1장 작업이다. 여러 장을 만들지 않는다.\n"
        "- 결과 이미지는 CSV의 output_filename과 동일한 한 장의 PNG로 사용된다.\n"
        "- 한국어, 숫자, 포트, 약어, 수식, 화살표 방향을 프롬프트와 정확히 맞춘다.\n"
        "- 출력에 파일명, 코드명, 워터마크, 프롬프트 문장을 넣지 않는다.\n"
        f"- 최종 캔버스 기준: {row['source_width']} × {row['source_height']} px.\n"
    )


def post_json(url: str, api_key: str, payload: dict[str, Any], timeout: int) -> dict[str, Any]:
    request = urllib.request.Request(
        url,
        data=json.dumps(payload, ensure_ascii=False).encode("utf-8"),
        headers={
            "Content-Type": "application/json",
            "x-goog-api-key": api_key,
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            return json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        body = exc.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"Gemini API HTTP {exc.code}: {body}") from exc


def find_output_image_data(obj: Any) -> str | None:
    if isinstance(obj, dict):
        output_image = obj.get("output_image")
        if isinstance(output_image, dict) and isinstance(output_image.get("data"), str):
            return output_image["data"]
        if obj.get("mime_type", "").startswith("image/") and isinstance(obj.get("data"), str):
            return obj["data"]
        for value in obj.values():
            found = find_output_image_data(value)
            if found:
                return found
    elif isinstance(obj, list):
        for item in obj:
            found = find_output_image_data(item)
            if found:
                return found
    return None


def normalize_image(image_bytes: bytes, expected_size: tuple[int, int]) -> Image.Image:
    image = Image.open(BytesIO(image_bytes)).convert("RGB")
    if image.size == expected_size:
        return image
    fitted = ImageOps.contain(image, expected_size, method=Image.Resampling.LANCZOS)
    canvas = Image.new("RGB", expected_size, "white")
    canvas.paste(fitted, ((expected_size[0] - fitted.width) // 2, (expected_size[1] - fitted.height) // 2))
    return canvas


def write_qa(root: Path, qa_rows: list[dict[str, Any]], batch: str) -> Path:
    guide = find_file(root, "00_*")
    path = guide / f"batch{batch}_nano_banana_검수결과.csv"
    fields = [
        "batch",
        "code",
        "title",
        "action",
        "model",
        "expected_width",
        "expected_height",
        "actual_width",
        "actual_height",
        "dimension_ok",
        "output_abs",
        "response_json",
        "status",
        "note",
    ]
    with path.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(qa_rows)
    return path


def update_management(root: Path, completed_codes: set[str], batch: str) -> None:
    guide = find_file(root, "00_*")
    management = guide / "나노바나나_작업관리표_v2.csv"
    if not management.exists():
        return
    with management.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        rows = list(reader)
        fields = reader.fieldnames or []
    for row in rows:
        if row.get("code") in completed_codes:
            row["작업상태"] = "완료"
            row["1차검수"] = "크기검증 통과"
            row["2차검수"] = "대기"
            row["비고"] = f"Nano Banana API batch {batch} 호출 완료"
    with management.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def select_rows(rows: list[dict[str, str]], batch: str, codes: list[str], limit: int, force: bool) -> list[dict[str, str]]:
    selected = []
    for row in rows:
        if codes and row["code"] not in codes:
            continue
        if not codes and row.get("batch") != batch:
            continue
        if not force and row.get("작업상태") == "완료":
            continue
        selected.append(row)
    return selected[:limit]


def main() -> int:
    parser = argparse.ArgumentParser(description="Call Nano Banana through the Gemini Interactions API for one 10-image batch.")
    parser.add_argument("--root", type=Path, default=DEFAULT_ROOT)
    parser.add_argument("--batch", default="02", help="Batch number from 작업관리표_v2.csv, e.g. 02.")
    parser.add_argument("--limit", type=int, default=10)
    parser.add_argument("--code", action="append", default=[], help="Run only a specific code. May be repeated.")
    parser.add_argument("--model", default="gemini-3.1-flash-image", help="Nano Banana model id.")
    parser.add_argument("--force", action="store_true", help="Re-run rows already marked 완료.")
    parser.add_argument("--dry-run", action="store_true", help="Print selected rows without calling the API.")
    parser.add_argument("--timeout", type=int, default=180)
    parser.add_argument("--sleep", type=float, default=2.0, help="Delay between API calls.")
    args = parser.parse_args()

    root = args.root
    rows = load_rows(root)
    selected = select_rows(rows, args.batch, args.code, args.limit, args.force)
    if not selected:
        print("No rows selected.")
        return 0

    print(f"selected={len(selected)} model={args.model} batch={args.batch}")
    for row in selected:
        print(f"- {row['code']} {row['action']} -> {output_path(root, row)}")
    if args.dry_run:
        return 0

    api_key = os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY")
    if not api_key:
        print("ERROR: Set GEMINI_API_KEY or GOOGLE_API_KEY in the environment before running.", file=sys.stderr)
        return 2

    qa_rows: list[dict[str, Any]] = []
    completed: set[str] = set()
    response_dir = find_file(root, "00_*") / "nano_banana_responses"
    response_dir.mkdir(parents=True, exist_ok=True)

    for idx, row in enumerate(selected, start=1):
        code = row["code"]
        prompt = build_prompt(row, prompt_path(root, row).read_text(encoding="utf-8"))
        src = source_path(root, row)
        out = output_path(root, row)
        out.parent.mkdir(parents=True, exist_ok=True)
        response_json = response_dir / f"batch{args.batch}_{code}.json"

        payload = {
            "model": args.model,
            "input": [
                {"type": "text", "text": prompt},
                image_input(src),
            ],
        }
        print(f"[{idx}/{len(selected)}] calling {code} ...")
        response = post_json(INTERACTIONS_URL, api_key, payload, args.timeout)
        response_json.write_text(json.dumps(response, ensure_ascii=False, indent=2), encoding="utf-8")

        image_data = find_output_image_data(response)
        if not image_data:
            raise RuntimeError(f"{code}: response did not contain output image data. Saved {response_json}")
        image_bytes = base64.b64decode(image_data)
        expected = (int(row["source_width"]), int(row["source_height"]))
        image = normalize_image(image_bytes, expected)
        image.save(out)

        with Image.open(out) as saved:
            actual = saved.size
        dimension_ok = actual == expected
        qa_rows.append(
            {
                "batch": args.batch,
                "code": code,
                "title": row["title"],
                "action": row["action"],
                "model": args.model,
                "expected_width": expected[0],
                "expected_height": expected[1],
                "actual_width": actual[0],
                "actual_height": actual[1],
                "dimension_ok": dimension_ok,
                "output_abs": str(out),
                "response_json": str(response_json),
                "status": "크기검증 통과" if dimension_ok else "재작업",
                "note": "Nano Banana API 결과를 원본 비율 유지 방식으로 최종 캔버스에 맞춤",
            }
        )
        if dimension_ok:
            completed.add(code)
        time.sleep(args.sleep)

    qa_path = write_qa(root, qa_rows, args.batch)
    update_management(root, completed, args.batch)
    print(f"qa={qa_path}")
    print(f"completed={len(completed)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
