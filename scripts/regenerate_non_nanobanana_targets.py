from __future__ import annotations

import argparse
import base64
import csv
import json
import os
import time
import urllib.error
import urllib.request
from io import BytesIO
from pathlib import Path
from typing import Any

from PIL import Image, ImageOps


INTERACTIONS_URL = "https://generativelanguage.googleapis.com/v1beta/interactions"

DEFAULT_TARGET_CODES = [
    "P1-F32",
    "P1-F52",
    "P2-F14",
    "P2-F18",
    "P2-F20",
    "P2-F21",
    "P2-F31",
    "P2-F32",
    "P2-F33",
    "P2-F41",
    "P2-F51",
    "P2-F61",
    "P2-F62",
    "P2-F64",
    "P2-F65",
]


def default_root() -> Path:
    candidates = [
        path
        for path in Path.cwd().iterdir()
        if path.is_dir() and path.name not in {".git", "scripts"}
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


def completed_dir(root: Path) -> Path:
    return first_dir(root, "03_")


def management_path(root: Path) -> Path:
    for path in sorted(guide_dir(root).glob("*.csv")):
        try:
            with path.open("r", encoding="utf-8-sig", newline="") as f:
                fields = csv.DictReader(f).fieldnames or []
        except UnicodeDecodeError:
            continue
        if {"part", "code", "title", "action", "priority", "workpack_source", "output_filename"}.issubset(fields):
            return path
    raise FileNotFoundError("Could not locate the management CSV.")


def load_management(root: Path) -> tuple[Path, list[dict[str, str]]]:
    path = management_path(root)
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        return path, list(csv.DictReader(f))


def prompt_path(root: Path, code: str) -> Path:
    matches = sorted(guide_dir(root).rglob(f"{code}.txt"))
    if len(matches) != 1:
        raise FileNotFoundError(f"Expected one prompt file for {code}, found {len(matches)}.")
    return matches[0]


def source_path(root: Path, row: dict[str, str]) -> Path:
    source = root / Path(row["workpack_source"])
    if source.exists():
        return source
    absolute = Path(row.get("input_abs", ""))
    if absolute.exists():
        return absolute
    raise FileNotFoundError(f"Missing source image for {row['code']}: {source}")


def output_path(root: Path, row: dict[str, str]) -> Path:
    return completed_dir(root) / f"Part{row['part']}" / row["output_filename"]


def image_part(path: Path) -> dict[str, str]:
    return {
        "type": "image",
        "mime_type": "image/png",
        "data": base64.b64encode(path.read_bytes()).decode("ascii"),
    }


def build_prompt(row: dict[str, str], prompt_text: str) -> str:
    title_policy = row.get("title_policy", "")
    title_rule = (
        "Part2 images must not render a top title, figure code, filename, prompt text, or duplicated caption text. "
        "Start directly with the diagram body, panel headers, flow labels, or core concept boxes. "
        if row["part"] != "1"
        else "Follow the Part1 title policy exactly; do not render the figure code or filename. "
    )
    return f"""
You are regenerating a Korean information-security study diagram with Nano Banana / Gemini image style.

This target was classified as a hand-made flat SVG-style diagram, so redraw it as a polished Nano Banana style infographic:
- richer illustrated icons and devices, subtle depth, clean educational diagram composition
- white background, navy/teal/light gray palette, red only for risks or warnings
- accurate Korean labels, no pseudo-Korean, no misspellings
- preserve the learning intent and required correction, but do not copy the flat SVG look

Reference:
- code for tracking only: {row['code']}
- topic for understanding only: {row['title']}
- action: {row['action']}
- title policy: {title_policy}
- canvas: {row['source_width']} x {row['source_height']} px

Important title rule:
{title_rule}
Do not prefix any protocol message, panel title, row label, or section title with bracketed labels such as [A1], [B1], [Part 1], [1], or [2].
Use plain semantic labels only.

Known issue to fix:
{row.get('issue', '')}

Required correction:
{row.get('required_correction', '')}

Original per-image instruction follows. Use it as content guidance, not as visible text:
{prompt_text}

Output requirements:
- Return exactly one PNG-like image.
- Keep the final image suitable for the specified canvas.
- Do not include watermark, file path, filename, code, model name, version string, or prompt sentences.
- Do not create decorative arrows unrelated to the information flow.
""".strip()


def post_json(url: str, api_key: str, payload: dict[str, Any], timeout: int) -> dict[str, Any]:
    request = urllib.request.Request(
        url,
        data=json.dumps(payload, ensure_ascii=False).encode("utf-8"),
        headers={"Content-Type": "application/json", "x-goog-api-key": api_key},
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
        if str(obj.get("mime_type", "")).startswith("image/") and isinstance(obj.get("data"), str):
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


def write_results(path: Path, rows: list[dict[str, Any]]) -> None:
    fields = [
        "code",
        "part",
        "batch",
        "title",
        "model",
        "source_path",
        "output_path",
        "response_json",
        "expected_width",
        "expected_height",
        "actual_width",
        "actual_height",
        "dimension_ok",
        "status",
        "note",
    ]
    with path.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def load_existing_results(path: Path) -> dict[str, dict[str, Any]]:
    if not path.exists():
        return {}
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        return {row["code"]: row for row in csv.DictReader(f) if row.get("code")}


def main() -> int:
    parser = argparse.ArgumentParser(description="Regenerate the currently available non-Nano-Banana style targets.")
    parser.add_argument("--root", type=Path, default=None)
    parser.add_argument("--code", action="append", default=[])
    parser.add_argument("--model", default="gemini-3.1-flash-image")
    parser.add_argument("--timeout", type=int, default=180)
    parser.add_argument("--sleep", type=float, default=2.0)
    parser.add_argument("--limit", type=int, default=None)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--continue-on-error", action="store_true")
    args = parser.parse_args()

    root = args.root or default_root()
    _, rows = load_management(root)
    row_by_code = {row["code"]: row for row in rows}
    target_codes = args.code or DEFAULT_TARGET_CODES
    selected = [row_by_code[code] for code in target_codes if code in row_by_code]
    if args.limit is not None:
        selected = selected[: args.limit]
    if not selected:
        print("No rows selected.")
        return 0

    print(f"root={root}")
    print(f"selected={len(selected)} model={args.model}")
    for row in selected:
        print(f"- {row['code']} {row['title']} -> {output_path(root, row)}")
    if args.dry_run:
        return 0

    api_key = os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY")
    if not api_key:
        print("ERROR: Set GEMINI_API_KEY or GOOGLE_API_KEY.")
        return 2

    response_dir = guide_dir(root) / "style_regeneration_responses"
    response_dir.mkdir(parents=True, exist_ok=True)
    results_path = guide_dir(root) / "style_regeneration_results.csv"
    result_by_code = load_existing_results(results_path)
    failures = 0

    for index, row in enumerate(selected, start=1):
        code = row["code"]
        src = source_path(root, row)
        out = output_path(root, row)
        out.parent.mkdir(parents=True, exist_ok=True)
        response_json = response_dir / f"{code}.json"
        prompt = build_prompt(row, prompt_path(root, code).read_text(encoding="utf-8"))
        payload = {
            "model": args.model,
            "input": [{"type": "text", "text": prompt}, image_part(src)],
        }
        print(f"[{index}/{len(selected)}] regenerating {code} ...")
        try:
            response = post_json(INTERACTIONS_URL, api_key, payload, args.timeout)
            response_json.write_text(json.dumps(response, ensure_ascii=False, indent=2), encoding="utf-8")
            image_data = find_output_image_data(response)
            if not image_data:
                raise RuntimeError(f"Gemini response did not contain image data. See {response_json}")
            expected = (int(row["source_width"]), int(row["source_height"]))
            normalized = normalize_image(base64.b64decode(image_data), expected)
            normalized.save(out)
            with Image.open(out) as saved:
                actual = saved.size
            dimension_ok = actual == expected
            status = "OK" if dimension_ok else "SIZE_MISMATCH"
            note = "Regenerated from non-Nano-Banana style classification."
        except Exception as exc:
            failures += 1
            actual = ("", "")
            dimension_ok = False
            status = "ERROR"
            note = str(exc)
            print(f"ERROR {code}: {exc}")
            if not args.continue_on_error:
                raise
        result_by_code[code] = {
            "code": code,
            "part": row["part"],
            "batch": row["batch"],
            "title": row["title"],
            "model": args.model,
            "source_path": str(src),
            "output_path": str(out),
            "response_json": str(response_json),
            "expected_width": row["source_width"],
            "expected_height": row["source_height"],
            "actual_width": actual[0],
            "actual_height": actual[1],
            "dimension_ok": dimension_ok,
            "status": status,
            "note": note,
        }
        write_results(results_path, list(result_by_code.values()))
        time.sleep(args.sleep)

    print(f"results={results_path}")
    print(f"responses={response_dir}")
    print(f"failures={failures}")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
