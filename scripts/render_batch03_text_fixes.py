from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(r"C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2")
OUT_DIR = ROOT / "03_수정완료" / "Part3"
FONT = Path(r"C:\Windows\Fonts\malgun.ttf")
BOLD = Path(r"C:\Windows\Fonts\malgunbd.ttf")

NAVY = "#17395A"
BLUE = "#24508A"
TEAL = "#07889B"
TEAL_DARK = "#056B7A"
LIGHT_TEAL = "#E6F6F7"
LIGHT_BLUE = "#EEF4FA"
GRAY = "#F4F6F8"
MID_GRAY = "#D9E1E8"
GREEN = "#1F8A5B"
LIGHT_GREEN = "#EAF7EF"
RED = "#C23834"
LIGHT_RED = "#FCECEC"
TEXT = "#102A43"
WHITE = "#FFFFFF"


def font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(str(BOLD if bold else FONT), size=size)


def wrap(draw: ImageDraw.ImageDraw, text: str, fnt: ImageFont.FreeTypeFont, max_width: int) -> str:
    lines: list[str] = []
    for raw in text.split("\n"):
        current = ""
        for token in raw.split(" "):
            candidate = token if not current else current + " " + token
            if draw.textbbox((0, 0), candidate, font=fnt)[2] <= max_width:
                current = candidate
            else:
                if current:
                    lines.append(current)
                current = token
        if current:
            lines.append(current)
    return "\n".join(lines)


def text_center(
    draw: ImageDraw.ImageDraw,
    xy: tuple[int, int, int, int],
    text: str,
    fnt: ImageFont.FreeTypeFont,
    fill: str = TEXT,
    spacing: int = 6,
) -> None:
    x1, y1, x2, y2 = xy
    text = wrap(draw, text, fnt, x2 - x1 - 20)
    box = draw.multiline_textbbox((0, 0), text, font=fnt, spacing=spacing)
    tw, th = box[2] - box[0], box[3] - box[1]
    draw.multiline_text(
        (x1 + (x2 - x1 - tw) / 2, y1 + (y2 - y1 - th) / 2),
        text,
        font=fnt,
        fill=fill,
        align="center",
        spacing=spacing,
    )


def text_left(
    draw: ImageDraw.ImageDraw,
    xy: tuple[int, int, int, int],
    text: str,
    fnt: ImageFont.FreeTypeFont,
    fill: str = TEXT,
    spacing: int = 7,
) -> None:
    x1, y1, x2, _ = xy
    draw.multiline_text((x1, y1), wrap(draw, text, fnt, x2 - x1), font=fnt, fill=fill, spacing=spacing)


def rect(
    draw: ImageDraw.ImageDraw,
    xy: tuple[int, int, int, int],
    fill: str,
    outline: str = BLUE,
    width: int = 3,
    radius: int = 16,
) -> None:
    draw.rounded_rectangle(xy, radius=radius, fill=fill, outline=outline, width=width)


def label(
    draw: ImageDraw.ImageDraw,
    xy: tuple[int, int, int, int],
    text: str,
    fill: str = NAVY,
    outline: str = NAVY,
    fnt: ImageFont.FreeTypeFont | None = None,
) -> None:
    rect(draw, xy, fill, outline, width=2, radius=10)
    text_center(draw, xy, text, fnt or font(22, True), WHITE)


def arrow(draw: ImageDraw.ImageDraw, start: tuple[int, int], end: tuple[int, int], fill: str = TEAL, width: int = 5) -> None:
    draw.line([start, end], fill=fill, width=width)
    x1, y1 = start
    x2, y2 = end
    if abs(y2 - y1) > abs(x2 - x1):
        sign = -1 if y2 > y1 else 1
        pts = [(x2, y2), (x2 - 12, y2 + 14 * sign), (x2 + 12, y2 + 14 * sign)]
    else:
        sign = -1 if x2 > x1 else 1
        pts = [(x2, y2), (x2 + 14 * sign, y2 - 12), (x2 + 14 * sign, y2 + 12)]
    draw.polygon(pts, fill=fill)


def draw_server(draw: ImageDraw.ImageDraw, x: int, y: int, label_text: str) -> None:
    rect(draw, (x, y, x + 92, y + 128), "#F8FAFC", NAVY, width=3, radius=10)
    for yy in (y + 28, y + 55, y + 82):
        draw.rounded_rectangle((x + 18, yy, x + 74, yy + 10), radius=5, fill=BLUE)
    draw.ellipse((x + 38, y + 102, x + 54, y + 118), fill=TEAL)
    text_center(draw, (x - 40, y + 132, x + 132, y + 170), label_text, font(19, True), TEXT)


def draw_key(draw: ImageDraw.ImageDraw, x: int, y: int, scale: int = 1, fill: str = TEAL) -> None:
    r = 14 * scale
    draw.ellipse((x, y, x + 2 * r, y + 2 * r), outline=NAVY, width=3, fill=LIGHT_TEAL)
    draw.ellipse((x + 7 * scale, y + 7 * scale, x + 13 * scale, y + 13 * scale), fill=NAVY)
    draw.line((x + 2 * r, y + r, x + 65 * scale, y + r), fill=fill, width=7 * scale)
    draw.rectangle((x + 46 * scale, y + r, x + 55 * scale, y + r + 18 * scale), fill=fill)
    draw.rectangle((x + 58 * scale, y + r, x + 67 * scale, y + r + 12 * scale), fill=fill)


def draw_document(draw: ImageDraw.ImageDraw, x: int, y: int, title: str, fill: str = WHITE) -> None:
    rect(draw, (x, y, x + 125, y + 94), fill, NAVY, width=3, radius=8)
    for yy in (y + 26, y + 44, y + 62):
        draw.line((x + 22, yy, x + 95, yy), fill=BLUE, width=4)
    text_center(draw, (x - 10, y + 98, x + 135, y + 140), title, font(18, True), TEXT)


def render_p3_f54() -> Path:
    img = Image.new("RGB", (1800, 1004), WHITE)
    draw = ImageDraw.Draw(img)

    # Functional panels only: no whole-image title.
    rect(draw, (45, 50, 620, 255), GRAY, MID_GRAY, width=2, radius=18)
    label(draw, (75, 78, 245, 125), "전송 TLS")
    draw.ellipse((90, 155, 132, 197), outline=NAVY, width=4, fill=LIGHT_BLUE)
    draw.rectangle((82, 200, 140, 225), outline=NAVY, width=4, fill=LIGHT_BLUE)
    draw_server(draw, 330, 95, "Application\nServer")
    arrow(draw, (150, 174), (318, 174), BLUE, 5)
    arrow(draw, (422, 174), (570, 174), BLUE, 5)
    text_center(draw, (175, 135, 318, 166), "HTTPS/TLS", font(20, True), NAVY)
    text_center(draw, (454, 135, 590, 166), "암호화 연결", font(20, True), NAVY)

    rect(draw, (45, 285, 620, 500), LIGHT_BLUE, MID_GRAY, width=2, radius=18)
    label(draw, (75, 315, 320, 365), "애플리케이션 계층 암호화")
    draw_server(draw, 400, 330, "DB Server")
    rect(draw, (90, 395, 260, 455), WHITE, TEAL, width=3, radius=12)
    text_center(draw, (90, 395, 260, 455), "평문 → 암호문\n앱에서 처리", font(19, True), TEXT)
    arrow(draw, (265, 424), (390, 424), TEAL, 5)

    rect(draw, (45, 530, 620, 935), GRAY, MID_GRAY, width=2, radius=18)
    label(draw, (75, 560, 315, 610), "TDE 저장장치 암호화")
    draw_server(draw, 400, 590, "DB Server")
    rect(draw, (95, 650, 330, 770), WHITE, NAVY, width=3, radius=12)
    text_left(draw, (118, 670, 310, 750), "데이터파일\n트랜잭션 로그\n백업 매체", font(20, True))
    arrow(draw, (335, 710), (392, 665), BLUE, 5)
    rect(draw, (160, 810, 520, 895), LIGHT_TEAL, TEAL, width=3, radius=14)
    text_center(draw, (160, 810, 520, 895), "저장소 탈취 시\n파일 내용 보호", font(24, True), TEAL_DARK)

    rect(draw, (675, 50, 1260, 455), WHITE, NAVY, width=4, radius=18)
    label(draw, (710, 82, 940, 132), "열/필드 암호화", TEAL, TEAL)
    rect(draw, (725, 170, 1145, 338), WHITE, MID_GRAY, width=2, radius=8)
    columns = [725, 845, 965, 1145]
    for x in columns:
        draw.line((x, 170, x, 338), fill=MID_GRAY, width=2)
    for y in (210, 252, 294, 338):
        draw.line((725, y, 1145, y), fill=MID_GRAY, width=2)
    text_center(draw, (725, 170, 845, 210), "이름", font(18, True))
    text_center(draw, (845, 170, 965, 210), "등급", font(18, True))
    text_center(draw, (965, 170, 1145, 210), "암호화 필드", font(18, True), WHITE)
    draw.rectangle((965, 170, 1145, 210), fill=TEAL)
    text_center(draw, (965, 170, 1145, 210), "암호화 필드", font(18, True), WHITE)
    sample_rows = [("사용자", "일반", "ENC(...)"), ("관리자", "제한", "ENC(...)"), ("서비스", "일반", "ENC(...)")]
    y = 210
    for name, grade, enc in sample_rows:
        text_center(draw, (725, y, 845, y + 42), name, font(17))
        text_center(draw, (845, y, 965, y + 42), grade, font(17))
        text_center(draw, (965, y, 1145, y + 42), enc, font(17, True), TEAL_DARK)
        y += 42
    draw_key(draw, 1168, 224)
    rect(draw, (735, 360, 1165, 425), LIGHT_RED, RED, width=2, radius=12)
    text_center(draw, (735, 360, 1165, 425), "암호화는 SQL Injection·권한 오남용을\n자동 차단하지 않음", font(20, True), RED)

    rect(draw, (675, 500, 1260, 935), WHITE, NAVY, width=4, radius=18)
    label(draw, (710, 530, 920, 580), "권한 분리", NAVY, NAVY)
    rect(draw, (720, 635, 930, 785), LIGHT_BLUE, BLUE, width=3, radius=14)
    text_center(draw, (720, 635, 930, 700), "데이터 접근 권한", font(22, True), NAVY)
    text_center(draw, (720, 710, 930, 775), "DBA\n업무 데이터", font(20), TEXT)
    rect(draw, (990, 635, 1200, 785), LIGHT_TEAL, TEAL, width=3, radius=14)
    text_center(draw, (990, 635, 1200, 700), "키 접근 권한", font(22, True), TEAL_DARK)
    text_center(draw, (990, 710, 1200, 775), "Security Officer\n암호키", font(20), TEXT)
    text_center(draw, (720, 830, 1195, 910), "키와 데이터 관리자를 분리하여\n복호화 권한 집중을 방지한다.", font(24, True), TEXT)

    rect(draw, (1320, 70, 1725, 935), GRAY, MID_GRAY, width=2, radius=18)
    label(draw, (1360, 105, 1685, 160), "KMS/HSM 키 라이프사이클", NAVY, NAVY)
    rect(draw, (1395, 220, 1655, 650), WHITE, NAVY, width=4, radius=18)
    stages = [
        (1525, 270, "생성"),
        (1605, 370, "배포"),
        (1565, 510, "회전"),
        (1435, 510, "폐기"),
        (1395, 370, "백업·복구"),
    ]
    for x, y, text in stages:
        draw.ellipse((x - 38, y - 38, x + 38, y + 38), fill=LIGHT_TEAL, outline=TEAL, width=4)
        text_center(draw, (x - 70, y + 48, x + 70, y + 85), text, font(18, True))
    for start, end in [((1525, 308), (1605, 332)), ((1605, 408), (1565, 472)), ((1565, 548), (1435, 548)), ((1435, 472), (1395, 408)), ((1395, 332), (1525, 308))]:
        arrow(draw, start, end, BLUE, 4)
    draw_key(draw, 1492, 360, scale=1)
    rect(draw, (1370, 720, 1688, 830), LIGHT_GREEN, GREEN, width=3, radius=14)
    text_center(draw, (1370, 720, 1688, 830), "중앙 키 관리\n감사 로그·접근통제", font(23, True), GREEN)

    out = OUT_DIR / "P3-F54.png"
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    img.save(out)
    return out


def render_p3_f59() -> Path:
    img = Image.new("RGB", (1800, 1004), WHITE)
    draw = ImageDraw.Draw(img)

    # Functional areas only: no whole-image title.
    rect(draw, (50, 60, 920, 940), GRAY, MID_GRAY, width=2, radius=18)
    text_center(draw, (90, 95, 880, 145), "고객 (Customer)", font(30, True), TEXT)
    draw_document(draw, 110, 260, "Order\nInformation\n(OI)")
    draw_document(draw, 110, 600, "Payment\nInformation\n(PI)")
    rect(draw, (310, 285, 470, 350), WHITE, BLUE, width=3, radius=10)
    text_center(draw, (310, 285, 470, 350), "OIMD\n= H(OI)", font(20, True))
    rect(draw, (310, 625, 470, 690), WHITE, BLUE, width=3, radius=10)
    text_center(draw, (310, 625, 470, 690), "PIMD\n= H(PI)", font(20, True))
    arrow(draw, (235, 307), (305, 317), BLUE, 5)
    arrow(draw, (235, 647), (305, 657), BLUE, 5)

    rect(draw, (525, 430, 735, 520), LIGHT_TEAL, TEAL, width=4, radius=14)
    text_center(draw, (525, 430, 735, 520), "POMD = H\n(PIMD || OIMD)", font(22, True), TEAL_DARK)
    arrow(draw, (475, 317), (525, 460), BLUE, 5)
    arrow(draw, (475, 657), (525, 495), BLUE, 5)

    draw_key(draw, 590, 590)
    text_center(draw, (530, 545, 760, 590), "고객 개인키", font(21, True), TEXT)
    rect(draw, (620, 710, 785, 775), WHITE, NAVY, width=3, radius=10)
    text_center(draw, (620, 710, 785, 775), "Sign", font(24, True), NAVY)
    arrow(draw, (630, 520), (695, 704), BLUE, 5)
    arrow(draw, (650, 620), (695, 704), BLUE, 5)
    rect(draw, (715, 430, 850, 535), WHITE, NAVY, width=3, radius=12)
    text_center(draw, (715, 430, 850, 535), "DS", font(25, True), NAVY)
    arrow(draw, (785, 742), (785, 542), BLUE, 5)
    text_center(draw, (355, 820, 845, 875), "DS = Sign_customer_private(POMD)", font(25, True), TEXT)

    # Shipping of OI/PIMD to merchant and PI/OIMD to payment gateway.
    arrow(draw, (850, 475), (1000, 280), BLUE, 6)
    arrow(draw, (850, 475), (1000, 690), BLUE, 6)

    rect(draw, (1000, 60, 1748, 465), GRAY, MID_GRAY, width=2, radius=18)
    text_center(draw, (1040, 95, 1708, 145), "상점 (Merchant)", font(30, True), TEXT)
    draw_document(draw, 1055, 195, "OI")
    rect(draw, (1250, 215, 1395, 275), WHITE, BLUE, width=3, radius=10)
    text_center(draw, (1250, 215, 1395, 275), "OIMD = H(OI)", font(18, True))
    rect(draw, (1055, 330, 1180, 400), WHITE, BLUE, width=3, radius=10)
    text_center(draw, (1055, 330, 1180, 400), "PIMD", font(21, True))
    rect(draw, (1265, 330, 1395, 400), WHITE, BLUE, width=3, radius=10)
    text_center(draw, (1265, 330, 1395, 400), "Verify", font(21, True))
    draw_key(draw, 1460, 235)
    text_center(draw, (1410, 190, 1640, 230), "고객 공개키", font(21, True), TEXT)
    rect(draw, (1525, 320, 1668, 410), LIGHT_GREEN, GREEN, width=4, radius=16)
    text_center(draw, (1525, 320, 1668, 410), "Dual\nSignature", font(22, True), GREEN)
    text_center(draw, (1200, 410, 1510, 450), "Verify(POMD, DS, 고객 공개키)", font(22, True), TEXT)
    arrow(draw, (1185, 230), (1245, 245), BLUE, 5)
    arrow(draw, (1185, 365), (1260, 365), BLUE, 5)
    arrow(draw, (1395, 365), (1518, 365), TEAL, 5)

    rect(draw, (1000, 535, 1748, 940), GRAY, MID_GRAY, width=2, radius=18)
    text_center(draw, (1040, 570, 1708, 620), "Payment Gateway (PG)", font(30, True), TEXT)
    draw_document(draw, 1055, 670, "PI")
    rect(draw, (1250, 690, 1395, 750), WHITE, BLUE, width=3, radius=10)
    text_center(draw, (1250, 690, 1395, 750), "PIMD = H(PI)", font(18, True))
    rect(draw, (1055, 805, 1180, 875), WHITE, BLUE, width=3, radius=10)
    text_center(draw, (1055, 805, 1180, 875), "OIMD", font(21, True))
    rect(draw, (1265, 805, 1395, 875), WHITE, BLUE, width=3, radius=10)
    text_center(draw, (1265, 805, 1395, 875), "Verify", font(21, True))
    draw_key(draw, 1460, 710)
    text_center(draw, (1410, 665, 1640, 705), "고객 공개키", font(21, True), TEXT)
    rect(draw, (1525, 795, 1668, 885), LIGHT_GREEN, GREEN, width=4, radius=16)
    text_center(draw, (1525, 795, 1668, 885), "Dual\nSignature", font(22, True), GREEN)
    text_center(draw, (1200, 885, 1510, 925), "Verify(POMD, DS, 고객 공개키)", font(22, True), TEXT)
    arrow(draw, (1185, 705), (1245, 720), BLUE, 5)
    arrow(draw, (1185, 840), (1260, 840), BLUE, 5)
    arrow(draw, (1395, 840), (1518, 840), TEAL, 5)

    out = OUT_DIR / "P3-F59.png"
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    img.save(out)
    return out


def main() -> None:
    print(render_p3_f54())
    print(render_p3_f59())


if __name__ == "__main__":
    main()
