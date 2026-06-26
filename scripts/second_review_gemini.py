from __future__ import annotations

import argparse
import base64
import csv
import json
import os
import re
import ssl
import sys
import time
import urllib.error
import urllib.request
from io import BytesIO
from pathlib import Path
from typing import Any

from PIL import Image


API_URL_TEMPLATE = "https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent"

SECOND_REVIEW = "2\ucc28\uac80\uc218"
NOTE = "\ube44\uace0"
PASS = "\ud1b5\uacfc"
REWORK = "\uc7ac\uc791\uc5c5"
REVIEW_NEEDED = "\uac80\ud1a0\ud544\uc694"
WAITING = "\ub300\uae30"


def default_root() -> Path:
    candidates = [
        p
        for p in Path.cwd().iterdir()
        if p.is_dir() and p.name not in {".git", "scripts", ".gh-temp"}
    ]
    if len(candidates) != 1:
        raise FileNotFoundError("Pass --root because the workpack directory could not be inferred.")
    return candidates[0]


def first_dir(root: Path, prefix: str) -> Path:
    matches = sorted(p for p in root.iterdir() if p.is_dir() and p.name.startswith(prefix))
    if not matches:
        raise FileNotFoundError(f"No directory under {root} starts with {prefix!r}.")
    return matches[0]


def guide_dir(root: Path) -> Path:
    return first_dir(root, "00_")


def completed_dir(root: Path) -> Path:
    return first_dir(root, "03_")


def management_path(root: Path) -> Path:
    guide = guide_dir(root)
    for path in sorted(guide.glob("*.csv"), key=lambda p: p.name):
        if path.name.startswith("batch"):
            continue
        with path.open("r", encoding="utf-8-sig", newline="") as f:
            fields = csv.DictReader(f).fieldnames or []
        if {"part", "code", "title", "action", "batch", SECOND_REVIEW}.issubset(fields):
            return path
    raise FileNotFoundError("Could not find management CSV.")


def load_management(root: Path) -> tuple[Path, list[str], list[dict[str, str]]]:
    path = management_path(root)
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        rows = list(reader)
        fields = reader.fieldnames or []
    return path, fields, rows


def write_management(path: Path, fields: list[str], rows: list[dict[str, str]]) -> None:
    with path.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def output_path(root: Path, row: dict[str, str]) -> Path:
    absolute = Path(row.get("output_abs", ""))
    if absolute.exists():
        return absolute
    return completed_dir(root) / f"Part{row['part']}" / row["output_filename"]


def source_path(root: Path, row: dict[str, str]) -> Path | None:
    absolute = Path(row.get("input_abs", ""))
    if absolute.exists():
        return absolute
    candidate = root / Path(row["workpack_source"])
    if candidate.exists():
        return candidate
    return None


def image_dimensions(path: Path) -> tuple[int, int]:
    with Image.open(path) as img:
        return img.size


def image_part(path: Path, max_side: int, quality: int) -> dict[str, Any]:
    with Image.open(path) as img:
        image = img.convert("RGB")
        if max(image.size) > max_side:
            image.thumbnail((max_side, max_side), Image.Resampling.LANCZOS)
        buf = BytesIO()
        image.save(buf, format="JPEG", quality=quality, optimize=True)
    return {
        "inlineData": {
            "mimeType": "image/jpeg",
            "data": base64.b64encode(buf.getvalue()).decode("ascii"),
        }
    }


def build_prompt(row: dict[str, str], has_source: bool) -> str:
    source_note = "Image 1 is the original/source image. Image 2 is the final corrected image." if has_source else "The attached image is the final corrected image."
    return f"""
You are performing the second automated QA review for Korean information-security exam study diagrams.

{source_note}

Review target:
- code: {row['code']}
- title/reference topic: {row['title']}
- action type: {row['action']}
- title policy: {row['title_policy']}
- known issue to fix: {row['issue']}
- required correction: {row['required_correction']}
- expected canvas: {row['source_width']} x {row['source_height']} px

Judge only the final corrected image. Use the original image only as context for what was supposed to change.

Checklist:
1. The required correction is visibly reflected in the final image.
2. The diagram is conceptually accurate for the stated Korean information-security topic.
3. Korean text is readable and not obviously garbled, duplicated, or broken.
4. The title policy is followed. If the policy says internal full title/code is forbidden, reject visible codes such as P1-F32, filenames, bracketed figure labels, prompt text, or duplicated full-title banners.
5. The image is not blank, severely cropped, severely overlapped, or layout-broken.
6. For partial edits, the intended diagram content should remain while the specified issue is corrected.

Return strict JSON only, no markdown:
{{
  "verdict": "PASS" | "FAIL" | "REVIEW",
  "confidence": 0.0,
  "required_correction_met": true,
  "title_policy_ok": true,
  "no_internal_code_or_filename": true,
  "korean_text_ok": true,
  "layout_ok": true,
  "concept_accuracy_ok": true,
  "summary_ko": "Korean one-sentence review summary",
  "failure_reasons_ko": ["Korean reason if FAIL or REVIEW"],
  "observed_issues_ko": ["Korean issue observations, empty if none"]
}}

Use PASS only when there is no material issue. Use FAIL when rework is required. Use REVIEW if the image cannot be judged reliably.
""".strip()


def post_review(api_key: str, model: str, prompt: str, parts: list[dict[str, Any]], timeout: int) -> dict[str, Any]:
    payload = {
        "contents": [
            {
                "role": "user",
                "parts": [{"text": prompt}, *parts],
            }
        ],
        "generationConfig": {
            "temperature": 0,
            "responseMimeType": "application/json",
        },
    }
    req = urllib.request.Request(
        API_URL_TEMPLATE.format(model=model),
        data=json.dumps(payload, ensure_ascii=False).encode("utf-8"),
        headers={
            "Content-Type": "application/json",
            "x-goog-api-key": api_key,
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=timeout, context=ssl.create_default_context()) as response:
            return json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        body = exc.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"Gemini API HTTP {exc.code}: {body}") from exc


def candidate_text(response: dict[str, Any]) -> str:
    candidates = response.get("candidates") or []
    if not candidates:
        raise ValueError("Gemini response contained no candidates.")
    parts = candidates[0].get("content", {}).get("parts", [])
    texts = [part.get("text", "") for part in parts if isinstance(part.get("text"), str)]
    text = "\n".join(texts).strip()
    if not text:
        raise ValueError("Gemini response contained no text.")
    return text


def parse_review(response: dict[str, Any]) -> dict[str, Any]:
    text = candidate_text(response)
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        match = re.search(r"\{.*\}", text, flags=re.S)
        if not match:
            raise
        return json.loads(match.group(0))


def normalize_verdict(review: dict[str, Any], dimension_ok: bool) -> str:
    verdict = str(review.get("verdict", "REVIEW")).upper()
    if verdict not in {"PASS", "FAIL", "REVIEW"}:
        verdict = "REVIEW"
    critical_flags = [
        "required_correction_met",
        "title_policy_ok",
        "no_internal_code_or_filename",
        "korean_text_ok",
        "layout_ok",
        "concept_accuracy_ok",
    ]
    if not dimension_ok:
        return "FAIL"
    if any(review.get(flag) is False for flag in critical_flags):
        return "FAIL"
    return verdict


def review_to_second_status(verdict: str) -> str:
    if verdict == "PASS":
        return PASS
    if verdict == "FAIL":
        return REWORK
    return REVIEW_NEEDED


def result_row(
    row: dict[str, str],
    model: str,
    out_path: Path,
    src_path: Path | None,
    response_path: Path,
    review: dict[str, Any],
    verdict: str,
    actual_size: tuple[int, int],
    dimension_ok: bool,
) -> dict[str, Any]:
    reasons = review.get("failure_reasons_ko") or []
    observed = review.get("observed_issues_ko") or []
    return {
        "batch": row["batch"],
        "code": row["code"],
        "title": row["title"],
        "action": row["action"],
        "priority": row["priority"],
        "model": model,
        "verdict": verdict,
        "second_review": review_to_second_status(verdict),
        "confidence": review.get("confidence", ""),
        "required_correction_met": review.get("required_correction_met", ""),
        "title_policy_ok": review.get("title_policy_ok", ""),
        "no_internal_code_or_filename": review.get("no_internal_code_or_filename", ""),
        "korean_text_ok": review.get("korean_text_ok", ""),
        "layout_ok": review.get("layout_ok", ""),
        "concept_accuracy_ok": review.get("concept_accuracy_ok", ""),
        "expected_width": row["source_width"],
        "expected_height": row["source_height"],
        "actual_width": actual_size[0],
        "actual_height": actual_size[1],
        "dimension_ok": dimension_ok,
        "summary_ko": review.get("summary_ko", ""),
        "failure_reasons_ko": " | ".join(map(str, reasons)),
        "observed_issues_ko": " | ".join(map(str, observed)),
        "source_path": str(src_path or ""),
        "output_path": str(out_path),
        "response_json": str(response_path),
    }


def write_results(path: Path, rows: list[dict[str, Any]]) -> None:
    fields = [
        "batch",
        "code",
        "title",
        "action",
        "priority",
        "model",
        "verdict",
        "second_review",
        "confidence",
        "required_correction_met",
        "title_policy_ok",
        "no_internal_code_or_filename",
        "korean_text_ok",
        "layout_ok",
        "concept_accuracy_ok",
        "expected_width",
        "expected_height",
        "actual_width",
        "actual_height",
        "dimension_ok",
        "summary_ko",
        "failure_reasons_ko",
        "observed_issues_ko",
        "source_path",
        "output_path",
        "response_json",
    ]
    with path.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def load_existing_results(path: Path) -> list[dict[str, Any]]:
    if not path.exists():
        return []
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def select_rows(rows: list[dict[str, str]], batch: str | None, codes: set[str], limit: int | None, include_done: bool) -> list[dict[str, str]]:
    selected: list[dict[str, str]] = []
    for row in rows:
        if batch and row.get("batch") != batch:
            continue
        if codes and row.get("code") not in codes:
            continue
        if not include_done and row.get(SECOND_REVIEW) != WAITING:
            continue
        selected.append(row)
        if limit is not None and len(selected) >= limit:
            break
    return selected


def update_management_rows(
    mgmt_rows: list[dict[str, str]],
    code: str,
    model: str,
    verdict: str,
    review: dict[str, Any],
) -> None:
    second_status = review_to_second_status(verdict)
    summary = str(review.get("summary_ko") or "").strip()
    reasons = review.get("failure_reasons_ko") or []
    reason_text = " | ".join(map(str, reasons)).strip()
    detail = summary or reason_text or verdict
    note = f"2nd automated Gemini review ({model}): {second_status}"
    if detail:
        note += f" - {detail[:240]}"
    for row in mgmt_rows:
        if row.get("code") == code:
            row[SECOND_REVIEW] = second_status
            row[NOTE] = note
            return


def main() -> int:
    parser = argparse.ArgumentParser(description="Run Gemini-based second QA review for completed Nano Banana images.")
    parser.add_argument("--root", type=Path, default=None)
    parser.add_argument("--batch", default=None)
    parser.add_argument("--code", action="append", default=[])
    parser.add_argument("--limit", type=int, default=None)
    parser.add_argument("--model", default="gemini-2.5-flash")
    parser.add_argument("--timeout", type=int, default=120)
    parser.add_argument("--sleep", type=float, default=1.0)
    parser.add_argument("--max-side", type=int, default=1600)
    parser.add_argument("--jpeg-quality", type=int, default=88)
    parser.add_argument("--include-reviewed", action="store_true")
    parser.add_argument("--no-source", action="store_true", help="Do not attach original/source image context.")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    root = args.root or default_root()
    guide = guide_dir(root)
    management, fields, mgmt_rows = load_management(root)
    selected = select_rows(mgmt_rows, args.batch, set(args.code), args.limit, args.include_reviewed)
    if not selected:
        print("No rows selected.")
        return 0

    print(f"root={root}")
    print(f"management={management}")
    print(f"selected={len(selected)} model={args.model}")
    for row in selected[:20]:
        print(f"- batch={row['batch']} code={row['code']} second={row.get(SECOND_REVIEW)}")
    if len(selected) > 20:
        print(f"... {len(selected) - 20} more")
    if args.dry_run:
        return 0

    api_key = os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY")
    if not api_key:
        print("ERROR: Set GEMINI_API_KEY or GOOGLE_API_KEY.", file=sys.stderr)
        return 2

    response_dir = guide / "second_review_responses"
    response_dir.mkdir(parents=True, exist_ok=True)
    combined_path = guide / "second_review_results.csv"
    existing = load_existing_results(combined_path)
    result_by_code = {row["code"]: row for row in existing if row.get("code")}

    failures = 0
    for idx, row in enumerate(selected, start=1):
        code = row["code"]
        out_path = output_path(root, row)
        src_path = None if args.no_source else source_path(root, row)
        response_path = response_dir / f"{code}.json"
        if not out_path.exists():
            raise FileNotFoundError(f"Missing output image for {code}: {out_path}")

        expected = (int(row["source_width"]), int(row["source_height"]))
        actual = image_dimensions(out_path)
        dimension_ok = actual == expected

        parts: list[dict[str, Any]] = []
        if src_path and src_path.exists():
            parts.append(image_part(src_path, args.max_side, args.jpeg_quality))
        parts.append(image_part(out_path, args.max_side, args.jpeg_quality))

        prompt = build_prompt(row, has_source=bool(src_path and src_path.exists()))
        print(f"[{idx}/{len(selected)}] reviewing {code} ...")
        try:
            response = post_review(api_key, args.model, prompt, parts, args.timeout)
            response_path.write_text(json.dumps(response, ensure_ascii=False, indent=2), encoding="utf-8")
            review = parse_review(response)
            verdict = normalize_verdict(review, dimension_ok)
        except Exception as exc:
            failures += 1
            review = {
                "verdict": "REVIEW",
                "confidence": 0,
                "required_correction_met": False,
                "title_policy_ok": False,
                "no_internal_code_or_filename": False,
                "korean_text_ok": False,
                "layout_ok": False,
                "concept_accuracy_ok": False,
                "summary_ko": f"Gemini review failed: {exc}",
                "failure_reasons_ko": [str(exc)],
                "observed_issues_ko": [],
            }
            verdict = "REVIEW"
            response_path.write_text(json.dumps({"error": str(exc)}, ensure_ascii=False, indent=2), encoding="utf-8")

        result_by_code[code] = result_row(row, args.model, out_path, src_path, response_path, review, verdict, actual, dimension_ok)
        update_management_rows(mgmt_rows, code, args.model, verdict, review)
        write_results(combined_path, list(result_by_code.values()))
        write_management(management, fields, mgmt_rows)
        print(f"  -> {verdict} / {review_to_second_status(verdict)}")
        time.sleep(args.sleep)

    by_batch: dict[str, list[dict[str, Any]]] = {}
    for result in result_by_code.values():
        by_batch.setdefault(str(result.get("batch", "")), []).append(result)
    for batch, rows in by_batch.items():
        if batch:
            write_results(guide / f"batch{batch}_second_review_results.csv", rows)

    print(f"results={combined_path}")
    print(f"responses={response_dir}")
    print(f"failures={failures}")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
