from __future__ import annotations

import csv
import math
from pathlib import Path
from typing import Iterable

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(r"C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2")
MANIFEST = ROOT / "00_가이드" / "나노바나나_전체_수정대상_매니페스트_v2.csv"
OUT = ROOT / "03_수정완료"
CONTACT_SHEET = ROOT / "00_가이드" / "batch01_priorityA_contact_sheet.png"

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
RED = "#C23834"
LIGHT_RED = "#FBE9E8"
GREEN = "#1F7A54"
LIGHT_GREEN = "#EAF7EF"
TEXT = "#102A43"
MUTED = "#4F6478"
WHITE = "#FFFFFF"


def font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(str(BOLD if bold else FONT), size=size)


def text_size(draw: ImageDraw.ImageDraw, text: str, fnt: ImageFont.FreeTypeFont) -> tuple[int, int]:
    if not text:
        return 0, 0
    box = draw.multiline_textbbox((0, 0), text, font=fnt, spacing=max(4, fnt.size // 5))
    return box[2] - box[0], box[3] - box[1]


def wrap_text(draw: ImageDraw.ImageDraw, text: str, fnt: ImageFont.FreeTypeFont, max_width: int) -> str:
    lines: list[str] = []
    for raw in text.split("\n"):
        if not raw:
            lines.append("")
            continue
        current = ""
        for token in raw.split(" "):
            candidate = token if not current else current + " " + token
            if text_size(draw, candidate, fnt)[0] <= max_width:
                current = candidate
                continue
            if current:
                lines.append(current)
            current = token
            if text_size(draw, current, fnt)[0] > max_width:
                chunk = ""
                for ch in token:
                    candidate = chunk + ch
                    if text_size(draw, candidate, fnt)[0] <= max_width:
                        chunk = candidate
                    else:
                        if chunk:
                            lines.append(chunk)
                        chunk = ch
                current = chunk
        if current:
            lines.append(current)
    return "\n".join(lines)


def centered_text(
    draw: ImageDraw.ImageDraw,
    xy: tuple[int, int, int, int],
    text: str,
    fnt: ImageFont.FreeTypeFont,
    fill: str = TEXT,
    spacing: int | None = None,
) -> None:
    x1, y1, x2, y2 = xy
    spacing = spacing if spacing is not None else max(4, fnt.size // 4)
    wrapped = wrap_text(draw, text, fnt, max(20, x2 - x1 - 26))
    tw, th = text_size(draw, wrapped, fnt)
    draw.multiline_text(
        (x1 + (x2 - x1 - tw) / 2, y1 + (y2 - y1 - th) / 2),
        wrapped,
        font=fnt,
        fill=fill,
        align="center",
        spacing=spacing,
    )


def left_text(
    draw: ImageDraw.ImageDraw,
    xy: tuple[int, int, int, int],
    text: str,
    fnt: ImageFont.FreeTypeFont,
    fill: str = TEXT,
    spacing: int | None = None,
) -> None:
    x1, y1, x2, _ = xy
    spacing = spacing if spacing is not None else max(4, fnt.size // 4)
    wrapped = wrap_text(draw, text, fnt, max(20, x2 - x1))
    draw.multiline_text((x1, y1), wrapped, font=fnt, fill=fill, spacing=spacing)


def rect(
    draw: ImageDraw.ImageDraw,
    xy: tuple[int, int, int, int],
    fill: str = GRAY,
    outline: str = BLUE,
    width: int = 4,
    radius: int = 22,
) -> None:
    draw.rounded_rectangle(xy, radius=radius, fill=fill, outline=outline, width=width)


def box(
    draw: ImageDraw.ImageDraw,
    xy: tuple[int, int, int, int],
    text: str,
    fill: str = GRAY,
    outline: str = BLUE,
    title: bool = False,
    color: str = TEXT,
    radius: int = 22,
) -> None:
    rect(draw, xy, fill=fill, outline=outline, radius=radius)
    centered_text(draw, xy, text, font(30 if title else 26, title), color)


def arrow(draw: ImageDraw.ImageDraw, start: tuple[int, int], end: tuple[int, int], color: str = BLUE, width: int = 5) -> None:
    draw.line([start, end], fill=color, width=width)
    angle = math.atan2(end[1] - start[1], end[0] - start[0])
    size = 18 + width
    pts = [
        end,
        (end[0] - size * math.cos(angle - math.pi / 7), end[1] - size * math.sin(angle - math.pi / 7)),
        (end[0] - size * math.cos(angle + math.pi / 7), end[1] - size * math.sin(angle + math.pi / 7)),
    ]
    draw.polygon(pts, fill=color)


def dashed_arrow(draw: ImageDraw.ImageDraw, start: tuple[int, int], end: tuple[int, int], color: str = RED, width: int = 4) -> None:
    x1, y1 = start
    x2, y2 = end
    length = math.hypot(x2 - x1, y2 - y1)
    steps = max(1, int(length / 24))
    for i in range(steps):
        if i % 2 == 0:
            a = i / steps
            b = min(1, (i + 0.7) / steps)
            draw.line(
                [(x1 + (x2 - x1) * a, y1 + (y2 - y1) * a), (x1 + (x2 - x1) * b, y1 + (y2 - y1) * b)],
                fill=color,
                width=width,
            )
    arrow(draw, start=(int(x1 + (x2 - x1) * 0.92), int(y1 + (y2 - y1) * 0.92)), end=end, color=color, width=width)


def title(draw: ImageDraw.ImageDraw, w: int, text: str) -> None:
    centered_text(draw, (0, 38, w, 112), text, font(44, True), NAVY)


def canvas(w: int, h: int) -> tuple[Image.Image, ImageDraw.ImageDraw]:
    img = Image.new("RGB", (w, h), WHITE)
    return img, ImageDraw.Draw(img)


def table(
    draw: ImageDraw.ImageDraw,
    x: int,
    y: int,
    col_widths: list[int],
    row_heights: list[int],
    cells: list[list[str]],
    header: bool = True,
) -> None:
    yy = y
    for r, rh in enumerate(row_heights):
        xx = x
        for c, cw in enumerate(col_widths):
            fill = NAVY if header and r == 0 else (LIGHT_BLUE if r % 2 else WHITE)
            outline = MID_GRAY if not (header and r == 0) else NAVY
            draw.rectangle((xx, yy, xx + cw, yy + rh), fill=fill, outline=outline, width=2)
            centered_text(draw, (xx + 8, yy + 6, xx + cw - 8, yy + rh - 6), cells[r][c], font(22 if r else 23, r == 0), WHITE if r == 0 else TEXT)
            xx += cw
        yy += rh


def save(img: Image.Image, part: int, code: str) -> Path:
    folder = OUT / f"Part{part}"
    folder.mkdir(parents=True, exist_ok=True)
    path = folder / f"{code}.png"
    img.save(path)
    return path


def draw_p1_f32() -> Image.Image:
    img, d = canvas(2048, 1136)
    title(d, 2048, "자산·위협·취약점·통제·위험 관계")
    y = 250
    xs = [170, 520, 900, 1280, 1640]
    labels = ["자산\n보호 대상", "위협원", "취약점 악용", "공격/사건", "영향/손실"]
    fills = [LIGHT_GREEN, LIGHT_BLUE, LIGHT_BLUE, LIGHT_RED, LIGHT_RED]
    outlines = [GREEN, BLUE, BLUE, RED, RED]
    for x, label, fill, outline in zip(xs, labels, fills, outlines):
        box(d, (x, y, x + 260, y + 160), label, fill=fill, outline=outline, title=True)
    arrow(d, (780, y + 80), (900, y + 80))
    arrow(d, (1160, y + 80), (1280, y + 80))
    arrow(d, (1540, y + 80), (1640, y + 80), color=RED)
    arrow(d, (430, y + 112), (900, y + 132), color=GREEN, width=4)
    centered_text(d, (520, y + 142, 850, y + 222), "자산은 취약점을 가질 수 있음", font(23, False), MUTED)
    box(d, (760, 650, 1288, 820), "통제\n취약점·발생 가능성·영향을 낮춤", fill=LIGHT_TEAL, outline=TEAL, title=True, color=TEAL_DARK)
    arrow(d, (875, 650), (975, 410), color=TEAL)
    arrow(d, (1024, 650), (1410, 410), color=TEAL)
    arrow(d, (1175, 650), (1760, 410), color=TEAL)
    box(d, (210, 895, 940, 1008), "위험 = 발생 가능성 × 영향", fill=WHITE, outline=NAVY, title=True)
    box(d, (1108, 895, 1840, 1008), "통제 후 남는 위험 = 잔여위험", fill=WHITE, outline=TEAL, title=True, color=TEAL_DARK)
    return img


def draw_p1_f52() -> Image.Image:
    img, d = canvas(2048, 1136)
    title(d, 2048, "시스템 분석 도구 분류 지도")
    cards = [
        ("호스트·포트", "Nmap\nMasscan\nZMap\nNetcat(연결 시험)"),
        ("취약점 스캐너", "Nessus\nOpenVAS/Greenbone\nQualys\nSARA·SATAN(역사적)"),
        ("파일 무결성", "Tripwire\nAIDE\nSamhain"),
        ("패킷·IDS", "Wireshark\ntcpdump\nSnort\nSuricata"),
        ("로그·SIEM", "syslog/journalctl\nEvent Viewer\nELK/Splunk\nSIEM"),
        ("프로세스·루트킷", "ps\nlsof\nchkrootkit\nrkhunter"),
        ("악성코드 분석", "YARA\n정적 분석\n샌드박스·동적 분석"),
    ]
    positions = [
        (105, 170, 565, 385),
        (595, 170, 1055, 385),
        (1085, 170, 1545, 385),
        (1575, 170, 2035, 385),
        (265, 455, 725, 670),
        (795, 455, 1255, 670),
        (1325, 455, 1785, 670),
    ]
    for (head, body), xy in zip(cards, positions):
        rect(d, xy, fill=LIGHT_BLUE, outline=BLUE)
        centered_text(d, (xy[0], xy[1] + 18, xy[2], xy[1] + 72), head, font(30, True), NAVY)
        centered_text(d, (xy[0] + 24, xy[1] + 84, xy[2] - 24, xy[3] - 18), body, font(24), TEXT)
    box(
        d,
        (240, 825, 1808, 965),
        "도구 기능은 겹칠 수 있으므로 이름보다 관찰 대상·입력·출력을 기준으로 구분한다.",
        fill=LIGHT_TEAL,
        outline=TEAL,
        title=True,
        color=TEAL_DARK,
    )
    return img


def draw_p2_f02() -> Image.Image:
    img, d = canvas(2848, 1504)
    # Panel headings only; no whole-image title or code.
    columns = [(110, 90, 860, 1330), (990, 90, 1700, 1330), (1830, 90, 2738, 1330)]
    for xy, head in zip(columns, ["OSI 계층", "TCP/IP 계층", "대표 장비·PDU·주소"]):
        rect(d, xy, fill=WHITE, outline=NAVY, radius=28)
        centered_text(d, (xy[0], xy[1] + 20, xy[2], xy[1] + 90), head, font(42, True), NAVY)
    osi_rows = [
        ("7 응용", "Data"),
        ("6 표현", "Data"),
        ("5 세션", "Data"),
        ("4 전송", "Segment / Datagram\nPort"),
        ("3 네트워크", "Packet\nIP"),
        ("2 데이터링크", "Frame\nMAC"),
        ("1 물리", "Bit"),
    ]
    y = 210
    row_h = 145
    for i, (layer, meta) in enumerate(osi_rows):
        fill = LIGHT_BLUE if i < 3 else (LIGHT_TEAL if i == 3 else WHITE)
        rect(d, (180, y, 790, y + row_h - 18), fill=fill, outline=BLUE)
        centered_text(d, (195, y + 8, 775, y + row_h - 26), f"{layer}\n{meta}", font(28, True), NAVY)
        y += row_h
    tcp_rows = [
        ("응용", "OSI 7·6·5"),
        ("전송", "OSI 4"),
        ("인터넷", "OSI 3"),
        ("네트워크 액세스", "OSI 2·1"),
    ]
    y_positions = [(210, 628), (650, 778), (800, 948), (970, 1250)]
    for (name, meta), (y1, y2) in zip(tcp_rows, y_positions):
        box(d, (1080, y1, 1610, y2), f"{name}\n{meta}", fill=LIGHT_TEAL, outline=TEAL, title=True, color=TEAL_DARK)
    for sy, ey in [(281, 419), (426, 419), (571, 419), (716, 714), (861, 874), (1006, 1110), (1151, 1110)]:
        arrow(d, (790, sy), (1080, ey), color=TEAL, width=4)
    equipment = [
        ("L7", "Proxy / WAF", "응용 계층"),
        ("L4", "Load Balancer", "전송 계층"),
        ("L3", "Router / L3 Switch", "인터넷 계층"),
        ("L2", "Bridge / Switch", "Frame · MAC"),
        ("L1", "Repeater / Hub", "Bit"),
    ]
    y = 210
    for layer, name, note in equipment:
        box(d, (1900, y, 2668, y + 150), f"{layer}  {name}\n{note}", fill=LIGHT_BLUE, outline=BLUE, title=True)
        y += 190
    return img


def draw_p2_f10() -> Image.Image:
    img, d = canvas(2848, 1504)
    root = (1170, 130, 1678, 320)
    sw1 = (420, 850, 930, 1045)
    sw2 = (1918, 850, 2428, 1045)
    box(d, root, "Root Bridge\n모든 포트: Designated / Forwarding", fill=LIGHT_TEAL, outline=TEAL, title=True, color=TEAL_DARK)
    box(d, sw1, "비루트 스위치 A", fill=LIGHT_BLUE, outline=BLUE, title=True)
    box(d, sw2, "비루트 스위치 B", fill=LIGHT_BLUE, outline=BLUE, title=True)
    d.line([(930, 850), (1170, 320)], fill=NAVY, width=8)
    d.line([(1918, 850), (1678, 320)], fill=NAVY, width=8)
    d.line([(930, 945), (1918, 945)], fill=NAVY, width=8)
    box(d, (930, 515, 1295, 610), "Root Port\nForwarding", fill=WHITE, outline=GREEN, title=True, color=GREEN)
    box(d, (1550, 515, 1918, 610), "Root Port\nForwarding", fill=WHITE, outline=GREEN, title=True, color=GREEN)
    box(d, (1030, 980, 1375, 1075), "Designated\nForwarding", fill=WHITE, outline=TEAL, title=True, color=TEAL_DARK)
    box(d, (1475, 980, 1845, 1075), "Alternate\nDiscarding", fill=LIGHT_RED, outline=RED, title=True, color=RED)
    box(d, (990, 365, 1320, 460), "Designated\nForwarding", fill=WHITE, outline=TEAL, title=True, color=TEAL_DARK)
    box(d, (1528, 365, 1858, 460), "Designated\nForwarding", fill=WHITE, outline=TEAL, title=True, color=TEAL_DARK)
    box(
        d,
        (530, 1220, 2318, 1348),
        "BPDU의 Root ID와 Path Cost로 포트 역할이 결정된다. Root Bridge에는 Root Port가 없다.",
        fill=WHITE,
        outline=NAVY,
        title=True,
    )
    return img


def draw_p2_f20() -> Image.Image:
    img, d = canvas(1600, 850)
    box(d, (70, 305, 300, 445), "Client\nUDP 68", fill=LIGHT_BLUE, outline=BLUE, title=True)
    box(d, (1300, 305, 1530, 445), "DHCP Server\nUDP 67", fill=LIGHT_TEAL, outline=TEAL, title=True, color=TEAL_DARK)
    steps = [
        ("1 Discover  Client UDP 68 → Server UDP 67", BLUE, (450, 95, 1150, 175), True),
        ("2 Offer  Server → Client", TEAL, (450, 240, 1150, 320), False),
        ("3 Request  Client → Server", BLUE, (450, 385, 1150, 465), True),
        ("4 ACK  Server → Client", TEAL, (450, 530, 1150, 610), False),
    ]
    for label, color, xy, ctos in steps:
        rect(d, xy, fill=WHITE, outline=color)
        centered_text(d, (xy[0] + 10, xy[1] + 8, xy[2] - 10, xy[3] - 8), label, font(27, True), color)
        if ctos:
            arrow(d, (300, (xy[1] + xy[3]) // 2), (xy[0], (xy[1] + xy[3]) // 2), color=color, width=4)
            arrow(d, (xy[2], (xy[1] + xy[3]) // 2), (1300, (xy[1] + xy[3]) // 2), color=color, width=4)
        else:
            arrow(d, (1300, (xy[1] + xy[3]) // 2), (xy[2], (xy[1] + xy[3]) // 2), color=color, width=4)
            arrow(d, (xy[0], (xy[1] + xy[3]) // 2), (300, (xy[1] + xy[3]) // 2), color=color, width=4)
    box(d, (90, 650, 560, 780), "방어 패널\nDHCP Snooping · 신뢰 포트 · 바인딩 테이블", fill=LIGHT_TEAL, outline=TEAL, title=True, color=TEAL_DARK)
    box(d, (1040, 650, 1510, 780), "공격 패널\nDHCP Starvation · Rogue DHCP", fill=LIGHT_RED, outline=RED, title=True, color=RED)
    return img


def draw_p2_f31() -> Image.Image:
    img, d = canvas(1600, 850)
    cells = [
        ["방식", "개인용 인증", "기업용 인증", "데이터 보호", "판단"],
        ["WEP", "공유키", "해당 없음", "RC4·짧은 IV", "폐기"],
        ["WPA", "PSK", "802.1X/EAP", "TKIP/RC4", "레거시"],
        ["WPA2", "PSK", "802.1X/EAP", "AES-CCMP", "강한 설정 필요"],
        ["WPA3", "SAE", "802.1X/EAP", "강화된 AES 계열\nPMF 필수", "권장"],
    ]
    table(d, 80, 90, [180, 300, 320, 400, 220], [86, 116, 116, 116, 136], cells)
    box(
        d,
        (110, 660, 1490, 765),
        "SAE는 WPA3-Personal의 인증 방식이다. Enterprise는 802.1X/EAP를 사용하며, WPA3에서는 PMF가 필수이다.",
        fill=LIGHT_TEAL,
        outline=TEAL,
        title=True,
        color=TEAL_DARK,
    )
    return img


def draw_p2_f32() -> Image.Image:
    img, d = canvas(1600, 850)
    actors = [
        ("Supplicant\n단말", (80, 90, 350, 190)),
        ("Authenticator\nSwitch/AP", (665, 90, 935, 190)),
        ("Authentication Server\nRADIUS", (1250, 90, 1520, 190)),
    ]
    for text, xy in actors:
        box(d, xy, text, fill=LIGHT_BLUE if xy[0] < 1200 else LIGHT_TEAL, outline=BLUE if xy[0] < 1200 else TEAL, title=True)
    x = [215, 800, 1385]
    for xx in x:
        d.line([(xx, 210), (xx, 700)], fill=MID_GRAY, width=3)
    events = [
        (250, 0, 1, "EAPOL-Start"),
        (315, 1, 0, "Identity 요청"),
        (380, 0, 1, "Identity 응답"),
        (445, 1, 2, "RADIUS Access-Request"),
        (510, 2, 1, "Access-Challenge / EAP 응답 왕복"),
        (575, 2, 1, "Access-Accept · EAP-Success"),
        (640, 1, 0, "Controlled Port 허용\nVLAN/ACL 적용"),
    ]
    for y, a, b, label in events:
        arrow(d, (x[a], y), (x[b], y), color=TEAL if a > b else BLUE, width=4)
        centered_text(d, (min(x[a], x[b]) + 20, y - 46, max(x[a], x[b]) - 20, y - 5), label, font(20, True), NAVY)
    return img


def draw_p2_f41() -> Image.Image:
    img, d = canvas(1600, 850)
    cells = [
        ["스캔", "Open", "Closed", "Filtered / 기타"],
        ["SYN", "SYN/ACK", "RST", "무응답 또는 ICMP"],
        ["Connect", "Handshake 성공", "RST", "Timeout / ICMP"],
        ["FIN / NULL / Xmas", "무응답 = open|filtered", "RST", "모호 가능"],
        ["ACK", "Open/Closed 구분 불가", "Open/Closed 구분 불가", "RST=unfiltered\n무응답/ICMP=filtered"],
        ["UDP", "응용 응답", "ICMP Port Unreachable", "무응답 = open|filtered"],
    ]
    table(d, 70, 72, [270, 365, 365, 430], [80, 105, 105, 118, 135, 118], cells)
    return img


def draw_p2_f51() -> Image.Image:
    img, d = canvas(1600, 850)
    panels = [
        ("Dual-Homed Host", "외부망 ↔ 두 NIC Bastion/Proxy ↔ 내부망\n직접 라우팅 제한", (60, 90, 500, 720)),
        ("Screened Host", "외부망 ↔ Screening Router ↔ 내부측 Bastion Host\n외부 접근은 Bastion으로 제한", (580, 90, 1020, 720)),
        ("Screened Subnet", "두 필터링 지점 또는 3-leg 방화벽이 DMZ 생성\n공개 서버는 DMZ에 배치", (1100, 90, 1540, 720)),
    ]
    for head, body, xy in panels:
        rect(d, xy, fill=WHITE, outline=NAVY, radius=26)
        centered_text(d, (xy[0], xy[1] + 20, xy[2], xy[1] + 78), head, font(28, True), NAVY)
        y = xy[1] + 135
        labels = ["외부망", "필터링", "Bastion/DMZ", "내부망"]
        for i, lab in enumerate(labels):
            bx = (xy[0] + 45, y + i * 100, xy[2] - 45, y + i * 100 + 62)
            fill = LIGHT_RED if i == 0 else LIGHT_TEAL if i == 2 else LIGHT_BLUE
            outline = RED if i == 0 else TEAL if i == 2 else BLUE
            box(d, bx, lab, fill=fill, outline=outline, title=True, color=RED if i == 0 else TEXT)
            if i:
                arrow(d, ((bx[0] + bx[2]) // 2, bx[1] - 30), ((bx[0] + bx[2]) // 2, bx[1]), color=TEAL, width=4)
        left_text(d, (xy[0] + 42, xy[3] - 140, xy[2] - 42, xy[3] - 20), body, font(22), TEXT)
    return img


def draw_p2_f61() -> Image.Image:
    img, d = canvas(1600, 850)
    steps = [
        ("ClientHello", BLUE),
        ("ServerHello", TEAL),
        ("EncryptedExtensions", TEAL),
        ("Certificate", TEAL),
        ("CertificateVerify", TEAL),
        ("Server Finished", TEAL),
        ("Client Finished", BLUE),
        ("Application Data", GREEN),
    ]
    x0, y0 = 70, 150
    w, h, gap = 300, 92, 46
    coords = []
    for i, (label, color) in enumerate(steps):
        row = i // 4
        col = i % 4
        x = x0 + col * (w + gap)
        y = y0 + row * 210
        coords.append((x, y, x + w, y + h, color, label))
        rect(d, (x, y, x + w, y + h), fill=WHITE if label != "Application Data" else LIGHT_GREEN, outline=color)
        centered_text(d, (x + 10, y + 8, x + w - 10, y + h - 8), label, font(24, True), color)
    for i in range(len(coords) - 1):
        a = coords[i]
        b = coords[i + 1]
        if i == 3:
            d.line([(a[0] + w // 2, a[3]), (a[0] + w // 2, a[3] + 72), (b[0] + w // 2, b[1] - 72), (b[0] + w // 2, b[1])], fill=TEAL, width=4)
            arrow(d, (b[0] + w // 2, b[1] - 36), (b[0] + w // 2, b[1]), color=TEAL, width=4)
        else:
            arrow(d, (a[2], a[1] + h // 2), (b[0], b[1] + h // 2), color=TEAL if i >= 1 else BLUE, width=4)
    d.line([(70, 315), (1530, 315)], fill=RED, width=5)
    centered_text(d, (450, 322, 1150, 370), "ServerHello 이후 후속 핸드셰이크 보호 시작", font(26, True), RED)
    box(
        d,
        (110, 650, 1490, 765),
        "인증서 개인키는 CertificateVerify 서명에 사용된다. 대량 응용데이터를 인증서 RSA 키로 직접 암호화하지 않는다.",
        fill=LIGHT_TEAL,
        outline=TEAL,
        title=True,
        color=TEAL_DARK,
    )
    return img


RENDERERS = {
    "P1-F32": (1, draw_p1_f32),
    "P1-F52": (1, draw_p1_f52),
    "P2-F02": (2, draw_p2_f02),
    "P2-F10": (2, draw_p2_f10),
    "P2-F20": (2, draw_p2_f20),
    "P2-F31": (2, draw_p2_f31),
    "P2-F32": (2, draw_p2_f32),
    "P2-F41": (2, draw_p2_f41),
    "P2-F51": (2, draw_p2_f51),
    "P2-F61": (2, draw_p2_f61),
}


def manifest_rows() -> dict[str, dict[str, str]]:
    with MANIFEST.open("r", encoding="utf-8-sig", newline="") as f:
        return {row["code"]: row for row in csv.DictReader(f)}


def make_contact_sheet(paths: Iterable[Path]) -> None:
    thumbs = []
    for path in paths:
        img = Image.open(path).convert("RGB")
        img.thumbnail((360, 220))
        tile = Image.new("RGB", (390, 270), WHITE)
        x = (390 - img.width) // 2
        tile.paste(img, (x, 12))
        d = ImageDraw.Draw(tile)
        centered_text(d, (0, 232, 390, 265), path.name, font(20, True), NAVY)
        thumbs.append(tile)
    sheet = Image.new("RGB", (390 * 2, 270 * 5), WHITE)
    for i, tile in enumerate(thumbs):
        sheet.paste(tile, ((i % 2) * 390, (i // 2) * 270))
    sheet.save(CONTACT_SHEET)


def main() -> None:
    rows = manifest_rows()
    generated: list[Path] = []
    for code, (part, render) in RENDERERS.items():
        img = render()
        row = rows[code]
        expected = (int(row["source_width"]), int(row["source_height"]))
        if img.size != expected:
            raise ValueError(f"{code}: expected {expected}, got {img.size}")
        generated.append(save(img, part, code))
    make_contact_sheet(generated)
    print("\n".join(str(p) for p in generated))
    print(f"contact_sheet={CONTACT_SHEET}")


if __name__ == "__main__":
    main()
