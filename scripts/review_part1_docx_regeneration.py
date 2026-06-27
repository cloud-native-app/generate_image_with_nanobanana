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


def default_root() -> Path:
    candidates = [
        path
        for path in Path.cwd().iterdir()
        if path.is_dir() and path.name not in {".git", "scripts", ".gh-temp"}
    ]
    if len(candidates) != 1:
        raise FileNotFoundError("Pass --root because the workpack directory could not be inferred.")
    return candidates[0]


def first_dir(root: Path, prefix: str) -> Path:
    matches = sorted(path for path in root.iterdir() if path.is_dir() and path.name.startswith(prefix))
    if not matches:
        raise FileNotFoundError(f"No directory under {root} starts with {prefix!r}.")
    return matches[0]


def guide_dir(root: Path) -> Path:
    return first_dir(root, "00_")


def image_dimensions(path: Path) -> tuple[int, int]:
    with Image.open(path) as image:
        return image.size


def image_part(path: Path, max_side: int, quality: int) -> dict[str, Any]:
    with Image.open(path) as image:
        converted = image.convert("RGB")
        if max(converted.size) > max_side:
            converted.thumbnail((max_side, max_side), Image.Resampling.LANCZOS)
        buffer = BytesIO()
        converted.save(buffer, format="JPEG", quality=quality, optimize=True)
    return {
        "inlineData": {
            "mimeType": "image/jpeg",
            "data": base64.b64encode(buffer.getvalue()).decode("ascii"),
        }
    }


def build_prompt(row: dict[str, str]) -> str:
    return f"""
You are performing automated second QA review for Korean information-security exam study diagrams.

Image 1 is the regenerated Nano Banana / Gemini-style final image.
Image 2 is the original flat SVG-style or borderline source extracted from the Part1 system-security DOCX.

Review target:
- code: {row['code']}
- reference topic: {row['title']}
- internal document reference: {row['caption']}
- nearby context: {row['purpose']}
- expected canvas: {row['expected_width']} x {row['expected_height']} px

Judge Image 1 as the final image. Use Image 2 only as the authoritative context for what content and structure should be preserved.
The reference topic and nearby context are helper text only; do not fail concept accuracy merely because that helper text appears to mismatch the original image.

Checklist:
1. The final image visibly changes the flat SVG or borderline style into a polished dimensional Nano Banana-style educational diagram.
2. The final image preserves the original technical meaning, flow, comparisons, and important Korean labels.
3. Korean text is readable and not obviously garbled, duplicated, or broken.
4. The final image must not render the figure code, filename, prompt text, or any large top title/header/banner naming the whole diagram topic.
5. Internal panel headers and meaningful technical labels are allowed.
6. The image is not blank, severely cropped, severely overlapped, or layout-broken.
7. The final image is conceptually accurate relative to the original source image and its visible diagram content.

Title policy detail:
- Apply title policy only to Image 1. Ignore any title/header/banner that appears only in Image 2.
- FAIL if Image 1 has a large top banner/title bar such as a full-width dark strip with the whole topic name.
- PASS is possible when labels inside boxes, columns, rows, flow steps, or local panels remain as internal diagram content.

Return strict JSON only, no markdown:
{{
  "verdict": "PASS" | "FAIL" | "REVIEW",
  "confidence": 0.0,
  "style_converted_ok": true,
  "content_preserved_ok": true,
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
    request = urllib.request.Request(
        API_URL_TEMPLATE.format(model=model),
        data=json.dumps(payload, ensure_ascii=False).encode("utf-8"),
        headers={"Content-Type": "application/json", "x-goog-api-key": api_key},
        method="POST",
    )
    try:
        with urllib.request.urlopen(request, timeout=timeout, context=ssl.create_default_context()) as response:
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
    if not dimension_ok and verdict == "PASS":
        return "FAIL"
    critical_flags = [
        "style_converted_ok",
        "content_preserved_ok",
        "title_policy_ok",
        "no_internal_code_or_filename",
        "korean_text_ok",
        "layout_ok",
        "concept_accuracy_ok",
    ]
    if verdict == "PASS" and any(review.get(flag) is False for flag in critical_flags):
        return "FAIL"
    return verdict


def load_rows(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as file:
        return list(csv.DictReader(file))


def write_results(path: Path, rows: list[dict[str, Any]]) -> None:
    fields = [
        "code",
        "title",
        "model",
        "verdict",
        "confidence",
        "style_converted_ok",
        "content_preserved_ok",
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
    with path.open("w", encoding="utf-8-sig", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def load_existing_review_results(path: Path) -> dict[str, dict[str, Any]]:
    if not path.exists():
        return {}
    with path.open("r", encoding="utf-8-sig", newline="") as file:
        return {row["code"]: row for row in csv.DictReader(file) if row.get("code")}


def result_row(
    row: dict[str, str],
    model: str,
    response_path: Path,
    review: dict[str, Any],
    verdict: str,
    actual_size: tuple[int, int],
    dimension_ok: bool,
) -> dict[str, Any]:
    reasons = review.get("failure_reasons_ko") or []
    observed = review.get("observed_issues_ko") or []
    return {
        "code": row["code"],
        "title": row["title"],
        "model": model,
        "verdict": verdict,
        "confidence": review.get("confidence", ""),
        "style_converted_ok": review.get("style_converted_ok", ""),
        "content_preserved_ok": review.get("content_preserved_ok", ""),
        "title_policy_ok": review.get("title_policy_ok", ""),
        "no_internal_code_or_filename": review.get("no_internal_code_or_filename", ""),
        "korean_text_ok": review.get("korean_text_ok", ""),
        "layout_ok": review.get("layout_ok", ""),
        "concept_accuracy_ok": review.get("concept_accuracy_ok", ""),
        "expected_width": row["expected_width"],
        "expected_height": row["expected_height"],
        "actual_width": actual_size[0],
        "actual_height": actual_size[1],
        "dimension_ok": dimension_ok,
        "summary_ko": review.get("summary_ko", ""),
        "failure_reasons_ko": " | ".join(map(str, reasons)),
        "observed_issues_ko": " | ".join(map(str, observed)),
        "source_path": row["source_path"],
        "output_path": row["output_path"],
        "response_json": str(response_path),
    }


def select_rows(rows: list[dict[str, str]], codes: set[str], limit: int | None) -> list[dict[str, str]]:
    selected = [
        row
        for row in rows
        if row.get("status") == "OK" and (not codes or row.get("code") in codes)
    ]
    if limit is not None:
        selected = selected[:limit]
    return selected


def main() -> int:
    parser = argparse.ArgumentParser(description="Review Part1 DOCX SVG-style regeneration outputs.")
    parser.add_argument("--root", type=Path, default=None)
    parser.add_argument("--results", type=Path, default=None)
    parser.add_argument("--code", action="append", default=[])
    parser.add_argument("--limit", type=int, default=None)
    parser.add_argument("--model", default="gemini-2.5-flash")
    parser.add_argument("--timeout", type=int, default=120)
    parser.add_argument("--sleep", type=float, default=1.0)
    parser.add_argument("--max-side", type=int, default=1600)
    parser.add_argument("--jpeg-quality", type=int, default=88)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    root = args.root or default_root()
    guide = guide_dir(root)
    source_results = args.results or guide / "part1_docx_style_regeneration_results.csv"
    rows = select_rows(load_rows(source_results), set(args.code), args.limit)
    if not rows:
        print("No rows selected.")
        return 0

    print(f"root={root}")
    print(f"source_results={source_results}")
    print(f"selected={len(rows)} model={args.model}")
    for row in rows[:20]:
        print(f"- {row['code']} {row['title']}")
    if len(rows) > 20:
        print(f"... {len(rows) - 20} more")
    if args.dry_run:
        return 0

    api_key = os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY")
    if not api_key:
        print("ERROR: Set GEMINI_API_KEY or GOOGLE_API_KEY.", file=sys.stderr)
        return 2

    responses = guide / "part1_docx_second_review_responses"
    responses.mkdir(parents=True, exist_ok=True)
    out_results = guide / "part1_docx_second_review_results.csv"
    result_by_code = load_existing_review_results(out_results)
    failures = 0

    for index, row in enumerate(rows, start=1):
        source = Path(row["source_path"])
        output = Path(row["output_path"])
        response_path = responses / f"{row['code']}.json"
        if not source.exists():
            raise FileNotFoundError(f"Missing source image for {row['code']}: {source}")
        if not output.exists():
            raise FileNotFoundError(f"Missing output image for {row['code']}: {output}")

        expected = (int(row["expected_width"]), int(row["expected_height"]))
        actual = image_dimensions(output)
        dimension_ok = actual == expected
        parts = [
            image_part(output, args.max_side, args.jpeg_quality),
            image_part(source, args.max_side, args.jpeg_quality),
        ]
        print(f"[{index}/{len(rows)}] reviewing {row['code']} ...")
        try:
            response = post_review(api_key, args.model, build_prompt(row), parts, args.timeout)
            response_path.write_text(json.dumps(response, ensure_ascii=False, indent=2), encoding="utf-8")
            review = parse_review(response)
            verdict = normalize_verdict(review, dimension_ok)
        except Exception as exc:
            failures += 1
            response_path.write_text(json.dumps({"error": str(exc)}, ensure_ascii=False, indent=2), encoding="utf-8")
            review = {
                "verdict": "REVIEW",
                "confidence": 0,
                "style_converted_ok": False,
                "content_preserved_ok": False,
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

        result_by_code[row["code"]] = result_row(row, args.model, response_path, review, verdict, actual, dimension_ok)
        write_results(out_results, [result_by_code[code] for code in sorted(result_by_code)])
        print(f"  -> {verdict}")
        time.sleep(args.sleep)

    print(f"results={out_results}")
    print(f"responses={responses}")
    print(f"failures={failures}")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
