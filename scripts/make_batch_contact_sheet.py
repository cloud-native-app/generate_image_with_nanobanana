from __future__ import annotations

import argparse
import csv
from pathlib import Path

from PIL import Image, ImageDraw

from render_batch03_text_fixes import ROOT, font, text_center


GUIDE = ROOT / "00_가이드"


def build_sheet(rows: list[dict[str, str]], out: Path) -> Path:
    thumb_w, thumb_h = 300, 167
    label_h = 46
    pad = 18
    cols = 5
    sheet_rows = (len(rows) + cols - 1) // cols
    sheet_w = cols * thumb_w + (cols + 1) * pad
    sheet_h = sheet_rows * (label_h + thumb_h) + (sheet_rows + 1) * pad
    sheet = Image.new("RGB", (sheet_w, sheet_h), "white")
    draw = ImageDraw.Draw(sheet)

    for idx, row in enumerate(rows):
        col = idx % cols
        sheet_row = idx // cols
        x = pad + col * (thumb_w + pad)
        y = pad + sheet_row * (label_h + thumb_h + pad)
        label = row.get("code", "")
        title = row.get("title", "")
        if title:
            label = f"{label} · {title[:14]}"
        text_center(draw, (x, y, x + thumb_w, y + label_h), label, font(17, True), "#102A43")

        path = Path(row["output_abs"])
        with Image.open(path) as img:
            img = img.convert("RGB")
            img.thumbnail((thumb_w, thumb_h), Image.Resampling.LANCZOS)
            tile = Image.new("RGB", (thumb_w, thumb_h), "#F3F6F8")
            tile.paste(img, ((thumb_w - img.width) // 2, (thumb_h - img.height) // 2))
        sheet.paste(tile, (x, y + label_h))
        draw.rectangle((x, y + label_h, x + thumb_w, y + label_h + thumb_h), outline="#17395A", width=2)

    sheet.save(out)
    return out


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--batch", required=True)
    parser.add_argument("--prefix", default="nano_banana")
    args = parser.parse_args()

    csv_path = GUIDE / f"batch{args.batch}_{args.prefix}_검수결과.csv"
    out = GUIDE / f"batch{args.batch}_{args.prefix}_contact_sheet.png"
    with csv_path.open("r", encoding="utf-8-sig", newline="") as f:
        rows = list(csv.DictReader(f))
    if not rows:
        raise ValueError(f"No rows in {csv_path}")
    print(build_sheet(rows, out))


if __name__ == "__main__":
    main()
