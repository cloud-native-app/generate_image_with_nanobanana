from __future__ import annotations

import csv
from pathlib import Path

from PIL import Image, ImageDraw

from render_batch03_text_fixes import ROOT, font, text_center


GUIDE = ROOT / "00_가이드"
COMPLETE = ROOT / "03_수정완료"
REWORK = ROOT / "04_재작업"
MANAGEMENT = GUIDE / "나노바나나_작업관리표_v2.csv"

BATCH = "06-final"

ITEMS = [
    ("P5-F26", "Part5", "nano_banana", "물리보안 구역, 인증요건, 출입기록, 반입·반출 통제와 Tailgating 방지가 명확함. 전체 제목·코드 없음."),
    ("P5-F41", "Part5", "nano_banana", "레지스터·캐시부터 원격 로그·백업까지 휘발성 우선순위가 명확하고 수집 영향 판단 기준이 적절함."),
    ("P5-F42", "Part5", "nano_banana", "디지털 증거 식별-보존-수집-검사-분석-보고-보관/폐기 생명주기와 무결성 관리가 명확함."),
    ("P5-F46", "Part5", "nano_banana_rerun", "ISMS-P 3개 영역과 16·64·21, 총 101개 기준이 정확하고 상단 전체 제목·오탈자 없음."),
    ("P5-F49", "Part5", "nano_banana", "CC 인증에서 PP, ST, TOE, SFR/SAR, EAL과 평가·인증 흐름이 명확함."),
    ("P5-F53", "Part5", "nano_banana_rerun", "조직 인증과 제품 인증의 범위, 평가대상, 인증근거 차이가 명확하고 시험 강조 문구 없음."),
    ("P5-F54", "Part5", "local_text_fix", "디지털 시민의 책임·존중·공정·안전·프라이버시·지식재산 원칙과 윤리 판단 문구가 정확함."),
    ("P5-F55", "Part5", "local_text_fix", "게시 전 점검, 게시, 타인 확산, 문제 발생 시 대응과 익명성 책임 문구가 정확함."),
    ("P5-F64", "Part5", "local_text_fix", "국내 정보보호 관련 법률별 보호대상과 목적 차이가 정확하며 영어 오탈자·전체 제목 없음."),
    ("P5-F68", "Part5", "nano_banana_rerun", "위원회, 관계 중앙행정기관, 관리기관, 전문기관의 역할과 지침·지원 흐름이 명확함. 그림 코드 없음."),
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
    out = GUIDE / "batch06_final_육안검수결과.csv"
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
    out = GUIDE / "batch06_final_검수결과.csv"
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

    for row in rows:
        if row.get("batch") == "06" and row.get("code") in reasons:
            row[status_col] = "완료"
            row[first_col] = "통과"
            row[note_col] = reasons[row["code"]]

    with MANAGEMENT.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def write_contact_sheet(paths: dict[str, Path]) -> Path:
    out = GUIDE / "batch06_final_contact_sheet.png"
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
