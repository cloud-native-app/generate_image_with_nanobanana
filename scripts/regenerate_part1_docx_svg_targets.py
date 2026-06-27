from __future__ import annotations

import argparse
import base64
import csv
import json
import os
import re
import time
import urllib.error
import urllib.request
import zipfile
from io import BytesIO
from pathlib import Path
from typing import Any
import xml.etree.ElementTree as ET

from PIL import Image, ImageDraw, ImageFont, ImageOps


INTERACTIONS_URL = "https://generativelanguage.googleapis.com/v1beta/interactions"

NANO_BANANA_LIKE_CODES = {
    "P1-F01",
    "P1-F02",
    "P1-F03",
    "P1-F04",
    "P1-F05",
    "P1-F22",
    "P1-F24",
    "P1-F28",
    "P1-F29",
    "P1-F34",
    "P1-F41",
    "P1-F42",
}

ALREADY_REGENERATED_CODES = {
    "P1-F32",
    "P1-F52",
}

FORCE_REMOVE_TOP_TITLE_CODES = {
    "P1-F07",
    "P1-F08",
    "P1-F10",
    "P1-F12",
    "P1-F13",
    "P1-F14",
    "P1-F16",
    "P1-F25",
    "P1-F35",
    "P1-F36",
    "P1-F40",
    "P1-F45",
    "P1-F46",
    "P1-F49",
    "P1-F54",
}

TITLE_CROP_FRACTIONS = {
    "P1-F25": 0.08,
    "P1-F35": 0.10,
    "P1-F36": 0.10,
    "P1-F49": 0.08,
}

SPECIAL_CODE_INSTRUCTIONS = {
    "P1-F47": (
        "Preserve the original single cyclic ring structure. Do not add a separate external "
        "containment/isolation panel; keep containment/isolation only as an internal ring segment if present."
    ),
}

PART1_SVG_TARGET_CODES = [
    f"P1-F{number:02d}"
    for number in range(1, 56)
    if f"P1-F{number:02d}" not in NANO_BANANA_LIKE_CODES
    and f"P1-F{number:02d}" not in ALREADY_REGENERATED_CODES
]

NS = {
    "w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main",
    "a": "http://schemas.openxmlformats.org/drawingml/2006/main",
    "r": "http://schemas.openxmlformats.org/officeDocument/2006/relationships",
}


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


def completed_part1_dir(root: Path) -> Path:
    path = first_dir(root, "03_") / "Part1"
    path.mkdir(parents=True, exist_ok=True)
    return path


def rel_target_to_media_path(target: str) -> str:
    return target if target.startswith("word/") else f"word/{target}"


def paragraph_text(paragraph: ET.Element) -> str:
    return "".join(text.text or "" for text in paragraph.findall(".//w:t", NS)).strip()


def nearby_text(paragraphs: list[tuple[int, str, list[str]]], index: int, direction: int, span: int) -> list[str]:
    out: list[str] = []
    stop = index + direction * span
    for cursor in range(index + direction, stop, direction):
        if cursor < 0 or cursor >= len(paragraphs):
            break
        text = paragraphs[cursor][1]
        if text:
            out.append(text)
    return out


def choose_reference_title(before: list[str], after: list[str], code: str) -> str:
    heading_pattern = re.compile(r"^\d+(?:\.\d+)*\s+.{2,80}$")
    for text in [*after[:4], *before[:8]]:
        if heading_pattern.match(text) and len(text) <= 90:
            return text
    for text in [*before, *after]:
        if 4 <= len(text) <= 90:
            return text
    return f"{code} Part1 system security figure"


def extract_docx_figures(docx: Path, root: Path, target_codes: set[str]) -> dict[str, dict[str, str]]:
    extract_dir = guide_dir(root) / "part1_docx_extracted_sources"
    extract_dir.mkdir(parents=True, exist_ok=True)

    with zipfile.ZipFile(docx) as archive:
        document = ET.fromstring(archive.read("word/document.xml"))
        rels = ET.fromstring(archive.read("word/_rels/document.xml.rels"))
        rid_to_target = {
            rel.attrib["Id"]: rel.attrib["Target"]
            for rel in rels
            if rel.attrib.get("Type", "").endswith("/image")
        }
        paragraphs: list[tuple[int, str, list[str]]] = []
        for index, paragraph in enumerate(document.findall(".//w:p", NS)):
            rids: list[str] = []
            for blip in paragraph.findall(".//a:blip", NS):
                rid = blip.attrib.get(f"{{{NS['r']}}}embed") or blip.attrib.get(f"{{{NS['r']}}}link")
                if rid:
                    rids.append(rid)
            paragraphs.append((index, paragraph_text(paragraph), rids))

        figures: dict[str, dict[str, str]] = {}
        figure_number = 0
        for index, _, rids in paragraphs:
            for rid in rids:
                target = rid_to_target.get(rid)
                if not target:
                    continue
                figure_number += 1
                code = f"P1-F{figure_number:02d}"
                if code not in target_codes:
                    continue

                media_path = rel_target_to_media_path(target)
                before = nearby_text(paragraphs, index, -1, 12)
                after = nearby_text(paragraphs, index, 1, 12)
                title = choose_reference_title(before, after, code)
                caption = f"{code} Part1 document figure order reference"
                purpose = " / ".join(after[:2] or before[:2])

                output = extract_dir / f"{code}.png"
                output.write_bytes(archive.read(media_path))
                with Image.open(output) as image:
                    width, height = image.size

                figures[code] = {
                    "code": code,
                    "title": title,
                    "caption": caption,
                    "purpose": purpose,
                    "source_path": str(output),
                    "source_width": str(width),
                    "source_height": str(height),
                    "media_path": media_path,
                    "before_text": " / ".join(before[:3]),
                    "after_text": " / ".join(after[:3]),
                }
    return figures


def image_part(path: Path) -> dict[str, str]:
    return {
        "type": "image",
        "mime_type": "image/png",
        "data": base64.b64encode(path.read_bytes()).decode("ascii"),
    }


def build_prompt(figure: dict[str, str]) -> str:
    special_instruction = SPECIAL_CODE_INSTRUCTIONS.get(figure["code"])
    special_block = ""
    if special_instruction:
        special_block = f"""

Code-specific preservation instruction:
- {special_instruction}
""".rstrip()

    return f"""
You are regenerating a Korean information-security study diagram with Nano Banana / Gemini image style.

Use the attached original figure as the authoritative content and layout reference.
This Part1 system-security figure was classified as a hand-made flat SVG-style or borderline diagram, so redraw it as a polished Nano Banana style infographic:
- richer dimensional icons, operating-system objects, users, processes, memory blocks, logs, servers, shields, and subtle depth where appropriate
- clean educational diagram composition on a white background
- navy, teal, light gray, and restrained red only for risks or warnings
- preserve the technical relationships, arrows, sequence, comparison structure, and Korean labels from the original
- accurate Korean labels only; no pseudo-Korean, no misspellings
- do not copy the flat SVG look

Tracking code, not visible text: {figure['code']}
Reference topic for understanding only, not visible text: {figure['title']}
Nearby context for understanding only: {figure['purpose']}
Target canvas: {figure['source_width']} x {figure['source_height']} px.
{special_block}

Important title rule:
- Do not render the figure code, filename, prompt text, or document caption.
- Never render the tracking code in any form, including "{figure['code']}", "({figure['code']})", or any figure-number label.
- If the source image contains a large top title/header/banner, treat it as document caption text and remove it from the regenerated image.
- Do not render any large top title/header/banner that names the whole diagram topic, even when it appears in the original.
- Do not render the reference topic text "{figure['title']}" as a visible title.
- The final image must not contain a full-width or near-full-width top strip whose only purpose is naming the whole topic.
- Reclaim that title space: scale and reflow the actual diagram body upward so the canvas does not look like a title was simply covered.
- Start directly with the diagram body, panel headers, flow labels, comparison rows, or core concept boxes near the top of the canvas.
- Internal panel headers and meaningful technical labels are allowed.
- Do not prefix protocol messages, panel titles, row labels, or section titles with bracketed labels such as [A1], [B1], [Part 1], [1], or [2].

Output requirements:
- Return exactly one PNG-like image.
- Keep the same aspect ratio and make the final image suitable for the target canvas.
- Do not include watermark, file path, filename, model name, version string, or prompt sentences.
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


def results_path(root: Path) -> Path:
    return guide_dir(root) / "part1_docx_style_regeneration_results.csv"


def response_dir(root: Path) -> Path:
    path = guide_dir(root) / "part1_docx_style_regeneration_responses"
    path.mkdir(parents=True, exist_ok=True)
    return path


def titleless_prompt_source_dir(root: Path) -> Path:
    path = guide_dir(root) / "part1_docx_titleless_prompt_sources"
    path.mkdir(parents=True, exist_ok=True)
    return path


def prompt_source_path(root: Path, figure: dict[str, str]) -> Path:
    source = Path(figure["source_path"])
    code = figure["code"]
    if code not in FORCE_REMOVE_TOP_TITLE_CODES:
        return source

    with Image.open(source) as image:
        converted = image.convert("RGB")
        crop_fraction = TITLE_CROP_FRACTIONS.get(code, 0.14)
        crop_top = max(1, min(converted.height // 4, round(converted.height * crop_fraction)))
        body = converted.crop((0, crop_top, converted.width, converted.height))
        body = body.resize(converted.size, Image.Resampling.LANCZOS)

    output = titleless_prompt_source_dir(root) / f"{code}.png"
    body.save(output)
    return output


def load_existing_results(path: Path) -> dict[str, dict[str, Any]]:
    if not path.exists():
        return {}
    with path.open("r", encoding="utf-8-sig", newline="") as file:
        return {row["code"]: row for row in csv.DictReader(file) if row.get("code")}


def write_results(path: Path, rows_by_code: dict[str, dict[str, Any]]) -> None:
    fields = [
        "code",
        "title",
        "caption",
        "purpose",
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
    rows = [rows_by_code[code] for code in sorted(rows_by_code)]
    with path.open("w", encoding="utf-8-sig", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def make_contact_sheet(root: Path, codes: list[str]) -> Path:
    thumbs: list[tuple[str, Image.Image]] = []
    for code in codes:
        path = completed_part1_dir(root) / f"{code}.png"
        if not path.exists():
            continue
        image = Image.open(path).convert("RGB")
        image.thumbnail((360, 200), Image.Resampling.LANCZOS)
        thumbs.append((code, image.copy()))

    columns = 4
    cell_w, cell_h = 400, 260
    rows = max(1, (len(thumbs) + columns - 1) // columns)
    sheet = Image.new("RGB", (columns * cell_w, rows * cell_h), "white")
    draw = ImageDraw.Draw(sheet)
    try:
        font = ImageFont.truetype("arial.ttf", 18)
    except OSError:
        font = ImageFont.load_default()

    for index, (code, image) in enumerate(thumbs):
        col = index % columns
        row = index // columns
        x = col * cell_w
        y = row * cell_h
        draw.rectangle([x, y, x + cell_w - 1, y + cell_h - 1], outline=(210, 220, 230))
        draw.text((x + 12, y + 10), code, fill=(15, 35, 55), font=font)
        sheet.paste(image, (x + (cell_w - image.width) // 2, y + 44))

    out = guide_dir(root) / "part1_docx_style_regeneration_contact_sheet.png"
    sheet.save(out)
    return out


def main() -> int:
    parser = argparse.ArgumentParser(description="Regenerate remaining Part1 DOCX SVG-style figures.")
    parser.add_argument("--docx", type=Path, default=None)
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
    docx = args.docx or Path(os.environ.get("PART1_DOCX_PATH", ""))
    if not docx.exists():
        raise FileNotFoundError("Pass --docx or set PART1_DOCX_PATH to the Part1 DOCX file.")

    target_codes = args.code or PART1_SVG_TARGET_CODES
    if args.limit is not None:
        target_codes = target_codes[: args.limit]
    figures = extract_docx_figures(docx, root, set(target_codes))
    selected = [figures[code] for code in target_codes if code in figures]
    missing = [code for code in target_codes if code not in figures]

    print(f"docx={docx}")
    print(f"root={root}")
    print(f"selected={len(selected)} model={args.model}")
    if missing:
        print(f"missing={','.join(missing)}")
    for figure in selected:
        print(f"- {figure['code']} {figure['title']} -> {completed_part1_dir(root) / (figure['code'] + '.png')}")
    if args.dry_run:
        return 0

    api_key = os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY")
    if not api_key:
        print("ERROR: Set GEMINI_API_KEY or GOOGLE_API_KEY.")
        return 2

    responses = response_dir(root)
    results = load_existing_results(results_path(root))
    failures = 0

    for index, figure in enumerate(selected, start=1):
        code = figure["code"]
        source = Path(figure["source_path"])
        prompt_source = prompt_source_path(root, figure)
        output = completed_part1_dir(root) / f"{code}.png"
        response_json = responses / f"{code}.json"
        prompt = build_prompt(figure)
        payload = {
            "model": args.model,
            "input": [{"type": "text", "text": prompt}, image_part(prompt_source)],
        }
        print(f"[{index}/{len(selected)}] regenerating {code} ...")
        try:
            response = post_json(INTERACTIONS_URL, api_key, payload, args.timeout)
            response_json.write_text(json.dumps(response, ensure_ascii=False, indent=2), encoding="utf-8")
            image_data = find_output_image_data(response)
            if not image_data:
                raise RuntimeError(f"Gemini response did not contain image data. See {response_json}")
            expected = (int(figure["source_width"]), int(figure["source_height"]))
            normalized = normalize_image(base64.b64decode(image_data), expected)
            normalized.save(output)
            with Image.open(output) as saved:
                actual = saved.size
            dimension_ok = actual == expected
            status = "OK" if dimension_ok else "SIZE_MISMATCH"
            note = "Regenerated from Part1 DOCX SVG-style source."
            if prompt_source != source:
                note += " Prompt source had top title area removed."
        except Exception as exc:
            failures += 1
            actual = ("", "")
            dimension_ok = False
            status = "ERROR"
            note = str(exc)
            print(f"ERROR {code}: {exc}")
            if not args.continue_on_error:
                raise

        results[code] = {
            "code": code,
            "title": figure["title"],
            "caption": figure["caption"],
            "purpose": figure["purpose"],
            "model": args.model,
            "source_path": str(source),
            "output_path": str(output),
            "response_json": str(response_json),
            "expected_width": figure["source_width"],
            "expected_height": figure["source_height"],
            "actual_width": actual[0],
            "actual_height": actual[1],
            "dimension_ok": dimension_ok,
            "status": status,
            "note": note,
        }
        write_results(results_path(root), results)
        time.sleep(args.sleep)

    sheet = make_contact_sheet(root, target_codes)
    print(f"results={results_path(root)}")
    print(f"responses={responses}")
    print(f"contact_sheet={sheet}")
    print(f"failures={failures}")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
