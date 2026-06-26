from __future__ import annotations

import csv
import shutil

from render_batch03_text_fixes import ROOT


GUIDE = ROOT / "00_가이드"
COMPLETE = ROOT / "03_수정완료"
REWORK = ROOT / "04_재작업"
MANAGEMENT = GUIDE / "나노바나나_작업관리표_v2.csv"

BATCH = "07"

ITEMS = [
    ("P5-F73", "Part5", "재작업", "전자서명법 개정 전후 구조는 좋지만 하단에 시험 문제 언급이 남아 있음. 시험 문구 없이 현재 제도와 과거 용어 구분만 표시해야 함."),
    ("P5-F74", "Part5", "통과", "개인정보보호법 처리 원칙, 생명주기, 정보주체 권리, 처리자 의무와 침해 대응 흐름이 명확함."),
    ("P5-F77", "Part5", "통과", "개인정보 처리 단계와 적법 근거, 제3자 제공, 보관·파기, 안전조치 공통 준수사항이 명확함."),
    ("P5-F83", "Part5", "재작업", "상단 시험 대비 제목이 있고 Privacy Policy 항목에 어색한 오탈자가 많음. 처리방침 필수 항목과 실제 처리 일치 원칙만 표시해야 함."),
    ("P1-F24", "Part1", "재작업", "상단 전체 영어 제목이 남아 있음. UNIX/Linux 권한 구조와 750 계산, 파일/디렉터리 권한 의미를 제목 없이 정리해야 함."),
    ("P1-F30", "Part1", "재작업", "상단 전체 제목이 남아 있고 이벤트 상관분석 흐름이 희박함. 사용자·호스트·네트워크 이벤트를 시간순으로 연결해 침해 흐름을 보여야 함."),
    ("P2-F14", "Part2", "통과", "CIDR/VLSM에서 큰 요구부터 /25, /26, /27을 배정하고 네트워크·브로드캐스트 제외 및 중첩 금지가 명확함."),
    ("P2-F18", "Part2", "통과", "IPv6 NDP 기능과 Dual Stack, Tunneling, NAT64/DNS64 전환 방식이 명확함."),
    ("P2-F21", "Part2", "통과", "ICMP 주요 메시지, IGMP 멀티캐스트 그룹 관리, Unicast/Broadcast/Multicast/Anycast 전송 범위가 명확함."),
    ("P2-F33", "Part2", "통과", "무선 공격 유형과 PMF, WIDS/WIPS, 패치, WPA2/WPA3, 802.1X 대응 관계가 명확함."),
]

CORRECTIONS = {
    "P5-F73": "전체 제목과 시험 문구 없이 전자서명법 개정 전후를 좌우 비교한다. 개정 전은 공인인증서·공인인증기관·공인전자서명 중심, 개정 후는 전자서명인증사업자, 평가기관 인정·공표, 다양한 전자서명수단의 경쟁, 모든 전자서명의 동등한 법적 효력을 표시한다. 하단에는 과거 기술 표현과 현행 제도 용어 구분만 짧게 표시한다.",
    "P5-F83": "전체 제목과 시험 대비 문구 없이 개인정보 처리방침 점검 구조를 표시한다. 처리 현황은 시스템 로그, 데이터베이스, 접근권한을 포함한다. Privacy Policy 항목에는 처리 목적, 처리 항목, 보유기간, 제3자 제공, 처리위탁, 파기, 정보주체 권리, 안전성 확보조치, 자동수집, 변경 이력을 정확히 표시한다. 처리방침은 실제 처리와 일치해야 하며 동의를 대신하지 않는다는 문구를 표시한다. 오탈자 금지.",
    "P1-F24": "전체 제목 없이 UNIX/Linux 권한 문자열 구조를 표시한다. 파일 타입 1문자(-, d, l), 사용자/그룹/기타 권한 rwx, r=4 w=2 x=1, 예시 rwxr-x--- = 750을 정확히 계산한다. 파일 권한에서 r=내용 읽기, w=내용 수정, x=실행. 디렉터리 권한에서 r=목록 조회, w=파일 생성·삭제, x=진입/탐색을 표시한다.",
    "P1-F30": "전체 제목 없이 이벤트 상관분석 타임라인을 구성한다. 사용자, Host A, Host B, 네트워크 레인을 두고 로그인 실패, 로그인 성공, 권한 변경, 원격 실행, 중요 파일 접근, 외부 전송, 로그 삭제 이벤트를 시간순으로 연결한다. 하단에는 개별 약한 신호를 시간순으로 연결하면 계정 침해, 권한 상승, 내부 이동, 정보 유출 흐름을 볼 수 있다는 결론을 표시한다.",
}


def move_rework_files() -> dict[str, str]:
    locations: dict[str, str] = {}
    for code, part_dir, status, _ in ITEMS:
        src = COMPLETE / part_dir / f"{code}.png"
        if status == "재작업":
            dst = REWORK / part_dir / f"{code}.png"
            dst.parent.mkdir(parents=True, exist_ok=True)
            if src.exists():
                if dst.exists():
                    dst.unlink()
                shutil.move(str(src), str(dst))
            locations[code] = str(dst)
        else:
            locations[code] = str(src)
    return locations


def write_visual_csv(locations: dict[str, str]) -> None:
    out = GUIDE / "batch07_nano_banana_육안검수결과.csv"
    with out.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["batch", "code", "visual_status", "reason", "current_location"])
        writer.writeheader()
        for code, _, status, reason in ITEMS:
            writer.writerow({"batch": BATCH, "code": code, "visual_status": status, "reason": reason, "current_location": locations[code]})
    print(out)


def update_management() -> None:
    with MANAGEMENT.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        fields = reader.fieldnames or []
        rows = list(reader)

    status_col = fields[16]
    first_col = fields[17]
    issue_col = fields[6]
    required_col = fields[7]
    note_col = fields[19]
    item_map = {code: (status, reason) for code, _, status, reason in ITEMS}

    for row in rows:
        if row.get("batch") == BATCH and row.get("code") in item_map:
            status, reason = item_map[row["code"]]
            row[status_col] = "완료" if status == "통과" else "재작업"
            row[first_col] = status
            row[note_col] = reason
            if status == "재작업":
                row[issue_col] = reason
                row[required_col] = CORRECTIONS[row["code"]]

    with MANAGEMENT.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    locations = move_rework_files()
    write_visual_csv(locations)
    update_management()
    print("pass=6 rework=4")


if __name__ == "__main__":
    main()
