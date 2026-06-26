from __future__ import annotations

from math import exp
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
    draw_key,
    draw_server,
    font,
    label,
    rect,
    text_center,
    text_left,
)


OUT_PART3 = ROOT / "03_수정완료" / "Part3"
OUT_PART4 = ROOT / "03_수정완료" / "Part4"


def simple_person(draw: ImageDraw.ImageDraw, x: int, y: int, color: str = TEAL, caption: str = "") -> None:
    draw.ellipse((x + 42, y, x + 98, y + 56), fill=LIGHT_BLUE, outline=NAVY, width=4)
    draw.rounded_rectangle((x + 22, y + 62, x + 118, y + 145), radius=18, fill=color, outline=NAVY, width=4)
    if caption:
        text_center(draw, (x - 20, y + 150, x + 160, y + 200), caption, font(24, True), TEXT)


def bank(draw: ImageDraw.ImageDraw, x: int, y: int, caption: str, fill: str = LIGHT_BLUE) -> None:
    draw.polygon([(x + 65, y), (x, y + 42), (x + 130, y + 42)], fill=fill, outline=NAVY)
    draw.line((x, y + 42, x + 130, y + 42), fill=NAVY, width=4)
    for cx in (x + 25, x + 55, x + 85):
        draw.rectangle((cx, y + 45, cx + 18, y + 105), fill=fill, outline=NAVY, width=3)
    draw.rectangle((x + 8, y + 105, x + 122, y + 122), fill=fill, outline=NAVY, width=3)
    text_center(draw, (x - 35, y + 130, x + 165, y + 184), caption, font(22, True), TEXT)


def render_p3_f60() -> Path:
    img = Image.new("RGB", (1800, 1004), WHITE)
    draw = ImageDraw.Draw(img)

    rect(draw, (45, 60, 570, 950), LIGHT_BLUE, MID_GRAY, width=2, radius=18)
    label(draw, (75, 90, 230, 145), "사용자", NAVY, NAVY)
    simple_person(draw, 95, 210, TEAL, "사용자")
    draw_document(draw, 300, 205, "원문 M")
    rect(draw, (280, 365, 500, 455), WHITE, TEAL, width=3, radius=12)
    text_center(draw, (280, 365, 500, 455), "M' = Blind(M, r)", font(22, True), TEAL_DARK)
    arrow(draw, (235, 270), (292, 250), BLUE, 5)
    arrow(draw, (390, 300), (390, 362), TEAL, 5)
    text_center(draw, (255, 145, 520, 190), "1. 화폐정보 생성\n2. 은닉값 계산", font(24, True), TEXT)

    simple_person(draw, 95, 650, TEAL, "사용자")
    rect(draw, (260, 645, 510, 730), WHITE, BLUE, width=3, radius=12)
    text_center(draw, (260, 645, 510, 730), "S = Unblind(S', r)", font(21, True), NAVY)
    text_center(draw, (250, 765, 525, 825), "6. 은닉 해제\n7. 은행 공개키로 검증", font(24, True), TEXT)

    rect(draw, (640, 70, 1180, 470), WHITE, NAVY, width=4, radius=18)
    label(draw, (820, 100, 1000, 155), "은행", BLUE, BLUE)
    bank(draw, 820, 220, "Blind Signature", LIGHT_BLUE)
    draw_key(draw, 1020, 210)
    arrow(draw, (510, 410), (635, 270), TEAL, 6)
    text_center(draw, (570, 210, 760, 285), "3. 은닉 서명 요청\nM'", font(23, True), TEXT)
    rect(draw, (985, 320, 1138, 390), LIGHT_TEAL, TEAL, width=3, radius=12)
    text_center(draw, (985, 320, 1138, 390), "S' = Sign(M',\n은행 개인키)", font(18, True), TEAL_DARK)
    arrow(draw, (830, 380), (510, 685), TEAL, 6)
    text_center(draw, (555, 505, 850, 565), "5. 서명된 은닉값 반환 S'", font(24, True), TEXT)

    rect(draw, (640, 545, 1180, 950), WHITE, NAVY, width=4, radius=18)
    label(draw, (785, 575, 1030, 630), "가맹점 결제", TEAL, TEAL)
    bank(draw, 720, 700, "가맹점", LIGHT_TEAL)
    rect(draw, (920, 705, 1135, 790), WHITE, BLUE, width=3, radius=12)
    text_center(draw, (920, 705, 1135, 790), "전자화폐\n(M, S)", font(22, True), TEXT)
    arrow(draw, (510, 690), (715, 748), TEAL, 6)
    text_center(draw, (720, 635, 1140, 690), "8. 정상 지불 요청", font(25, True), TEXT)

    rect(draw, (1240, 80, 1745, 950), GRAY, MID_GRAY, width=2, radius=18)
    label(draw, (1280, 110, 1530, 165), "발행기관 / DB", NAVY, NAVY)
    bank(draw, 1325, 230, "발행기관", LIGHT_BLUE)
    rect(draw, (1510, 225, 1675, 330), WHITE, NAVY, width=3, radius=12)
    text_center(draw, (1510, 225, 1675, 330), "사용 여부\nDB", font(22, True), TEXT)
    arrow(draw, (1135, 748), (1285, 300), BLUE, 6)
    text_center(draw, (1225, 470, 1710, 535), "9. 화폐 일련값 조회\n재사용 여부 확인", font(25, True), TEXT)
    rect(draw, (1295, 610, 1710, 725), LIGHT_GREEN, GREEN, width=3, radius=16)
    text_center(draw, (1295, 610, 1710, 725), "정상: 미사용 화폐\n정산 및 저장", font(25, True), GREEN)
    rect(draw, (1295, 775, 1710, 890), LIGHT_RED, RED, width=3, radius=16)
    text_center(draw, (1295, 775, 1710, 890), "오류: 이중지불 감지\n정산 거부 및 경고", font(25, True), RED)

    out = OUT_PART3 / "P3-F60.png"
    OUT_PART3.mkdir(parents=True, exist_ok=True)
    img.save(out)
    return out


def render_p3_f61() -> Path:
    img = Image.new("RGB", (1800, 1004), WHITE)
    draw = ImageDraw.Draw(img)

    rect(draw, (40, 55, 560, 950), GRAY, MID_GRAY, width=2, radius=18)
    label(draw, (75, 85, 320, 140), "전자서명 검증", NAVY, NAVY)
    simple_person(draw, 80, 210, TEAL, "송신자")
    draw_document(draw, 280, 165, "문서")
    rect(draw, (280, 340, 450, 405), LIGHT_TEAL, TEAL, width=3, radius=10)
    text_center(draw, (280, 340, 450, 405), "해시", font(24, True), TEAL_DARK)
    draw_key(draw, 265, 460)
    rect(draw, (275, 540, 460, 610), WHITE, BLUE, width=3, radius=10)
    text_center(draw, (275, 540, 460, 610), "전자서명", font(23, True), NAVY)
    arrow(draw, (340, 260), (360, 335), BLUE, 5)
    arrow(draw, (360, 405), (360, 535), BLUE, 5)
    arrow(draw, (460, 575), (545, 575), BLUE, 5)
    rect(draw, (110, 730, 495, 900), LIGHT_GREEN, GREEN, width=3, radius=16)
    text_left(draw, (145, 760, 465, 875), "무결성 확인\n서명자 신원 확인\n부인방지 근거 제공\n문서 전체 암호화는 아님", font(23, True), GREEN)

    rect(draw, (610, 55, 1188, 950), WHITE, NAVY, width=4, radius=18)
    label(draw, (645, 85, 980, 140), "인증서 경로·폐기 검증", BLUE, BLUE)
    certs = [("서명자 인증서", 690, 195), ("중간 CA", 840, 305), ("루트 CA", 990, 195)]
    for caption, x, y in certs:
        draw_document(draw, x, y, caption)
    arrow(draw, (810, 245), (850, 330), BLUE, 5)
    arrow(draw, (960, 330), (1000, 245), BLUE, 5)
    rect(draw, (720, 475, 1075, 575), LIGHT_BLUE, BLUE, width=3, radius=14)
    text_center(draw, (720, 475, 1075, 575), "공개키와 신원 결속\n인증서 체인 검증", font(24, True), NAVY)
    draw_document(draw, 740, 665, "CRL")
    draw_document(draw, 930, 665, "OCSP")
    arrow(draw, (895, 575), (805, 660), TEAL, 5)
    arrow(draw, (905, 575), (995, 660), TEAL, 5)
    rect(draw, (720, 810, 1075, 900), LIGHT_RED, RED, width=3, radius=14)
    text_center(draw, (720, 810, 1075, 900), "폐기·만료·체인 단절 시\n검증 실패", font(24, True), RED)

    rect(draw, (1240, 55, 1760, 950), GRAY, MID_GRAY, width=2, radius=18)
    label(draw, (1275, 85, 1550, 140), "TSA 시점확인", TEAL, TEAL)
    draw_document(draw, 1300, 220, "데이터\n/서명 해시")
    bank(draw, 1485, 210, "TSA", LIGHT_BLUE)
    draw_key(draw, 1515, 450)
    rect(draw, (1310, 600, 1690, 705), WHITE, NAVY, width=3, radius=14)
    text_center(draw, (1310, 600, 1690, 705), "Timestamp Token\n= 해시 + 신뢰시각 + TSA 서명", font(22, True), TEXT)
    arrow(draw, (1425, 270), (1480, 270), BLUE, 5)
    arrow(draw, (1550, 375), (1500, 595), TEAL, 5)
    rect(draw, (1285, 770, 1500, 890), LIGHT_GREEN, GREEN, width=3, radius=14)
    text_center(draw, (1285, 770, 1500, 890), "존재 시각 증명\n서명 후\n변조 방지", font(21, True), GREEN)
    simple_person(draw, 1535, 740, TEAL, "수신자")
    arrow(draw, (1500, 705), (1602, 744), BLUE, 5)

    out = OUT_PART3 / "P3-F61.png"
    OUT_PART3.mkdir(parents=True, exist_ok=True)
    img.save(out)
    return out


def render_p4_f11() -> Path:
    img = Image.new("RGB", (1600, 893), WHITE)
    draw = ImageDraw.Draw(img)

    ox, oy = 350, 660
    w, h = 820, 460
    draw.line((ox, oy, ox, oy - h), fill="#777777", width=5)
    draw.line((ox, oy, ox + w, oy), fill="#777777", width=5)
    draw.polygon([(ox, oy - h - 18), (ox - 14, oy - h + 12), (ox + 14, oy - h + 12)], fill="#777777")
    draw.polygon([(ox + w + 18, oy), (ox + w - 12, oy - 14), (ox + w - 12, oy + 14)], fill="#777777")
    text_center(draw, (250, 380, 340, 460), "오류율", font(28, True), TEXT)
    text_center(draw, (600, 690, 900, 745), "판정 임계값", font(28, True), TEXT)
    text_center(draw, (950, 690, 1250, 745), "엄격해짐 →", font(28, True), TEXT)

    far_pts = []
    frr_pts = []
    for i in range(0, 701):
        t = i / 700
        q = 1 / (1 + exp(-8 * (t - 0.5)))
        x = ox + 60 + int(t * 650)
        far_y = oy - 55 - int((1 - q) * 330)
        frr_y = oy - 55 - int(q * 330)
        far_pts.append((x, far_y))
        frr_pts.append((x, frr_y))
    draw.line(far_pts, fill="#287AA0", width=7)
    draw.line(frr_pts, fill="#C33135", width=7)

    ex = ox + 60 + 325
    ey = oy - 55 - 165
    draw.line((ex, oy, ex, oy - h + 15), fill="#999999", width=2)
    draw.line((ox, ey, ex, ey), fill="#999999", width=2)
    draw.ellipse((ex - 18, ey - 18, ex + 18, ey + 18), fill=WHITE, outline=TEAL_DARK, width=7)
    rect(draw, (510, 195, 760, 245), LIGHT_BLUE, "#B7DDE8", width=1, radius=10)
    text_center(draw, (510, 195, 760, 245), "FAR : 오인수락률", font(24, True), "#287AA0")
    rect(draw, (1080, 235, 1335, 285), "#F9DCDD", "#E9B7BA", width=1, radius=10)
    text_center(draw, (1080, 235, 1335, 285), "FRR : 오인거부율", font(24, True), "#C33135")
    rect(draw, (1080, 545, 1335, 595), LIGHT_BLUE, "#B7DDE8", width=1, radius=10)
    text_center(draw, (1080, 545, 1335, 595), "FAR : 오인수락률", font(24, True), "#287AA0")
    text_left(draw, (790, 385, 1225, 475), "EER : FAR와 FRR이\n같아지는 지점", font(28, True), TEXT)
    text_center(draw, (255, 750, 795, 830), "임계값을 엄격하게 할수록\nFAR 감소, FRR 증가", font(25, True), TEXT)
    text_center(draw, (910, 750, 1360, 830), "EER이 낮을수록\n분리 성능이 우수", font(25, True), TEXT)

    out = OUT_PART4 / "P4-F11.png"
    OUT_PART4.mkdir(parents=True, exist_ok=True)
    img.save(out)
    return out


def render_p4_f24() -> Path:
    img = Image.new("RGB", (1600, 893), WHITE)
    draw = ImageDraw.Draw(img)

    rect(draw, (45, 290, 280, 410), "#6B7280", "#6B7280", width=2, radius=12)
    text_center(draw, (45, 290, 280, 410), "UDI\n검증되지 않은 입력", font(23, True), WHITE)
    simple_person(draw, 75, 115, LIGHT_BLUE, "사용자")
    arrow(draw, (170, 280), (170, 235), BLUE, 5)

    rect(draw, (355, 135, 605, 235), NAVY, NAVY, width=3, radius=14)
    text_center(draw, (355, 135, 605, 235), "TP\n인증된 변환절차", font(25, True), WHITE)
    rect(draw, (355, 500, 605, 600), NAVY, NAVY, width=3, radius=14)
    text_center(draw, (355, 500, 605, 600), "TP\n인증된 변환절차", font(25, True), WHITE)
    arrow(draw, (280, 350), (350, 185), BLUE, 5)
    arrow(draw, (280, 350), (350, 550), BLUE, 5)

    rect(draw, (740, 120, 1020, 245), TEAL, TEAL, width=3, radius=16)
    text_center(draw, (740, 120, 1020, 245), "CDI\n무결성이 보호되는 데이터", font(25, True), WHITE)
    rect(draw, (740, 500, 1020, 625), TEAL, TEAL, width=3, radius=16)
    text_center(draw, (740, 500, 1020, 625), "IVP\n무결성 검증절차", font(25, True), WHITE)
    arrow(draw, (605, 185), (735, 185), BLUE, 5)
    arrow(draw, (605, 550), (735, 550), BLUE, 5)
    arrow(draw, (880, 500), (880, 250), TEAL, 5)
    arrow(draw, (880, 250), (880, 500), TEAL, 5)
    text_center(draw, (905, 305, 1180, 375), "CDI 상태와\nTP 적합성 점검", font(24, True), TEXT)

    draw.line((360, 300, 1020, 300), fill=RED, width=5)
    draw.line((360, 300, 360, 235), fill=RED, width=5)
    draw.line((1020, 300, 1020, 245), fill=RED, width=5)
    text_center(draw, (440, 255, 820, 315), "직접 수정 금지", font(24, True), RED)

    rect(draw, (1135, 80, 1545, 330), GRAY, NAVY, width=3, radius=18)
    label(draw, (1260, 105, 1435, 150), "직무분리", NAVY, NAVY)
    simple_person(draw, 1175, 185, LIGHT_BLUE, "TP 담당")
    simple_person(draw, 1380, 185, LIGHT_BLUE, "IVP 담당")
    arrow(draw, (1300, 235), (1370, 235), TEAL, 5)

    rect(draw, (1135, 425, 1545, 760), GRAY, NAVY, width=3, radius=18)
    label(draw, (1260, 450, 1435, 495), "감사", NAVY, NAVY)
    draw_document(draw, 1285, 555, "감사 로그")
    arrow(draw, (1020, 560), (1280, 600), TEAL, 5)
    arrow(draw, (1280, 650), (1025, 610), TEAL, 5)
    text_center(draw, (1125, 775, 1545, 835), "TP 실행 기록과 검증 결과를\n감사 로그로 남긴다.", font(23, True), TEXT)

    rect(draw, (80, 700, 1020, 840), LIGHT_GREEN, GREEN, width=3, radius=18)
    text_left(
        draw,
        (120, 728, 980, 815),
        "핵심 규칙: 사용자는 CDI를 직접 수정하지 않고, 인증된 TP만 CDI를 변경한다. IVP는 CDI의 무결성과 TP 사용 적합성을 검증한다.",
        font(24, True),
        GREEN,
    )

    out = OUT_PART4 / "P4-F24.png"
    OUT_PART4.mkdir(parents=True, exist_ok=True)
    img.save(out)
    return out


def main() -> None:
    print(render_p3_f60())
    print(render_p3_f61())
    print(render_p4_f11())
    print(render_p4_f24())


if __name__ == "__main__":
    main()
