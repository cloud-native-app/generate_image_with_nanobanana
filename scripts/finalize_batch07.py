from __future__ import annotations

import csv
from pathlib import Path

from PIL import Image, ImageDraw

from render_batch03_text_fixes import ROOT, font, text_center


GUIDE = ROOT / "00_가이드"
COMPLETE = ROOT / "03_수정완료"
REWORK = ROOT / "04_재작업"
MANAGEMENT = GUIDE / "나노바나나_작업관리표_v2.csv"

BATCH = "07-final"

ITEMS = [
    ("P5-F73", "Part5", "nano_banana_rerun", "전자서명법 개정 전후, 전자서명인증사업자, 평가·인정, 동등한 법적 효력과 과거/현행 용어 구분이 명확함."),
    ("P5-F74", "Part5", "nano_banana", "개인정보보호법 처리 원칙, 생명주기, 정보주체 권리, 처리자 의무와 침해 대응 흐름이 명확함."),
    ("P5-F77", "Part5", "nano_banana", "개인정보 처리 단계와 적법 근거, 제3자 제공, 보관·파기, 안전조치 공통 준수사항이 명확함."),
    ("P5-F83", "Part5", "local_text_fix", "개인정보 처리방침 필수 기재 항목과 실제 처리 일치 확인, 동의 대체 금지 문구가 정확함."),
    ("P1-F24", "Part1", "nano_banana_rerun", "UNIX/Linux 권한 문자열, 750 계산, 파일/디렉터리 권한 의미가 정확하고 전체 제목 없음."),
    ("P1-F30", "Part1", "local_text_fix", "사용자·Host A·Host B·네트워크 이벤트를 시간순으로 연결해 계정 침해부터 정보 유출까지 흐름이 명확함."),
    ("P2-F14", "Part2", "nano_banana", "CIDR/VLSM에서 큰 요구부터 /25, /26, /27을 배정하고 네트워크·브로드캐스트 제외 및 중첩 금지가 명확함."),
    ("P2-F18", "Part2", "nano_banana", "IPv6 NDP 기능과 Dual Stack, Tunneling, NAT64/DNS64 전환 방식이 명확함."),
    ("P2-F21", "Part2", "nano_banana", "ICMP 주요 메시지, IGMP 멀티캐스트 그룹 관리, Unicast/Broadcast/Multicast/Anycast 전송 범위가 명확함."),
    ("P2-F33", "Part2", "nano_banana", "무선 공격 유형과 PMF, WIDS/WIPS, 패치, WPA2/WPA3, 802.1X 대응 관계가 명확함."),
]


def final_path(code: str, part_dir: str) -> Path:
    return COMPLETE / part_dir / f"{code}.png"


def read_expected_sizes() -> dict[str, tuple[int, int]]:
    with MANAGEMENT.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        return {
            row["code"]: (int(row["source_width"]), int(row["source_height"]))
            for row in reader
            if row.get("batch") == "07"
        }


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
    out = GUIDE / "batch07_final_육안검수결과.csv"
    with out.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["batch", "code", "visual_status", "reason", "current_location"])
        writer.writeheader()
        for code, _, _, reason in ITEMS:
            writer.writerow({"batch": BATCH, "code": code, "visual_status": "통과", "reason": reason, "current_location": str(paths[code])})
    return out


def write_dimension_csv(paths: dict[str, Path], expected: dict[str, tuple[int, int]]) -> Path:
    out = GUIDE / "batch07_final_검수결과.csv"
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
        for code, _, source, _ in ITEMS:
            path = paths[code]
            with Image.open(path) as img:
                width, height = img.size
            exp_w, exp_h = expected[code]
            writer.writerow(
                {
                    "batch": BATCH,
                    "code": code,
                    "expected_width": exp_w,
                    "expected_height": exp_h,
                    "actual_width": width,
                    "actual_height": height,
                    "dimension_ok": str((width, height) == (exp_w, exp_h)),
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
        if row.get("batch") == "07" and row.get("code") in reasons:
            row[status_col] = "완료"
            row[first_col] = "통과"
            row[note_col] = reasons[row["code"]]

    with MANAGEMENT.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def write_contact_sheet(paths: dict[str, Path]) -> Path:
    out = GUIDE / "batch07_final_contact_sheet.png"
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

    expected = read_expected_sizes()
    removed = remove_stale_rework()
    visual_csv = write_visual_csv(paths)
    dimension_csv = write_dimension_csv(paths, expected)
    update_management()
    contact_sheet = write_contact_sheet(paths)

    print(f"removed_rework={len(removed)}")
    print(visual_csv)
    print(dimension_csv)
    print(contact_sheet)


if __name__ == "__main__":
    main()
