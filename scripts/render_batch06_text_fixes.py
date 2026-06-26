from __future__ import annotations

from math import cos, sin, tau
from pathlib import Path

from PIL import Image, ImageDraw

from render_batch03_text_fixes import (
    BLUE,
    GRAY,
    GREEN,
    LIGHT_BLUE,
    LIGHT_GREEN,
    LIGHT_RED,
    LIGHT_TEAL,
    MID_GRAY,
    NAVY,
    RED,
    ROOT,
    TEAL,
    TEAL_DARK,
    TEXT,
    WHITE,
    arrow,
    draw_document,
    font,
    label,
    rect,
    text_center,
    text_left,
)


OUT_PART5 = ROOT / "03_수정완료" / "Part5"


def pill(
    draw: ImageDraw.ImageDraw,
    xy: tuple[int, int, int, int],
    text: str,
    fill: str = LIGHT_TEAL,
    outline: str = TEAL,
    text_fill: str = TEXT,
    size: int = 24,
    bold: bool = True,
) -> None:
    rect(draw, xy, fill, outline, width=3, radius=14)
    text_center(draw, xy, text, font(size, bold), text_fill)


def simple_icon(draw: ImageDraw.ImageDraw, cx: int, cy: int, kind: str, color: str = TEAL) -> None:
    draw.ellipse((cx - 44, cy - 44, cx + 44, cy + 44), fill=WHITE, outline=color, width=6)
    if kind == "scale":
        draw.line((cx, cy - 24, cx, cy + 28), fill=NAVY, width=5)
        draw.line((cx - 28, cy - 10, cx + 28, cy - 10), fill=NAVY, width=5)
        draw.arc((cx - 36, cy - 18, cx - 4, cy + 30), 0, 180, fill=color, width=4)
        draw.arc((cx + 4, cy - 18, cx + 36, cy + 30), 0, 180, fill=color, width=4)
    elif kind == "shield":
        draw.polygon([(cx, cy - 30), (cx + 30, cy - 15), (cx + 22, cy + 28), (cx, cy + 42), (cx - 22, cy + 28), (cx - 30, cy - 15)], fill=LIGHT_TEAL, outline=NAVY)
        draw.line((cx - 14, cy + 4, cx - 2, cy + 18, cx + 18, cy - 14), fill=GREEN, width=5)
    elif kind == "lock":
        draw.rounded_rectangle((cx - 24, cy - 3, cx + 24, cy + 30), radius=8, fill=LIGHT_TEAL, outline=NAVY, width=4)
        draw.arc((cx - 20, cy - 30, cx + 20, cy + 12), 180, 360, fill=NAVY, width=5)
    elif kind == "idea":
        draw.ellipse((cx - 20, cy - 32, cx + 20, cy + 8), fill="#FFF2A8", outline=NAVY, width=4)
        draw.rectangle((cx - 12, cy + 8, cx + 12, cy + 30), fill=LIGHT_BLUE, outline=NAVY, width=3)
    elif kind == "person":
        draw.ellipse((cx - 16, cy - 28, cx + 16, cy + 4), fill=LIGHT_BLUE, outline=NAVY, width=4)
        draw.rounded_rectangle((cx - 30, cy + 6, cx + 30, cy + 38), radius=12, fill=LIGHT_TEAL, outline=NAVY, width=4)
    else:
        draw.ellipse((cx - 20, cy - 20, cx + 20, cy + 20), fill=LIGHT_TEAL, outline=NAVY, width=4)


def render_p5_f54() -> Path:
    img = Image.new("RGB", (1600, 893), WHITE)
    draw = ImageDraw.Draw(img)

    center_box = (590, 292, 1010, 570)
    rect(draw, center_box, "#EEF6F8", NAVY, width=6, radius=22)
    simple_icon(draw, 800, 370, "person", TEAL)
    text_center(draw, (620, 430, 980, 535), "디지털 시민의\n판단", font(36, True), TEXT)

    nodes = [
        ("책임", "자신의 온라인 행동과\n그 결과에 책임을 진다.", "person", (70, 120, 455, 245), BLUE),
        ("프라이버시", "개인정보와 사생활을\n보호한다.", "lock", (70, 320, 455, 445), TEAL),
        ("안전", "자신과 타인의 온라인 안전을\n지키고 위험 행위를 피한다.", "shield", (70, 520, 455, 675), TEAL),
        ("존중", "타인의 권리와 의견을\n존중하고 예의를 지킨다.", "person", (1145, 120, 1530, 245), BLUE),
        ("공정", "기회를 평등하게 제공하고\n차별하지 않는다.", "scale", (1145, 320, 1530, 445), TEAL),
        ("지식재산", "출처를 밝히고 무단 복제와\n유포를 하지 않는다.", "idea", (1145, 520, 1530, 675), TEAL),
    ]
    for title, body, icon, xy, color in nodes:
        x1, y1, x2, y2 = xy
        start = (590, 431) if x1 < 800 else (1010, 431)
        end = (x2, (y1 + y2) // 2) if x1 < 800 else (x1, (y1 + y2) // 2)
        arrow(draw, start, end, color, 3)
        rect(draw, xy, "#F8FAFC", color, width=3, radius=16)
        simple_icon(draw, x1 + 62, (y1 + y2) // 2, icon, color)
        text_center(draw, (x1 + 125, y1 + 18, x2 - 18, y1 + 58), title, font(30, True), TEXT)
        text_center(draw, (x1 + 125, y1 + 64, x2 - 18, y2 - 12), body, font(20, True), TEXT)

    rect(draw, (70, 745, 1530, 850), LIGHT_RED, RED, width=3, radius=18)
    text_center(
        draw,
        (100, 765, 1500, 830),
        "합법이라고 항상 윤리적인 것은 아니며, 표현의 자유와 타인의 권리를 함께 고려한다.",
        font(32, True),
        RED,
    )
    return _save(img, "P5-F54.png")


def render_p5_f55() -> Path:
    img = Image.new("RGB", (1600, 893), WHITE)
    draw = ImageDraw.Draw(img)

    rect(draw, (45, 70, 405, 720), "#F8FAFC", NAVY, width=4, radius=18)
    label(draw, (75, 100, 355, 155), "게시 전 점검", NAVY, NAVY, font(28, True))
    checks = [
        ("사실 확인", "허위·과장 여부 확인"),
        ("동의·프라이버시", "타인의 사진·정보 동의"),
        ("출처·저작권", "출처 표시와 이용 허락"),
        ("보안 위험", "개인정보·위치 노출 점검"),
    ]
    y = 190
    for title, body in checks:
        pill(draw, (90, y, 360, y + 70), title, LIGHT_TEAL, TEAL, TEAL_DARK, 24)
        text_center(draw, (90, y + 75, 360, y + 112), body, font(19, True), TEXT)
        y += 125

    pill(draw, (555, 360, 730, 440), "게시", NAVY, NAVY, WHITE, 34)
    arrow(draw, (405, 400), (548, 400), BLUE, 6)
    pill(draw, (885, 360, 1115, 440), "타인 확산", LIGHT_TEAL, TEAL, TEAL_DARK, 32)
    arrow(draw, (730, 400), (878, 400), BLUE, 6)

    for text, x, y in [
        ("빠른 확산", 780, 135),
        ("검색 가능성", 920, 250),
        ("장기 잔존", 920, 585),
        ("2차 피해", 720, 610),
    ]:
        arrow(draw, (1000, 360), (x + 105, y + 58), TEAL, 4)
        pill(draw, (x, y, x + 210, y + 58), text, WHITE, MID_GRAY, TEXT, 24)
    pill(draw, (885, 360, 1115, 440), "타인 확산", LIGHT_TEAL, TEAL, TEAL_DARK, 32)

    rect(draw, (1180, 85, 1548, 720), "#F8FAFC", NAVY, width=4, radius=18)
    label(draw, (1210, 115, 1518, 170), "문제 발생 시", TEAL, TEAL, font(28, True))
    actions = [
        ("증거 보존", "화면 캡처와 기록 보관"),
        ("신고", "플랫폼·기관에 신고"),
        ("정정·삭제", "오류 정정과 삭제 요청"),
        ("피해자 보호", "추가 확산 방지"),
    ]
    y = 210
    for title, body in actions:
        pill(draw, (1220, y, 1508, y + 62), title, LIGHT_BLUE, BLUE, NAVY, 24)
        text_center(draw, (1220, y + 65, 1508, y + 103), body, font(18, True), TEXT)
        y += 118
    arrow(draw, (1115, 400), (1173, 400), BLUE, 6)

    rect(draw, (500, 720, 1120, 835), LIGHT_RED, RED, width=3, radius=18)
    text_center(draw, (525, 740, 1095, 812), "익명성은 책임을 없애지 않는다.", font(36, True), RED)
    return _save(img, "P5-F55.png")


def law_box(
    draw: ImageDraw.ImageDraw,
    xy: tuple[int, int, int, int],
    title: str,
    subtitle: str,
    body: str,
    color: str,
) -> None:
    rect(draw, xy, WHITE, color, width=4, radius=18)
    x1, y1, x2, _ = xy
    draw.rounded_rectangle((x1, y1, x2, y1 + 58), radius=18, fill=color)
    text_center(draw, (x1, y1 + 4, x2, y1 + 54), title, font(25, True), WHITE)
    text_center(draw, (x1 + 18, y1 + 72, x2 - 18, y1 + 112), subtitle, font(20, True), color)
    text_left(draw, (x1 + 24, y1 + 128, x2 - 24, y1 + 220), body, font(20, True), TEXT)


def render_p5_f64() -> Path:
    img = Image.new("RGB", (1600, 893), WHITE)
    draw = ImageDraw.Draw(img)

    rect(draw, (575, 280, 1025, 610), "#EEF6F8", MID_GRAY, width=3, radius=22)
    text_center(draw, (610, 325, 990, 415), "디지털 환경", font(38, True), TEXT)
    text_center(draw, (610, 440, 990, 540), "법률마다\n보호대상과 목적이 다름", font(31, True), TEAL_DARK)

    boxes = [
        ((55, 70, 450, 300), "정보통신망법", "망 안정성과 이용자 보호", "망 안정성 확보\n침해행위·악성프로그램 금지\n불법정보·스팸 규제", NAVY),
        ((600, 55, 1000, 275), "정보통신기반보호법", "기반시설 보호", "주요정보통신기반시설 지정\n취약점 분석·평가\n보호대책 수립", TEAL),
        ((1150, 70, 1545, 300), "전자서명법", "전자서명 신뢰", "전자서명의 효력\n인증서비스 신뢰 기반\n인증서비스 관리", NAVY),
        ((55, 585, 450, 825), "저작권법", "디지털 저작물 보호", "저작물 이용 허락\n출처 표시\n침해 구제", "#6B7280"),
        ((600, 635, 1000, 850), "개인정보 보호법", "개인정보와 정보주체 권리", "개인정보 처리와 안전조치\n정보주체 권리 보장\n목적 외 이용 제한", TEAL_DARK),
        ((1150, 585, 1545, 825), "정보보호산업법", "정보보호 산업 진흥", "정보보호 산업 기반 조성\n기술 개발 지원\n전문인력 양성", "#6B7280"),
    ]
    for xy, title, subtitle, body, color in boxes:
        law_box(draw, xy, title, subtitle, body, color)
        x1, y1, x2, y2 = xy
        arrow(draw, ((x1 + x2) // 2, y2 if y2 < 500 else y1), (800, 445), color, 4)

    rect(draw, (575, 280, 1025, 610), "#EEF6F8", MID_GRAY, width=3, radius=22)
    text_center(draw, (610, 325, 990, 415), "디지털 환경", font(38, True), TEXT)
    text_center(draw, (610, 440, 990, 540), "법률마다\n보호대상과 목적이 다름", font(31, True), TEAL_DARK)

    return _save(img, "P5-F64.png")


def _save(img: Image.Image, name: str) -> Path:
    OUT_PART5.mkdir(parents=True, exist_ok=True)
    out = OUT_PART5 / name
    img.save(out)
    return out


def main() -> None:
    for path in (render_p5_f54(), render_p5_f55(), render_p5_f64()):
        print(path)


if __name__ == "__main__":
    main()
