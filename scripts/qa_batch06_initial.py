from __future__ import annotations

import csv
import shutil
from pathlib import Path

from render_batch03_text_fixes import ROOT


GUIDE = ROOT / "00_가이드"
COMPLETE = ROOT / "03_수정완료"
REWORK = ROOT / "04_재작업"
MANAGEMENT = GUIDE / "나노바나나_작업관리표_v2.csv"

BATCH = "06"

ITEMS = [
    ("P5-F26", "Part5", "통과", "물리보안 구역, 인증요건, 출입기록, 반입·반출 통제와 Tailgating 방지가 명확함. 전체 제목·코드 없음."),
    ("P5-F41", "Part5", "통과", "레지스터·캐시부터 원격 로그·백업까지 휘발성 우선순위가 명확하고 수집 영향 판단 기준이 적절함."),
    ("P5-F42", "Part5", "통과", "디지털 증거 식별-보존-수집-검사-분석-보고-보관/폐기 생명주기와 무결성 관리가 명확함."),
    ("P5-F46", "Part5", "재작업", "상단 전체 제목이 남아 있고 '인증도애'처럼 어색한 문구가 있음. 3개 영역·101개 기준 구조만 제목 없이 표시 필요."),
    ("P5-F49", "Part5", "통과", "CC 인증에서 PP, ST, TOE, SFR/SAR, EAL과 평가·인증 흐름이 명확하고 개념 오류가 크지 않음."),
    ("P5-F53", "Part5", "재작업", "중앙에 시험 강조점 박스가 있고 조직 인증/제품 인증 비교가 과밀함. 시험 문구 없이 평가대상 차이를 정리해야 함."),
    ("P5-F54", "Part5", "재작업", "사이버 윤리 항목 설명에 깨진 한글과 부정확한 문장이 많음. 책임·존중·공정·프라이버시 등 핵심 원칙 재작성 필요."),
    ("P5-F55", "Part5", "재작업", "여러 설명 문구가 깨져 있고 시험 강조 박스가 남아 있음. 게시 전 점검-게시-확산-피해대응 흐름을 정확히 정리해야 함."),
    ("P5-F64", "Part5", "재작업", "상단 전체 제목과 일부 영어 오탈자가 남아 있음. 법률별 보호대상·목적 차이를 제목 없이 명확히 표시해야 함."),
    ("P5-F68", "Part5", "재작업", "상단 전체 제목과 하단 그림 코드가 남아 있음. 위원회-관계 중앙행정기관-관리기관-전문기관 역할 흐름만 표시해야 함."),
]

CORRECTIONS = {
    "P5-F46": "전체 제목 없이 ISMS-P 인증체계의 3개 영역을 기능 패널로 구성한다. 관리체계 수립 및 운영 16개, 보호대책 요구사항 64개, 개인정보 처리단계별 요구사항 21개를 정확히 표시하고 합계 101개 기준을 표시한다. '인증도애' 같은 오탈자, 상단 전체 제목, 그림 코드 금지.",
    "P5-F53": "시험 강조 문구 없이 조직 인증과 제품 인증을 좌우 비교한다. 조직 인증은 ISMS/ISMS-P, 조직 전체 또는 특정 서비스 범위, 관리적·물리적·기술적 보호조치 운영, 내부 지침·정책·활동 이력·점검 기록을 표시한다. 제품 인증은 CC/암호모듈/특정제도, 제품 기능 단위 또는 통합 제품, 설계·구현·취약점 점검 및 검증, 제품 명세서·보안목표명세서(ST)·평가보고서를 표시한다. 두 대상을 혼동하지 말 것.",
    "P5-F54": "전체 제목 없이 중앙에 온라인 행위 판단을 두고 책임, 존중, 공정, 안전, 프라이버시, 지식재산 원칙을 방사형으로 구성한다. 하단에는 '합법이라고 항상 윤리적인 것은 아니며, 표현의 자유와 타인의 권리를 함께 고려한다.'를 표시한다. 깨진 한글, 의미 없는 문장, 시험 문구 금지.",
    "P5-F55": "전체 제목과 시험 강조 박스 없이 디지털 시민의 책임 흐름을 표시한다. 게시 전 점검, 동의·프라이버시 확인, 출처·저작권 확인, 게시, 빠른 확산·검색 가능·장기 잔존, 문제 발생 시 증거 보존·신고·정정/삭제·피해자 보호를 정확히 연결한다. '익명성은 책임을 없애지 않는다.'를 짧게 표시한다.",
    "P5-F64": "전체 제목 없이 국내 정보보호 법제를 법률별 보호대상·목적 차이 중심으로 지도화한다. 정보통신망법은 망 안정성·침해행위·악성프로그램·스팸, 정보통신기반보호법은 주요정보통신기반시설 지정·보호, 전자서명법은 전자서명·인증서비스 신뢰, 개인정보보호법은 개인정보 처리와 정보주체 권리, 저작권법은 디지털 저작물, 정보보호산업법은 정보보호 산업 진흥을 표시한다. 영어 오탈자와 상단 제목 금지.",
    "P5-F68": "전체 제목과 그림 코드 없이 주요정보통신기반시설 보호체계의 역할 흐름만 표시한다. 정보통신기반보호위원회는 정책·조정 및 심의·의결, 관계 중앙행정기관은 지정·감독·지원, 관리기관은 취약점 분석·평가와 보호대책 수립·이행, 전문기관은 기술지원과 취약점 분석평가 지원으로 구성한다. 보호지침·지침, 감독 및 지원, 기술지원 요청·결과 화살표를 명확히 표시한다.",
}


def move_rework_files() -> dict[str, Path]:
    locations: dict[str, Path] = {}
    for code, part_dir, status, _ in ITEMS:
        src = COMPLETE / part_dir / f"{code}.png"
        if status == "재작업":
            dst = REWORK / part_dir / f"{code}.png"
            dst.parent.mkdir(parents=True, exist_ok=True)
            if src.exists():
                if dst.exists():
                    dst.unlink()
                shutil.move(str(src), str(dst))
            locations[code] = dst
        else:
            locations[code] = src
    return locations


def write_visual_csv(locations: dict[str, Path]) -> Path:
    out = GUIDE / "batch06_nano_banana_육안검수결과.csv"
    with out.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["batch", "code", "visual_status", "reason", "current_location"])
        writer.writeheader()
        for code, _, status, reason in ITEMS:
            writer.writerow(
                {
                    "batch": BATCH,
                    "code": code,
                    "visual_status": status,
                    "reason": reason,
                    "current_location": str(locations[code]),
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
    visual_csv = write_visual_csv(locations)
    update_management()
    print(visual_csv)
    print("pass=4 rework=6")


if __name__ == "__main__":
    main()
