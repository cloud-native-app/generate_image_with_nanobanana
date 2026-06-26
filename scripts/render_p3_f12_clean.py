from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(r"C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2")
OUT = ROOT / "03_수정완료" / "Part3" / "P3-F12.png"
FONT = Path(r"C:\Windows\Fonts\malgun.ttf")
BOLD = Path(r"C:\Windows\Fonts\malgunbd.ttf")

NAVY = "#183A5A"
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


def centered(draw: ImageDraw.ImageDraw, xy: tuple[int, int, int, int], text: str, fnt: ImageFont.FreeTypeFont, fill: str = TEXT) -> None:
    x1, y1, x2, y2 = xy
    text = wrap(draw, text, fnt, x2 - x1 - 22)
    box = draw.multiline_textbbox((0, 0), text, font=fnt, spacing=6)
    tw, th = box[2] - box[0], box[3] - box[1]
    draw.multiline_text((x1 + (x2 - x1 - tw) / 2, y1 + (y2 - y1 - th) / 2), text, font=fnt, fill=fill, align="center", spacing=6)


def left(draw: ImageDraw.ImageDraw, xy: tuple[int, int, int, int], text: str, fnt: ImageFont.FreeTypeFont, fill: str = TEXT) -> None:
    x1, y1, x2, _ = xy
    draw.multiline_text((x1, y1), wrap(draw, text, fnt, x2 - x1), font=fnt, fill=fill, spacing=8)


def rect(draw: ImageDraw.ImageDraw, xy: tuple[int, int, int, int], fill: str, outline: str = BLUE, width: int = 3, radius: int = 16) -> None:
    draw.rounded_rectangle(xy, radius=radius, fill=fill, outline=outline, width=width)


def arrow(draw: ImageDraw.ImageDraw, start: tuple[int, int], end: tuple[int, int], fill: str = TEAL, width: int = 5) -> None:
    draw.line([start, end], fill=fill, width=width)
    x1, y1 = start
    x2, y2 = end
    if abs(y2 - y1) > abs(x2 - x1):
        pts = [(x2, y2), (x2 - 13, y2 + (13 if y2 < y1 else -13)), (x2 + 13, y2 + (13 if y2 < y1 else -13))]
    else:
        pts = [(x2, y2), (x2 + (-13 if x2 > x1 else 13), y2 - 13), (x2 + (-13 if x2 > x1 else 13), y2 + 13)]
    draw.polygon(pts, fill=fill)


def main() -> None:
    img = Image.new("RGB", (1800, 1004), WHITE)
    draw = ImageDraw.Draw(img)

    # Functional panels only: no whole-image title and no figure code.
    rect(draw, (55, 55, 1180, 445), WHITE, NAVY, width=4, radius=20)
    centered(draw, (75, 72, 360, 125), "Received 헤더 누적", font(28, True), NAVY)
    centered(draw, (880, 72, 1160, 125), "아래 → 위로 추적", font(25, True), TEAL_DARK)
    arrow(draw, (1040, 385), (1040, 145), TEAL, 8)

    received_rows = [
        ("최신", "Received: from mx2.receiver.net by mx3.receiver.net;\nThu, 27 Oct 2023 10:18:09 +0900 (KST)"),
        ("중간", "Received: from mx1.example.com by mx2.receiver.net;\nThu, 27 Oct 2023 10:17:45 +0900 (KST)"),
        ("최초", "Received: from client.example.com by mx1.example.com;\nThu, 27 Oct 2023 10:17:05 +0900 (KST)"),
    ]
    y = 140
    for tag, text in received_rows:
        rect(draw, (95, y, 210, y + 82), LIGHT_BLUE, BLUE, width=2, radius=12)
        centered(draw, (95, y, 210, y + 82), tag, font(22, True), NAVY)
        rect(draw, (230, y, 910, y + 82), GRAY, TEAL, width=2, radius=12)
        left(draw, (252, y + 12, 890, y + 75), text, font(22), TEXT)
        y += 94

    rect(draw, (55, 485, 1180, 724), WHITE, NAVY, width=4, radius=20)
    rows = [
        ("Header From", "user@example.com", "표시용 From"),
        ("Return-Path", "bounce@example.com", "Envelope From"),
        ("Reply-To", "help@example.com", "회신 주소"),
        ("Message-ID", "<unique-id@example.com>", "메시지 식별자"),
    ]
    y = 520
    for label, value, note in rows:
        rect(draw, (95, y, 295, y + 42), NAVY, NAVY, width=2, radius=10)
        centered(draw, (95, y, 295, y + 42), label, font(20, True), WHITE)
        left(draw, (320, y + 4, 850, y + 42), value, font(24), TEXT)
        left(draw, (875, y + 6, 1130, y + 42), note, font(20), TEAL_DARK)
        y += 48

    rect(draw, (55, 760, 1180, 948), WHITE, NAVY, width=4, radius=20)
    rect(draw, (95, 790, 375, 838), NAVY, NAVY, width=2, radius=10)
    centered(draw, (95, 790, 375, 838), "Authentication-Results", font(20, True), WHITE)
    left(
        draw,
        (410, 790, 1135, 935),
        "receiver.net;\nspf=pass smtp.mailfrom=example.com;\ndkim=pass header.d=example.com;\ndmarc=pass header.from=example.com",
        font(24),
        TEXT,
    )

    rect(draw, (1230, 70, 1718, 392), LIGHT_TEAL, TEAL, width=4, radius=20)
    centered(draw, (1260, 90, 1690, 145), "검증 결과 예시", font(28, True), TEAL_DARK)
    checks = [
        "OK  spf=pass",
        "OK  dkim=pass",
        "OK  dmarc=pass",
        "OK  DMARC 근거: SPF/DKIM 정렬",
    ]
    y = 170
    for item in checks:
        left(draw, (1292, y + 2, 1695, y + 42), item, font(22, True), GREEN if item.startswith("OK") else TEXT)
        y += 52

    rect(draw, (1230, 450, 1718, 704), GRAY, MID_GRAY, width=3, radius=20)
    centered(draw, (1260, 470, 1690, 520), "구분 포인트", font(28, True), NAVY)
    points = [
        "Header From: 사용자 표시 주소",
        "Return-Path: SPF 확인 Envelope From",
        "Received: 각 MTA가 위쪽에 추가",
        "한 줄만으로 전체 경로 단정 금지",
    ]
    y = 540
    for point in points:
        left(draw, (1270, y, 1695, y + 34), "- " + point, font(19), TEXT)
        y += 42

    rect(draw, (1230, 750, 1718, 948), LIGHT_GREEN, GREEN, width=4, radius=20)
    centered(draw, (1260, 770, 1690, 835), "판정 흐름", font(28, True), GREEN)
    centered(draw, (1260, 850, 1690, 922), "SPF/DKIM 결과와 Header From 정렬을 함께 확인하여 DMARC pass 여부를 판단한다.", font(23), TEXT)

    OUT.parent.mkdir(parents=True, exist_ok=True)
    img.save(OUT)
    print(OUT)


if __name__ == "__main__":
    main()
