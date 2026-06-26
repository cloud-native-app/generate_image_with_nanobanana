from __future__ import annotations

from PIL import Image, ImageDraw, ImageFont

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
    draw_key,
    font,
    label,
    rect,
    text_center,
    text_left,
)


OUT_PART4 = ROOT / "03_수정완료" / "Part4"
SYMBOL_FONT = r"C:\Windows\Fonts\seguisym.ttf"


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


def xor(draw: ImageDraw.ImageDraw, cx: int, cy: int, r: int = 22) -> None:
    draw.ellipse((cx - r, cy - r, cx + r, cy + r), outline=NAVY, width=4, fill=WHITE)
    draw.line((cx - r + 6, cy, cx + r - 6, cy), fill=NAVY, width=3)
    draw.line((cx, cy - r + 6, cx, cy + r - 6), fill=NAVY, width=3)


def center_text_raw(
    draw: ImageDraw.ImageDraw,
    xy: tuple[int, int, int, int],
    text: str,
    fnt: ImageFont.FreeTypeFont,
    fill: str = TEXT,
) -> None:
    x1, y1, x2, y2 = xy
    bbox = draw.textbbox((0, 0), text, font=fnt)
    tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
    draw.text((x1 + (x2 - x1 - tw) / 2, y1 + (y2 - y1 - th) / 2), text, font=fnt, fill=fill)


def render_p4_f53() -> Path:
    img = Image.new("RGB", (1600, 893), WHITE)
    draw = ImageDraw.Draw(img)

    # Functional comparison panels only; no whole-image title.
    rect(draw, (45, 42, 775, 710), "#F8FAFC", MID_GRAY, width=2, radius=18)
    label(draw, (70, 68, 350, 120), "Feistel 구조", NAVY, NAVY, font(28, True))
    pill(draw, (445, 68, 725, 120), "대표 예: DES", LIGHT_BLUE, BLUE, NAVY, 24)

    for y, title, left_label, right_label in [
        (155, "Round i", "L_i", "R_i"),
        (360, "Round i+1", "L_{i+1}", "R_{i+1}"),
    ]:
        pill(draw, (75, y, 205, y + 72), title, NAVY, NAVY, WHITE, 23)
        pill(draw, (250, y, 390, y + 50), left_label, LIGHT_BLUE, BLUE, NAVY, 23)
        pill(draw, (545, y, 685, y + 50), right_label, LIGHT_TEAL, TEAL, TEAL_DARK, 23)
        pill(draw, (445, y + 100, 585, y + 155), "F 함수", NAVY, NAVY, WHITE, 22)
        xor(draw, 330, y + 128)
        arrow(draw, (612, y + 50), (516, y + 96), TEAL, 5)
        arrow(draw, (445, y + 128), (356, y + 128), TEAL, 5)
        draw.line((615, y + 128, 707, y + 128), fill=RED, width=4)
        draw.polygon([(707, y + 128), (690, y + 118), (690, y + 138)], fill=RED)
        text_center(draw, (705, y + 105, 755, y + 150), "K_i", font(22, True), RED)

    arrow(draw, (320, 205), (620, 360), BLUE, 5)
    arrow(draw, (615, 205), (320, 360), BLUE, 5)
    arrow(draw, (320, 410), (620, 585), BLUE, 5)
    arrow(draw, (615, 410), (320, 585), BLUE, 5)
    pill(draw, (245, 580, 395, 635), "R_i", LIGHT_BLUE, BLUE, NAVY, 23)
    pill(draw, (520, 580, 710, 635), "L_i XOR F", LIGHT_TEAL, TEAL, TEAL_DARK, 22)
    pill(draw, (300, 655, 525, 698), "Swap", GRAY, MID_GRAY, TEXT, 22)

    rect(draw, (70, 735, 775, 850), LIGHT_GREEN, GREEN, width=3, radius=16)
    text_left(
        draw,
        (100, 760, 740, 825),
        "복호화: 같은 라운드 구조를 사용하고 라운드 키 순서만 반대로 적용한다.",
        font(27, True),
        GREEN,
    )

    rect(draw, (825, 42, 1555, 710), "#F8FAFC", MID_GRAY, width=2, radius=18)
    label(draw, (850, 68, 305 + 850, 120), "SPN 구조", NAVY, NAVY, font(28, True))
    pill(draw, (1225, 68, 1505, 120), "대표 예: AES", LIGHT_BLUE, BLUE, NAVY, 24)

    x_mid = 1190
    for y, round_name in [(150, "Round i"), (395, "Round i+1")]:
        pill(draw, (855, y, 990, y + 72), round_name, NAVY, NAVY, WHITE, 23)
        pill(draw, (1045, y, 1225, y + 48), "AddRoundKey", LIGHT_BLUE, BLUE, NAVY, 21)
        xor(draw, x_mid, y + 74, 18)
        pill(draw, (1065, y + 104, 1395, y + 152), "Substitution (S-box)", LIGHT_TEAL, TEAL, TEAL_DARK, 21)
        pill(draw, (1065, y + 164, 1395, y + 212), "Permutation / Linear Layer", GRAY, MID_GRAY, TEXT, 21)
        arrow(draw, (1225, y + 24), (x_mid - 22, y + 72), BLUE, 4)
        arrow(draw, (x_mid, y + 92), (x_mid, y + 102), BLUE, 4)
        arrow(draw, (x_mid, y + 152), (x_mid, y + 162), BLUE, 4)
        draw.line((1395, y + 73, 1490, y + 73), fill=RED, width=4)
        draw.polygon([(1490, y + 73), (1473, y + 63), (1473, y + 83)], fill=RED)
        text_center(draw, (1490, y + 52, 1540, y + 95), "K_i", font(21, True), RED)
    text_center(draw, (1140, 635, 1240, 700), "...", font(38, True), NAVY)

    rect(draw, (825, 735, 1555, 850), LIGHT_RED, RED, width=3, radius=16)
    text_left(
        draw,
        (855, 760, 1520, 825),
        "복호화: AddRoundKey, S-box, 선형 계층마다 대응되는 역변환이 필요하다.",
        font(27, True),
        RED,
    )

    draw.line((800, 55, 800, 835), fill=NAVY, width=4)
    return _save(img, "P4-F53.png")


def render_p4_f65() -> Path:
    img = Image.new("RGB", (1600, 893), WHITE)
    draw = ImageDraw.Draw(img)

    panel_w = 470
    panels = [
        (55, "큰 정수 인수분해\n(IFP)", "RSA · Rabin", ["암호화", "전자서명"], BLUE),
        (565, "유한체 이산로그\n(DLP)", "DH · ElGamal · DSA", ["DH: 키 합의", "ElGamal: 암호화/서명", "DSA: 전자서명"], TEAL),
        (1075, "타원곡선 이산로그\n(ECDLP)", "ECDH · ECDSA", ["ECDH: 키 합의", "ECDSA: 전자서명"], TEAL_DARK),
    ]

    for x, problem, family, uses, color in panels:
        label(draw, (x + 75, 45, x + panel_w - 75, 100), "대표 수학적 난제", NAVY, NAVY, font(22, True))
        rect(draw, (x + 35, 112, x + panel_w - 35, 220), WHITE, NAVY, width=3, radius=14)
        text_center(draw, (x + 35, 112, x + panel_w - 35, 220), problem, font(29, True), TEXT)
        arrow(draw, (x + panel_w // 2, 220), (x + panel_w // 2, 270), color, 6)
        rect(draw, (x, 270, x + panel_w, 610), "#F8FAFC", color, width=4, radius=18)
        draw.rounded_rectangle((x, 270, x + panel_w, 340), radius=18, fill=color)
        text_center(draw, (x, 275, x + panel_w, 335), family, font(31, True), WHITE)
        y = 365
        for use in uses:
            pill(draw, (x + 38, y, x + panel_w - 38, y + 72), use, LIGHT_TEAL if color != BLUE else LIGHT_BLUE, color, TEXT, 24)
            y += 88
        if x == 55:
            draw_key(draw, x + 285, 475)
        elif x == 565:
            draw_key(draw, x + 310, 395)
        else:
            draw_key(draw, x + 280, 395)

    rect(draw, (55, 660, 630, 840), LIGHT_BLUE, BLUE, width=3, radius=16)
    text_center(draw, (80, 680, 610, 720), "키 크기 비교", font(30, True), NAVY)
    table = [(90, 735, "RSA 2048", "ECC 224", "약 112비트"), (90, 792, "RSA 3072", "ECC 256", "약 128비트")]
    approx_font = ImageFont.truetype(SYMBOL_FONT, 29)
    for x, y, rsa, ecc, note in table:
        pill(draw, (x, y, x + 160, y + 42), rsa, WHITE, MID_GRAY, TEXT, 23)
        center_text_raw(draw, (x + 178, y, x + 218, y + 42), "≈", approx_font, TEXT)
        pill(draw, (x + 232, y, x + 392, y + 42), ecc, WHITE, MID_GRAY, TEXT, 23)
        text_center(draw, (x + 410, y, x + 555, y + 42), f"({note})", font(20, True), TEXT)

    rect(draw, (675, 668, 1055, 832), LIGHT_GREEN, GREEN, width=3, radius=16)
    text_center(draw, (700, 695, 1030, 805), "동일 보안강도에서는\nECC 키가 더 짧다", font(31, True), GREEN)

    rect(draw, (1110, 650, 1535, 845), LIGHT_RED, RED, width=3, radius=16)
    text_center(draw, (1140, 675, 1505, 720), "양자 알고리즘 위험", font(31, True), RED)
    text_left(
        draw,
        (1145, 735, 1495, 820),
        "Shor 알고리즘은 IFP, DLP, ECDLP를 모두 약화시킬 수 있다.",
        font(25, True),
        RED,
    )

    return _save(img, "P4-F65.png")


def render_p4_f74() -> Path:
    img = Image.new("RGB", (1600, 893), WHITE)
    draw = ImageDraw.Draw(img)

    # Password KDF side.
    rect(draw, (35, 40, 760, 690), "#F8FAFC", MID_GRAY, width=2, radius=18)
    label(draw, (65, 70, 345, 125), "Password KDF", NAVY, NAVY, font(27, True))
    pill(draw, (75, 215, 295, 315), "저엔트로피 입력\n비밀번호", LIGHT_BLUE, BLUE, NAVY, 24)
    pill(draw, (75, 405, 295, 535), "Salt\n비공개 아님\n랜덤 값", WHITE, BLUE, TEXT, 22)
    pill(draw, (75, 570, 295, 650), "Pepper\nKMS/HSM 보관", LIGHT_GREEN, GREEN, GREEN, 22)
    pill(draw, (405, 230, 705, 350), "PBKDF2 · scrypt · Argon2\n느리게 계산", NAVY, NAVY, WHITE, 25)
    draw_key(draw, 505, 390)
    pill(draw, (430, 505, 690, 590), "검증자 저장\n해시/파라미터", LIGHT_TEAL, TEAL, TEAL_DARK, 24)
    arrow(draw, (295, 265), (400, 285), BLUE, 6)
    arrow(draw, (295, 470), (400, 310), TEAL, 6)
    arrow(draw, (295, 610), (430, 540), GREEN, 5)
    arrow(draw, (555, 350), (555, 500), TEAL, 6)
    rect(draw, (70, 705, 760, 840), LIGHT_GREEN, GREEN, width=3, radius=16)
    text_left(
        draw,
        (100, 735, 725, 815),
        "목적: 낮은 엔트로피의 비밀번호를 오프라인 대입 공격에 더 강하게 만든다.",
        font(26, True),
        GREEN,
    )

    # HKDF / key separation side.
    rect(draw, (825, 40, 1565, 690), LIGHT_TEAL, TEAL, width=3, radius=18)
    label(draw, (855, 70, 1180, 125), "HKDF 키 분리", NAVY, NAVY, font(27, True))
    pill(draw, (865, 190, 1125, 275), "고엔트로피\n입력키 재료", WHITE, TEAL, TEXT, 24)
    pill(draw, (865, 330, 1125, 405), "Extract\nPRK 생성", LIGHT_BLUE, BLUE, NAVY, 24)
    pill(draw, (865, 475, 1125, 550), "Expand\ninfo / label / context", LIGHT_BLUE, BLUE, NAVY, 22)
    arrow(draw, (995, 275), (995, 325), TEAL, 6)
    arrow(draw, (995, 405), (995, 470), TEAL, 6)

    keys = [
        ("enc_key", "데이터\n암호화", 1200, 175),
        ("mac_key", "메시지\n인증", 1200, 295),
        ("exporter_key", "외부\n애플리케이션", 1200, 415),
        ("iv_key / nonce", "초기화\n벡터", 1200, 535),
    ]
    for name, use, x, y in keys:
        pill(draw, (x, y, x + 190, y + 58), name, WHITE, TEAL_DARK, TEAL_DARK, 22)
        arrow(draw, (1125, 512), (x - 5, y + 30), TEAL, 5)
        arrow(draw, (x + 190, y + 30), (1430, y + 30), BLUE, 5)
        text_center(draw, (1440, y - 2, 1550, y + 60), use, font(21, True), TEXT)

    draw.line((1125, 602, 1540, 602), fill=RED, width=4)
    text_center(draw, (1140, 612, 1530, 660), "동일 키 재사용 금지", font(26, True), RED)
    rect(draw, (830, 705, 1565, 840), LIGHT_RED, RED, width=3, radius=16)
    text_left(
        draw,
        (860, 730, 1530, 815),
        "잘못된 예: 원시 키 하나를 암호화 키, MAC 키, IV 키로 함께 사용하면 키 분리가 아니다.",
        font(26, True),
        RED,
    )

    return _save(img, "P4-F74.png")


def _save(img: Image.Image, name: str) -> Path:
    OUT_PART4.mkdir(parents=True, exist_ok=True)
    out = OUT_PART4 / name
    img.save(out)
    return out


def main() -> None:
    for path in (render_p4_f53(), render_p4_f65(), render_p4_f74()):
        print(path)


if __name__ == "__main__":
    main()
