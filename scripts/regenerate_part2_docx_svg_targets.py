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

ALREADY_REGENERATED_CODES = {
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
}

PART2_SVG_TARGET_CODES = [
    f"P2-F{number:02d}"
    for number in range(11, 70)
    if f"P2-F{number:02d}" not in ALREADY_REGENERATED_CODES
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


def completed_part2_dir(root: Path) -> Path:
    path = first_dir(root, "03_") / "Part2"
    path.mkdir(parents=True, exist_ok=True)
    return path


def rel_target_to_media_path(target: str) -> str:
    return target if target.startswith("word/") else f"word/{target}"


def paragraph_text(paragraph: ET.Element) -> str:
    return "".join(text.text or "" for text in paragraph.findall(".//w:t", NS)).strip()


def extract_docx_figures(docx: Path, root: Path) -> dict[str, dict[str, str]]:
    extract_dir = guide_dir(root) / "part2_docx_extracted_sources"
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
        for index, _, rids in paragraphs:
            for rid in rids:
                target = rid_to_target.get(rid)
                if not target:
                    continue
                media_path = rel_target_to_media_path(target)
                number_match = re.search(r"fig(\d+)\.", media_path)
                if not number_match:
                    continue
                code = f"P2-F{int(number_match.group(1)):02d}"

                caption = ""
                for previous in range(index - 1, max(-1, index - 10), -1):
                    text = paragraphs[previous][1]
                    if text:
                        caption = text
                        break

                purpose = ""
                for following in range(index + 1, min(len(paragraphs), index + 10)):
                    text = paragraphs[following][1]
                    if text:
                        purpose = text
                        break

                output = extract_dir / f"{code}.png"
                output.write_bytes(archive.read(media_path))
                with Image.open(output) as image:
                    width, height = image.size

                title = caption
                title_match = re.match(r"\[P2-F\d+\]\s*(.+)", caption)
                if title_match:
                    title = title_match.group(1)

                figures[code] = {
                    "code": code,
                    "title": title,
                    "caption": caption,
                    "purpose": purpose,
                    "source_path": str(output),
                    "source_width": str(width),
                    "source_height": str(height),
                    "media_path": media_path,
                }
    return figures


def image_part(path: Path) -> dict[str, str]:
    return {
        "type": "image",
        "mime_type": "image/png",
        "data": base64.b64encode(path.read_bytes()).decode("ascii"),
    }


def build_prompt(figure: dict[str, str]) -> str:
    return f"""
You are regenerating a Korean information-security study diagram with Nano Banana / Gemini image style.

Use the attached original figure as the authoritative content and layout reference.
This Part2 figure was classified as a hand-made flat SVG-style diagram, so redraw it as a polished Nano Banana style infographic:
- richer dimensional icons, network devices, packets, servers, shields, and subtle depth where appropriate
- clean educational diagram composition on a white background
- navy, teal, light gray, and restrained red only for risks or warnings
- preserve the technical relationships, arrows, sequence, comparison structure, and Korean labels from the original
- accurate Korean labels only; no pseudo-Korean, no misspellings
- do not copy the flat SVG look

Tracking code, not visible text: {figure['code']}
Caption for understanding only, not visible text: {figure['caption']}
Purpose for understanding only: {figure['purpose']}
Target canvas: {figure['source_width']} x {figure['source_height']} px.

Important title rule:
- Do not render the figure code, filename, prompt text, or document caption.
- Never render the tracking code in any form, including "{figure['code']}", "({figure['code']})", or any figure-number label.
- Do not render a large top title that duplicates the caption.
- Start directly with the diagram body, panel headers, flow labels, comparison rows, or core concept boxes.
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
    return guide_dir(root) / "part2_docx_style_regeneration_results.csv"


def response_dir(root: Path) -> Path:
    path = guide_dir(root) / "part2_docx_style_regeneration_responses"
    path.mkdir(parents=True, exist_ok=True)
    return path


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
        path = completed_part2_dir(root) / f"{code}.png"
        if not path.exists():
            continue
        image = Image.open(path).convert("RGB")
        image.thumbnail((360, 192), Image.Resampling.LANCZOS)
        thumbs.append((code, image.copy()))

    columns = 4
    cell_w, cell_h = 400, 250
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

    out = guide_dir(root) / "part2_docx_style_regeneration_contact_sheet.png"
    sheet.save(out)
    return out


def main() -> int:
    parser = argparse.ArgumentParser(description="Regenerate remaining Part2 DOCX SVG-style figures.")
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
    docx = args.docx or Path(os.environ.get("PART2_DOCX_PATH", ""))
    if not docx.exists():
        raise FileNotFoundError("Pass --docx or set PART2_DOCX_PATH to the Part2 DOCX file.")

    figures = extract_docx_figures(docx, root)
    target_codes = args.code or PART2_SVG_TARGET_CODES
    if args.limit is not None:
        target_codes = target_codes[: args.limit]
    selected = [figures[code] for code in target_codes if code in figures]
    missing = [code for code in target_codes if code not in figures]

    print(f"docx={docx}")
    print(f"root={root}")
    print(f"selected={len(selected)} model={args.model}")
    if missing:
        print(f"missing={','.join(missing)}")
    for figure in selected:
        print(f"- {figure['code']} {figure['title']} -> {completed_part2_dir(root) / (figure['code'] + '.png')}")
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
        output = completed_part2_dir(root) / f"{code}.png"
        response_json = responses / f"{code}.json"
        prompt = build_prompt(figure)
        payload = {
            "model": args.model,
            "input": [{"type": "text", "text": prompt}, image_part(source)],
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
            note = "Regenerated from Part2 DOCX SVG-style source."
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
