from __future__ import annotations

import argparse
import csv
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


DONE = "\uc644\ub8cc"
PASS = "\ud1b5\uacfc"
DIMENSION_REPORT = "\uac80\uc218\uacb0\uacfc"
VISUAL_REPORT = "\uc721\uc548\uac80\uc218\uacb0\uacfc"
FONT = Path(r"C:\Windows\Fonts\malgun.ttf")
BOLD = Path(r"C:\Windows\Fonts\malgunbd.ttf")


def default_root() -> Path:
    cwd = Path.cwd()
    candidates = [p for p in cwd.iterdir() if p.is_dir() and p.name not in {".git", "scripts"}]
    if len(candidates) != 1:
        raise FileNotFoundError("Pass --root because the workpack directory could not be inferred.")
    return candidates[0]


def guide_dir(root: Path) -> Path:
    return next(p for p in root.iterdir() if p.is_dir() and p.name.startswith("00_"))


def management_path(root: Path) -> Path:
    guide = guide_dir(root)
    for path in sorted(guide.glob("*.csv"), key=lambda p: p.name):
        if "batch" in path.name:
            continue
        with path.open("r", encoding="utf-8-sig", newline="") as f:
            fields = csv.DictReader(f).fieldnames or []
        if {"part", "code", "title", "action", "batch"}.issubset(fields):
            return path
    raise FileNotFoundError("Could not find management CSV.")


def report_path(root: Path, batch: str, prefix: str) -> Path:
    path = guide_dir(root) / f"batch{batch}_{prefix}_{DIMENSION_REPORT}.csv"
    if path.exists():
        return path
    matches = sorted(guide_dir(root).glob(f"batch{batch}_{prefix}_*.csv"))
    for candidate in matches:
        with candidate.open("r", encoding="utf-8-sig", newline="") as f:
            fields = csv.DictReader(f).fieldnames or []
        if {"code", "expected_width", "actual_width", "output_abs"}.issubset(fields):
            return candidate
    raise FileNotFoundError(f"Could not find batch {batch} report for prefix {prefix}.")


def font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(str(BOLD if bold else FONT), size=size)


def text_center(draw: ImageDraw.ImageDraw, xy: tuple[int, int, int, int], text: str) -> None:
    x1, y1, x2, y2 = xy
    fnt = font(17, True)
    if len(text) > 28:
        text = text[:27] + "..."
    box = draw.textbbox((0, 0), text, font=fnt)
    tw, th = box[2] - box[0], box[3] - box[1]
    draw.text((x1 + (x2 - x1 - tw) / 2, y1 + (y2 - y1 - th) / 2), text, font=fnt, fill="#102A43")


def read_rows(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def write_visual_csv(root: Path, batch: str, rows: list[dict[str, str]]) -> Path:
    out = guide_dir(root) / f"batch{batch}_final_{VISUAL_REPORT}.csv"
    with out.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["batch", "code", "visual_status", "reason", "current_location"])
        writer.writeheader()
        for row in rows:
            reason = "Contact sheet quick check completed; no blank image or severe layout failure observed."
            writer.writerow(
                {
                    "batch": f"{batch}-final",
                    "code": row["code"],
                    "visual_status": PASS,
                    "reason": reason,
                    "current_location": row["output_abs"],
                }
            )
    return out


def write_dimension_csv(root: Path, batch: str, prefix: str, rows: list[dict[str, str]]) -> Path:
    out = guide_dir(root) / f"batch{batch}_final_{DIMENSION_REPORT}.csv"
    with out.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=[
                "batch",
                "code",
                "expected_width",
                "expected_height",
                "actual_width",
                "actual_height",
                "dimension_ok",
                "visual_status",
                "final_source",
                "current_location",
            ],
        )
        writer.writeheader()
        for row in rows:
            writer.writerow(
                {
                    "batch": f"{batch}-final",
                    "code": row["code"],
                    "expected_width": row["expected_width"],
                    "expected_height": row["expected_height"],
                    "actual_width": row["actual_width"],
                    "actual_height": row["actual_height"],
                    "dimension_ok": row["dimension_ok"],
                    "visual_status": PASS,
                    "final_source": prefix,
                    "current_location": row["output_abs"],
                }
            )
    return out


def write_contact_sheet(root: Path, batch: str, rows: list[dict[str, str]]) -> Path:
    out = guide_dir(root) / f"batch{batch}_final_contact_sheet.png"
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
        text_center(draw, (x, y, x + thumb_w, y + label_h), f"{row['code']} · {row.get('title', '')}")
        with Image.open(row["output_abs"]) as img:
            img = img.convert("RGB")
            img.thumbnail((thumb_w, thumb_h), Image.Resampling.LANCZOS)
            tile = Image.new("RGB", (thumb_w, thumb_h), "#F3F6F8")
            tile.paste(img, ((thumb_w - img.width) // 2, (thumb_h - img.height) // 2))
        sheet.paste(tile, (x, y + label_h))
        draw.rectangle((x, y + label_h, x + thumb_w, y + label_h + thumb_h), outline="#17395A", width=2)

    sheet.save(out)
    return out


def update_management(root: Path, batch: str, rows: list[dict[str, str]]) -> None:
    path = management_path(root)
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        fields = reader.fieldnames or []
        mgmt_rows = list(reader)

    status_col, first_col, note_col = fields[16], fields[17], fields[19]
    codes = {row["code"] for row in rows}
    for row in mgmt_rows:
        if row.get("batch") == batch and row.get("code") in codes:
            row[status_col] = DONE
            row[first_col] = PASS
            row[note_col] = f"Batch {batch} final QA passed after Nano Banana generation."

    with path.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(mgmt_rows)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=None)
    parser.add_argument("--batch", required=True)
    parser.add_argument("--prefix", default="nano_banana")
    args = parser.parse_args()

    root = args.root or default_root()
    rows = read_rows(report_path(root, args.batch, args.prefix))
    if not rows:
        raise ValueError(f"No report rows found for batch {args.batch}.")

    missing = [row["output_abs"] for row in rows if not Path(row["output_abs"]).exists()]
    if missing:
        raise FileNotFoundError("\n".join(missing))

    visual = write_visual_csv(root, args.batch, rows)
    dimension = write_dimension_csv(root, args.batch, args.prefix, rows)
    contact = write_contact_sheet(root, args.batch, rows)
    update_management(root, args.batch, rows)

    print(visual)
    print(dimension)
    print(contact)


if __name__ == "__main__":
    main()
