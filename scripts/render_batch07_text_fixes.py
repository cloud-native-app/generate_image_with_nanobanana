from __future__ import annotations

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
    font,
    label,
    rect,
    text_center,
    text_left,
)


OUT_PART1 = ROOT / "03_수정완료" / "Part1"
OUT_PART5 = ROOT / "03_수정완료" / "Part5"


def pill(
    draw: ImageDraw.ImageDraw,
    xy: tuple[int, int, int, int],
    text: str,
    fill: str = LIGHT_TEAL,
    outline: str = TEAL,
    text_fill: str = TEXT,
    size: int = 24,
) -> None:
    rect(draw, xy, fill, outline, width=3, radius=14)
    text_center(draw, xy, text, font(size, True), text_fill)


def render_p5_f83() -> Path:
    img = Image.new("RGB", (1600, 893), WHITE)
    draw = ImageDraw.Draw(img)

    rect(draw, (55, 100, 420, 700), "#F8FAFC", NAVY, width=4, radius=18)
    label(draw, (85, 130, 390, 185), "처리 현황", NAVY, NAVY, font(28, True))
    for y, title, body in [
        (230, "시스템 로그", "접속·이용 기록"),
        (385, "데이터베이스", "수집 항목과 보유 데이터"),
        (540, "접근권한", "처리자와 권한 범위"),
    ]:
        pill(draw, (95, y, 380, y + 64), title, LIGHT_BLUE, BLUE, NAVY, 24)
        text_center(draw, (95, y + 70, 380, y + 110), body, font(19, True), TEXT)

    arrow(draw, (420, 400), (525, 400), BLUE, 7)

    rect(draw, (535, 70, 1205, 765), WHITE, NAVY, width=4, radius=20)
    label(draw, (565, 100, 1175, 160), "개인정보 처리방침 필수 기재 항목", NAVY, NAVY, font(27, True))
    rows = [
        ("처리 목적", "서비스 제공, 회원 관리 등"),
        ("처리 항목", "수집하는 개인정보 항목"),
        ("보유기간", "보유 및 이용 기간"),
        ("제3자 제공", "제공받는 자, 목적, 항목"),
        ("처리위탁", "수탁자와 위탁 업무"),
        ("파기", "파기 절차와 방법"),
        ("정보주체 권리", "열람·정정·삭제·처리정지"),
        ("안전성 확보조치", "접근통제, 암호화, 로그 관리"),
        ("자동수집 장치", "쿠키 등 사용과 거부 방법"),
        ("변경 이력", "개정일과 이전 버전"),
    ]
    y = 185
    for key, value in rows:
        draw.rounded_rectangle((570, y, 1170, y + 48), radius=10, fill="#F8FAFC", outline=MID_GRAY, width=2)
        draw.rectangle((570, y, 790, y + 48), fill=TEAL)
        text_center(draw, (570, y, 790, y + 48), key, font(21, True), WHITE)
        text_center(draw, (810, y, 1160, y + 48), value, font(20, True), TEXT)
        y += 54

    rect(draw, (1260, 125, 1545, 335), LIGHT_BLUE, BLUE, width=3, radius=18)
    text_center(draw, (1285, 155, 1520, 235), "실제 처리\n일치 확인", font(28, True), NAVY)
    text_center(draw, (1285, 250, 1520, 305), "현황과 방침 비교", font(21, True), TEXT)
    arrow(draw, (1205, 260), (1252, 230), BLUE, 6)

    rect(draw, (1260, 430, 1545, 665), LIGHT_TEAL, TEAL, width=3, radius=18)
    text_center(draw, (1285, 460, 1520, 530), "정책 생성·개정", font(27, True), TEAL_DARK)
    text_center(draw, (1285, 545, 1520, 630), "정책 수립\n업데이트\n이전 버전 비교", font(20, True), TEXT)
    arrow(draw, (1205, 560), (1252, 548), TEAL, 6)

    rect(draw, (160, 790, 1440, 865), LIGHT_RED, RED, width=3, radius=18)
    text_center(draw, (180, 805, 1420, 850), "처리방침은 실제 처리와 일치해야 하며, 동의를 대신하지 않는다.", font(30, True), RED)

    return _save(img, OUT_PART5, "P5-F83.png")


def event_box(
    draw: ImageDraw.ImageDraw,
    x: int,
    y: int,
    w: int,
    title: str,
    detail: str,
    severity: str,
    color: str,
) -> tuple[int, int]:
    rect(draw, (x, y, x + w, y + 78), WHITE, color, width=3, radius=12)
    text_left(draw, (x + 18, y + 13, x + w - 18, y + 44), title, font(20, True), TEXT)
    text_left(draw, (x + 18, y + 43, x + w - 70, y + 70), detail, font(16, True), TEXT)
    text_center(draw, (x + w - 66, y + 42, x + w - 10, y + 72), severity, font(16, True), color)
    return (x + w // 2, y + 78)


def render_p1_f30() -> Path:
    img = Image.new("RGB", (2048, 1210), WHITE)
    draw = ImageDraw.Draw(img)

    x0, x1 = 165, 1935
    y_top = 160
    draw.line((x0, y_top, x1, y_top), fill=TEXT, width=5)
    draw.polygon([(x1 + 25, y_top), (x1 - 10, y_top - 15), (x1 - 10, y_top + 15)], fill=TEXT)
    labels = ["로그인 실패", "로그인 성공", "권한 변경", "원격 실행", "중요 파일 접근", "외부 전송", "로그 삭제"]
    xs = [245, 520, 790, 1060, 1335, 1615, 1880]
    for x, lab in zip(xs, labels):
        draw.ellipse((x - 7, y_top - 7, x + 7, y_top + 7), fill=TEXT)
        pill(draw, (x - 100, y_top + 38, x + 100, y_top + 92), lab, "#F8FAFC", MID_GRAY, TEXT, 19)

    lanes = [("사용자", 300), ("Host A", 505), ("Host B", 710), ("네트워크", 915)]
    for name, y in lanes:
        rect(draw, (45, y - 65, 150, y + 65), GRAY, MID_GRAY, width=2, radius=10)
        text_center(draw, (45, y - 40, 150, y + 40), name, font(23, True), TEXT)
        draw.rectangle((165, y - 70, 1935, y + 70), outline="#E5E7EB", width=2)

    event_specs = [
        (175, 240, 245, "09:00:10", "jsmith / Host A\n로그인 실패", "낮음", "#6B7280"),
        (435, 240, 275, "09:00:15", "jsmith / Host A\n로그인 성공", "중간", TEAL),
        (700, 445, 275, "09:02:00", "관리자 그룹 추가", "높음", "#B7791F"),
        (965, 650, 315, "09:05:10", "Host B 원격 프로세스 실행", "높음", "#6B46C1"),
        (1240, 650, 315, "09:07:30", "중요 파일 1,240건 접근", "높음", BLUE),
        (1465, 855, 320, "09:09:00", "외부 IP로 대량 전송", "높음", TEAL_DARK),
        (1715, 445, 275, "09:10:15", "로그 삭제 시도", "치명", RED),
    ]
    events = [event_box(draw, *spec) for spec in event_specs]
    for a, b in zip(events, events[1:]):
        draw.line((a[0], a[1], b[0], b[1] - 78), fill=NAVY, width=5)
    for spec in event_specs:
        event_box(draw, *spec)
    for x, y in events:
        draw.ellipse((x - 8, y - 8, x + 8, y + 8), fill=TEXT)

    rect(draw, (180, 1010, 1260, 1162), "#F8FAFC", MID_GRAY, width=3, radius=18)
    text_center(
        draw,
        (220, 1035, 1220, 1135),
        "개별 이벤트는 약한 신호일 수 있다.\n사용자·호스트·네트워크 사건을 시간순으로 연결하면 침해 흐름이 보인다.",
        font(28, True),
        TEXT,
    )
    rect(draw, (1320, 1010, 1935, 1162), LIGHT_BLUE, BLUE, width=3, radius=18)
    text_center(draw, (1360, 1038, 1895, 1135), "상관분석 결과\n계정 침해 → 권한 상승 → 내부 이동 → 정보 유출", font(28, True), NAVY)

    return _save(img, OUT_PART1, "P1-F30.png")


def _save(img: Image.Image, out_dir: Path, name: str) -> Path:
    out_dir.mkdir(parents=True, exist_ok=True)
    out = out_dir / name
    img.save(out)
    return out


def main() -> None:
    for path in (render_p5_f83(), render_p1_f30()):
        print(path)


if __name__ == "__main__":
    main()
