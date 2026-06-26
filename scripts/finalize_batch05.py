from __future__ import annotations

import csv
from pathlib import Path

from PIL import Image, ImageDraw

from render_batch03_text_fixes import ROOT, font, text_center


GUIDE = ROOT / "00_가이드"
COMPLETE = ROOT / "03_수정완료"
REWORK = ROOT / "04_재작업"
MANAGEMENT = GUIDE / "나노바나나_작업관리표_v2.csv"

BATCH = "05-final"

ITEMS = [
    ("P4-F33", "Part4", "nano_banana", "인증 없는 DH에서 MITM이 공개값을 대체하는 흐름과 방어 수단이 명확함. 전체 제목·코드 없음."),
    ("P4-F53", "Part4", "local_text_fix", "Feistel/SPN 라운드 구조와 복호화 차이 보정본 통과. 전체 제목·의미 없는 문장 없음."),
    ("P4-F54", "Part4", "nano_banana", "블록암호/스트림암호 비교 표와 공통 경고가 명확함. 개념 오류 없음."),
    ("P4-F58", "Part4", "nano_banana", "대표 대칭키 알고리즘 비교 표가 안정적이고 주요 블록/키/구조 정보가 읽힘."),
    ("P4-F64", "Part4", "nano_banana", "암호분석 공격 분류와 설명이 기능 패널로 분리되어 있고 개념 오류 없음."),
    ("P4-F65", "Part4", "local_text_fix", "IFP/DLP/ECDLP 패널과 RSA 2048≈ECC 224, RSA 3072≈ECC 256 비교가 정확함. ECC 3072 없음."),
    ("P4-F73", "Part4", "nano_banana", "Salt DB 저장, Pepper KMS/HSM 분리, KDF 검증자 저장과 유출 영향이 명확함."),
    ("P4-F74", "Part4", "local_text_fix", "Password KDF와 HKDF Extract/Expand 키 분리 경로가 명확하고 EXAM FOCUS·전체 제목 없음."),
    ("P4-F66", "Part4", "nano_banana_rerun", "RSA 작은 수 계산 p=11, q=13, n=143, phi(n)=120, e=7, d=103, C=48, M=9가 정확함. 전체 제목 없음."),
    ("P5-F05", "Part5", "nano_banana_rerun", "RACI 매트릭스와 업무별 A 1명 원칙이 명확함. 상단 번호·제목 없음."),
]


def final_path(code: str, part_dir: str) -> Path:
    return COMPLETE / part_dir / f"{code}.png"


def remove_stale_rework() -> list[Path]:
    removed: list[Path] = []
    base = REWORK.resolve()
    for code, part_dir, _, _ in ITEMS:
        path = (REWORK / part_dir / f"{code}.png").resolve()
        if path.exists() and path.is_file() and path.is_relative_to(base):
            path.unlink()
            removed.append(path)
    return removed


def write_visual_csv(paths: dict[str, Path]) -> Path:
    out = GUIDE / "batch05_final_육안검수결과.csv"
    with out.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["batch", "code", "visual_status", "reason", "current_location"])
        writer.writeheader()
        for code, _, _, reason in ITEMS:
            writer.writerow(
                {
                    "batch": BATCH,
                    "code": code,
                    "visual_status": "통과",
                    "reason": reason,
                    "current_location": str(paths[code]),
                }
            )
    return out


def write_dimension_csv(paths: dict[str, Path]) -> Path:
    out = GUIDE / "batch05_final_검수결과.csv"
    with out.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=[
                "batch",
                "code",
                "actual_width",
                "actual_height",
                "dimension_ok",
                "visual_status",
                "final_source",
                "current_location",
            ],
        )
        writer.writeheader()
        for code, _, source, _ in ITEMS:
            path = paths[code]
            with Image.open(path) as img:
                width, height = img.size
            writer.writerow(
                {
                    "batch": BATCH,
                    "code": code,
                    "actual_width": width,
                    "actual_height": height,
                    "dimension_ok": str((width, height) == (1600, 893)),
                    "visual_status": "통과",
                    "final_source": source,
                    "current_location": str(path),
                }
            )
    return out


def update_management() -> None:
    with MANAGEMENT.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        fields = reader.fieldnames or []
        rows = list(reader)

    status_col = fields[16]
    first_col = fields[17]
    note_col = fields[19]
    reasons = {code: reason for code, _, _, reason in ITEMS}
    codes = set(reasons)

    for row in rows:
        if row.get("batch") == "05" and row.get("code") in codes:
            row[status_col] = "완료"
            row[first_col] = "통과"
            row[note_col] = reasons[row["code"]]

    with MANAGEMENT.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def write_contact_sheet(paths: dict[str, Path]) -> Path:
    out = GUIDE / "batch05_final_contact_sheet.png"
    thumb_w, thumb_h = 300, 167
    label_h = 42
    pad = 18
    cols = 5
    rows = 2
    sheet_w = cols * thumb_w + (cols + 1) * pad
    sheet_h = rows * (label_h + thumb_h) + (rows + 1) * pad
    sheet = Image.new("RGB", (sheet_w, sheet_h), "white")
    draw = ImageDraw.Draw(sheet)

    for idx, (code, _, source, _) in enumerate(ITEMS):
        col = idx % cols
        row = idx // cols
        x = pad + col * (thumb_w + pad)
        y = pad + row * (label_h + thumb_h + pad)
        text_center(draw, (x, y, x + thumb_w, y + label_h), f"{code} · {source}", font(19, True), "#102A43")
        with Image.open(paths[code]) as img:
            img = img.convert("RGB")
            img.thumbnail((thumb_w, thumb_h), Image.Resampling.LANCZOS)
            tile = Image.new("RGB", (thumb_w, thumb_h), "#F3F6F8")
            tile.paste(img, ((thumb_w - img.width) // 2, (thumb_h - img.height) // 2))
        sheet.paste(tile, (x, y + label_h))
        draw.rectangle((x, y + label_h, x + thumb_w, y + label_h + thumb_h), outline="#17395A", width=2)

    sheet.save(out)
    return out


def main() -> None:
    paths = {code: final_path(code, part_dir) for code, part_dir, _, _ in ITEMS}
    missing = [str(path) for path in paths.values() if not path.exists()]
    if missing:
        raise FileNotFoundError("\n".join(missing))

    removed = remove_stale_rework()
    visual_csv = write_visual_csv(paths)
    dimension_csv = write_dimension_csv(paths)
    update_management()
    contact_sheet = write_contact_sheet(paths)

    print(f"removed_rework={len(removed)}")
    print(visual_csv)
    print(dimension_csv)
    print(contact_sheet)


if __name__ == "__main__":
    main()
