# Nano Banana 작업용 프롬프트 묶음 · A 우선순위 정렬

- 입력 이미지는 `input_abs` 경로의 PNG를 사용한다.
- 결과는 `output_abs` 경로에 `output_filename` 그대로 저장한다.
- Part1은 내부 전체 제목 1개 유지, Part2~Part5는 내부 전체 제목·그림 코드 금지 정책을 따른다.
- 출력은 PNG/RGB/불투명 흰 배경, 원본 픽셀 크기 유지.

## [A] P1-F32 · 자산·위협·취약점·통제·위험 관계 · 전면 재생성

```text
[A] P1-F32 · 자산·위협·취약점·통제·위험 관계 · 전면 재생성

input_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\01_전면재생성\Part1\P1-F32.png
output_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\03_수정완료\Part1\P1-F32.png
canvas: 2048 x 1136 px
output_filename: P1-F32.png
title_policy: 내부 전체 제목 1개 유지, 그림 코드 금지

문제:
자산·취약점·통제의 화살표가 인과관계를 반대로 읽히게 한다.

필수 수정:
`위협원 → 취약점 악용 → 공격/사건 → 영향/손실`을 주 흐름으로, 통제는 취약점·가능성·영향을 낮추는 방향으로 재구성. `위험=가능성×영향`, `잔여위험` 표시.

통합 가이드 세부 지침:
- 주 흐름: `위협원 → 취약점 악용 → 공격/사건 → 영향/손실`
- `자산`은 보호 대상이며 취약점을 가질 수 있다.
- `통제`는 취약점, 발생 가능성 또는 영향을 낮추는 방향으로만 연결한다.
- 하단: `위험 = 발생 가능성 × 영향`, `통제 후 남는 위험 = 잔여위험`
- 내부 전체 제목은 정확히 한 번 유지하고 코드만 넣지 않는다.

기본 프롬프트:
정보보안기사 시험 대비용 한국어 교육 도식이다.
원본의 학습 목적만 유지하고, 아래에 지정한 정확한 구조와 허용 텍스트로 새로 그린다.
흰 배경, 네이비·틸·밝은 회색 중심, 위험·오류만 빨강, 단순한 벡터 스타일.
화살표는 실제 데이터·제어 흐름에만 사용하고 방향을 정확히 맞춘다.
허용 텍스트 외의 문구, 워터마크, 프롬프트 문장, 파일명, 가짜 수식, 의미 없는 약어를 넣지 않는다.
출력 크기와 제목 정책은 해당 코드의 매니페스트를 따른다.

공통 네거티브:
no watermark, no prompt text, no placeholder text, no pseudo-Korean,
no misspelled Korean, no duplicate labels, no invented formula,
no tiny text, no decorative arrows, no gradient background,
no photorealistic style, no file name, no version string
```

## [A] P1-F52 · 시스템 분석 도구 분류 지도 · 전면 재생성

```text
[A] P1-F52 · 시스템 분석 도구 분류 지도 · 전면 재생성

input_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\01_전면재생성\Part1\P1-F52.png
output_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\03_수정완료\Part1\P1-F52.png
canvas: 2048 x 1136 px
output_filename: P1-F52.png
title_policy: 내부 전체 제목 1개 유지, 그림 코드 금지

문제:
도구 분류가 혼재되어 패킷·로그·취약점·무결성 도구의 역할을 잘못 학습할 수 있다.

필수 수정:
`호스트·포트`, `취약점 스캐너`, `파일 무결성`, `패킷·IDS`, `로그·SIEM`, `프로세스·루트킷`, `악성코드 분석` 7분류로 재구성하고 도구 역할을 올바르게 배치.

통합 가이드 세부 지침:
7개 영역으로 재분류한다.

1. `호스트·포트`: Nmap, Masscan, ZMap, Netcat(연결 시험)
2. `취약점 스캐너`: Nessus, OpenVAS/Greenbone, Qualys, SARA·SATAN(역사적)
3. `파일 무결성`: Tripwire, AIDE, Samhain
4. `패킷·IDS`: Wireshark, tcpdump, Snort, Suricata
5. `로그·SIEM`: syslog/journalctl, Event Viewer, ELK/Splunk, SIEM
6. `프로세스·루트킷`: ps, lsof, chkrootkit, rkhunter
7. `악성코드 분석`: YARA, 정적 분석, 샌드박스·동적 분석

하단 주석: `도구 기능은 겹칠 수 있으므로 이름보다 관찰 대상·입력·출력을 기준으로 구분한다.`

기본 프롬프트:
정보보안기사 시험 대비용 한국어 교육 도식이다.
원본의 학습 목적만 유지하고, 아래에 지정한 정확한 구조와 허용 텍스트로 새로 그린다.
흰 배경, 네이비·틸·밝은 회색 중심, 위험·오류만 빨강, 단순한 벡터 스타일.
화살표는 실제 데이터·제어 흐름에만 사용하고 방향을 정확히 맞춘다.
허용 텍스트 외의 문구, 워터마크, 프롬프트 문장, 파일명, 가짜 수식, 의미 없는 약어를 넣지 않는다.
출력 크기와 제목 정책은 해당 코드의 매니페스트를 따른다.

공통 네거티브:
no watermark, no prompt text, no placeholder text, no pseudo-Korean,
no misspelled Korean, no duplicate labels, no invented formula,
no tiny text, no decorative arrows, no gradient background,
no photorealistic style, no file name, no version string
```

## [A] P2-F02 · OSI 7계층과 TCP/IP 계층 대응 · 전면 재생성

```text
[A] P2-F02 · OSI 7계층과 TCP/IP 계층 대응 · 전면 재생성

input_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\01_전면재생성\Part2\P2-F02.png
output_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\03_수정완료\Part2\P2-F02.png
canvas: 2848 x 1504 px
output_filename: P2-F02.png
title_policy: 내부 전체 제목·그림 코드 금지

문제:
Repeater·Hub를 Switch와 함께 L2로 묶어 계층 대응이 틀렸다.

필수 수정:
OSI↔TCP/IP 대응을 다시 그리고 장비는 L1 Repeater/Hub, L2 Bridge/Switch, L3 Router/L3 Switch, L4 Load Balancer, L7 Proxy/WAF로 분리.

통합 가이드 세부 지침:
- OSI 7·6·5 → TCP/IP 응용, OSI 4 → 전송, OSI 3 → 인터넷, OSI 2·1 → 네트워크 액세스.
- 장비는 `Repeater·Hub=L1`, `Bridge·Switch=L2`, `Router·L3 Switch=L3`, `L4 Load Balancer=L4`, `Proxy·WAF=L7`로 분리한다.
- PDU와 주소는 Bit/Frame/Packet/Segment·Datagram/Data, MAC/IP/Port 순으로 연결한다.

기본 프롬프트:
정보보안기사 시험 대비용 한국어 교육 도식이다.
원본의 학습 목적만 유지하고, 아래에 지정한 정확한 구조와 허용 텍스트로 새로 그린다.
흰 배경, 네이비·틸·밝은 회색 중심, 위험·오류만 빨강, 단순한 벡터 스타일.
화살표는 실제 데이터·제어 흐름에만 사용하고 방향을 정확히 맞춘다.
허용 텍스트 외의 문구, 워터마크, 프롬프트 문장, 파일명, 가짜 수식, 의미 없는 약어를 넣지 않는다.
출력 크기와 제목 정책은 해당 코드의 매니페스트를 따른다.

공통 네거티브:
no watermark, no prompt text, no placeholder text, no pseudo-Korean,
no misspelled Korean, no duplicate labels, no invented formula,
no tiny text, no decorative arrows, no gradient background,
no photorealistic style, no file name, no version string
```

## [A] P2-F10 · STP 루프 방지 · 전면 재생성

```text
[A] P2-F10 · STP 루프 방지 · 전면 재생성

input_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\01_전면재생성\Part2\P2-F10.png
output_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\03_수정완료\Part2\P2-F10.png
canvas: 2848 x 1504 px
output_filename: P2-F10.png
title_policy: 내부 전체 제목·그림 코드 금지

문제:
Root Bridge에 Root Port가 있는 것으로 표시되고, 중복 링크 양쪽을 모두 차단한 것으로 보여 STP 역할이 틀렸다.

필수 수정:
Root Bridge에는 Root Port가 없고 모든 포트가 Designated/Forwarding임을 표시. 비루트 스위치는 각 1개 Root Port, 중복 세그먼트는 한쪽 Designated/Forwarding·다른 쪽 Alternate/Discarding.

통합 가이드 세부 지침:
- Root Bridge에는 Root Port가 없다. Root의 활성 포트는 `Designated/Forwarding`이다.
- 각 비루트 스위치는 Root까지 최저 비용의 포트 1개를 `Root Port`로 선택한다.
- 비루트 간 중복 세그먼트는 한쪽 `Designated/Forwarding`, 반대쪽 `Alternate/Discarding`으로 표시한다.
- BPDU의 Root ID·Path Cost로 역할이 결정됨을 간단히 덧붙인다.

기본 프롬프트:
정보보안기사 시험 대비용 한국어 교육 도식이다.
원본의 학습 목적만 유지하고, 아래에 지정한 정확한 구조와 허용 텍스트로 새로 그린다.
흰 배경, 네이비·틸·밝은 회색 중심, 위험·오류만 빨강, 단순한 벡터 스타일.
화살표는 실제 데이터·제어 흐름에만 사용하고 방향을 정확히 맞춘다.
허용 텍스트 외의 문구, 워터마크, 프롬프트 문장, 파일명, 가짜 수식, 의미 없는 약어를 넣지 않는다.
출력 크기와 제목 정책은 해당 코드의 매니페스트를 따른다.

공통 네거티브:
no watermark, no prompt text, no placeholder text, no pseudo-Korean,
no misspelled Korean, no duplicate labels, no invented formula,
no tiny text, no decorative arrows, no gradient background,
no photorealistic style, no file name, no version string
```

## [A] P2-F20 · DHCP DORA와 공격면 · 전면 재생성

```text
[A] P2-F20 · DHCP DORA와 공격면 · 전면 재생성

input_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\01_전면재생성\Part2\P2-F20.png
output_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\03_수정완료\Part2\P2-F20.png
canvas: 1600 x 850 px
output_filename: P2-F20.png
title_policy: 내부 전체 제목·그림 코드 금지

문제:
DORA 단계의 방향과 정상·공격 흐름이 교차해 절차가 잘못 읽힌다.

필수 수정:
Discover C→S, Offer S→C, Request C→S, ACK S→C를 한 줄로 명확히 표시하고 Starvation/Rogue DHCP/DHCP Snooping은 별도 패널.

통합 가이드 세부 지침:
- Discover: Client UDP 68 → Server UDP 67
- Offer: Server → Client
- Request: Client → Server
- ACK: Server → Client
- 공격 패널: `DHCP Starvation`, `Rogue DHCP`
- 방어 패널: `DHCP Snooping`, 신뢰 포트, 바인딩 테이블

기본 프롬프트:
정보보안기사 시험 대비용 한국어 교육 도식이다.
원본의 학습 목적만 유지하고, 아래에 지정한 정확한 구조와 허용 텍스트로 새로 그린다.
흰 배경, 네이비·틸·밝은 회색 중심, 위험·오류만 빨강, 단순한 벡터 스타일.
화살표는 실제 데이터·제어 흐름에만 사용하고 방향을 정확히 맞춘다.
허용 텍스트 외의 문구, 워터마크, 프롬프트 문장, 파일명, 가짜 수식, 의미 없는 약어를 넣지 않는다.
출력 크기와 제목 정책은 해당 코드의 매니페스트를 따른다.

공통 네거티브:
no watermark, no prompt text, no placeholder text, no pseudo-Korean,
no misspelled Korean, no duplicate labels, no invented formula,
no tiny text, no decorative arrows, no gradient background,
no photorealistic style, no file name, no version string
```

## [A] P2-F31 · WEP에서 WPA3까지 무선 보안 발전 · 전면 재생성

```text
[A] P2-F31 · WEP에서 WPA3까지 무선 보안 발전 · 전면 재생성

input_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\01_전면재생성\Part2\P2-F31.png
output_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\03_수정완료\Part2\P2-F31.png
canvas: 1600 x 850 px
output_filename: P2-F31.png
title_policy: 내부 전체 제목·그림 코드 금지

문제:
WPA 계열의 개인용·기업용 인증, 키 관리, 데이터 보호가 혼재하고 SAE 적용 범위가 잘못 읽힌다.

필수 수정:
WEP/WPA/WPA2/WPA3를 개인용 인증·기업용 인증·데이터 보호·현재 판단으로 분리. SAE=WPA3-Personal, Enterprise=802.1X/EAP, WPA3 PMF 필수.

통합 가이드 세부 지침:
| 방식 | 개인용 인증 | 기업용 인증 | 데이터 보호 | 판단 |
|---|---|---|---|---|
| WEP | 공유키 | 해당 없음 | RC4·짧은 IV | 폐기 |
| WPA | PSK | 802.1X/EAP | TKIP/RC4 | 레거시 |
| WPA2 | PSK | 802.1X/EAP | AES-CCMP | 강한 설정 필요 |
| WPA3 | SAE | 802.1X/EAP | 강화된 AES 계열·PMF 필수 | 권장 |

SAE를 Enterprise에 연결하지 않고, 4-way handshake를 WPA2만의 고유 키관리처럼 표현하지 않는다.

기본 프롬프트:
정보보안기사 시험 대비용 한국어 교육 도식이다.
원본의 학습 목적만 유지하고, 아래에 지정한 정확한 구조와 허용 텍스트로 새로 그린다.
흰 배경, 네이비·틸·밝은 회색 중심, 위험·오류만 빨강, 단순한 벡터 스타일.
화살표는 실제 데이터·제어 흐름에만 사용하고 방향을 정확히 맞춘다.
허용 텍스트 외의 문구, 워터마크, 프롬프트 문장, 파일명, 가짜 수식, 의미 없는 약어를 넣지 않는다.
출력 크기와 제목 정책은 해당 코드의 매니페스트를 따른다.

공통 네거티브:
no watermark, no prompt text, no placeholder text, no pseudo-Korean,
no misspelled Korean, no duplicate labels, no invented formula,
no tiny text, no decorative arrows, no gradient background,
no photorealistic style, no file name, no version string
```

## [A] P2-F32 · 802.1X·EAP·RADIUS 인증 흐름 · 전면 재생성

```text
[A] P2-F32 · 802.1X·EAP·RADIUS 인증 흐름 · 전면 재생성

input_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\01_전면재생성\Part2\P2-F32.png
output_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\03_수정완료\Part2\P2-F32.png
canvas: 1600 x 850 px
output_filename: P2-F32.png
title_policy: 내부 전체 제목·그림 코드 금지

문제:
EAP Challenge/Response 왕복과 최종 Access-Accept 전 포트 개방 시점이 지나치게 단순화되었다.

필수 수정:
Supplicant–Authenticator–RADIUS 사이 EAP Challenge/Response 왕복을 표시하고 최종 Access-Accept/EAP-Success 이후 Controlled Port와 VLAN/ACL을 허용.

통합 가이드 세부 지침:
`Supplicant → Authenticator(Switch/AP) → Authentication Server(RADIUS)` 구조에서 다음 순서를 표시한다.

`EAPOL-Start → Identity 요청·응답 → RADIUS Access-Request → Access-Challenge/EAP 응답 왕복 → Access-Accept·EAP-Success → Controlled Port 허용·VLAN/ACL 적용`

기본 프롬프트:
정보보안기사 시험 대비용 한국어 교육 도식이다.
원본의 학습 목적만 유지하고, 아래에 지정한 정확한 구조와 허용 텍스트로 새로 그린다.
흰 배경, 네이비·틸·밝은 회색 중심, 위험·오류만 빨강, 단순한 벡터 스타일.
화살표는 실제 데이터·제어 흐름에만 사용하고 방향을 정확히 맞춘다.
허용 텍스트 외의 문구, 워터마크, 프롬프트 문장, 파일명, 가짜 수식, 의미 없는 약어를 넣지 않는다.
출력 크기와 제목 정책은 해당 코드의 매니페스트를 따른다.

공통 네거티브:
no watermark, no prompt text, no placeholder text, no pseudo-Korean,
no misspelled Korean, no duplicate labels, no invented formula,
no tiny text, no decorative arrows, no gradient background,
no photorealistic style, no file name, no version string
```

## [A] P2-F41 · TCP·UDP 스캔 응답 매트릭스 · 전면 재생성

```text
[A] P2-F41 · TCP·UDP 스캔 응답 매트릭스 · 전면 재생성

input_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\01_전면재생성\Part2\P2-F41.png
output_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\03_수정완료\Part2\P2-F41.png
canvas: 1600 x 850 px
output_filename: P2-F41.png
title_policy: 내부 전체 제목·그림 코드 금지

문제:
ACK Scan을 open/closed 판별처럼 보이게 하여 스캔 응답 의미가 틀렸다.

필수 수정:
ACK Scan은 open/closed 구분 불가, RST=unfiltered, 무응답/ICMP=filtered로 표시. SYN/Connect/FIN-NULL-Xmas/UDP 결과도 표준 응답으로 정리.

통합 가이드 세부 지침:
| 스캔 | Open | Closed | Filtered/기타 |
|---|---|---|---|
| SYN | SYN/ACK | RST | 무응답 또는 ICMP |
| Connect | Handshake 성공 | RST | Timeout/ICMP |
| FIN/NULL/Xmas | 무응답=`open|filtered` | RST | 모호 가능 |
| ACK | Open/Closed 구분 불가 | Open/Closed 구분 불가 | RST=`unfiltered`, 무응답/ICMP=`filtered` |
| UDP | 응용 응답 | ICMP Port Unreachable | 무응답=`open|filtered` |

기본 프롬프트:
정보보안기사 시험 대비용 한국어 교육 도식이다.
원본의 학습 목적만 유지하고, 아래에 지정한 정확한 구조와 허용 텍스트로 새로 그린다.
흰 배경, 네이비·틸·밝은 회색 중심, 위험·오류만 빨강, 단순한 벡터 스타일.
화살표는 실제 데이터·제어 흐름에만 사용하고 방향을 정확히 맞춘다.
허용 텍스트 외의 문구, 워터마크, 프롬프트 문장, 파일명, 가짜 수식, 의미 없는 약어를 넣지 않는다.
출력 크기와 제목 정책은 해당 코드의 매니페스트를 따른다.

공통 네거티브:
no watermark, no prompt text, no placeholder text, no pseudo-Korean,
no misspelled Korean, no duplicate labels, no invented formula,
no tiny text, no decorative arrows, no gradient background,
no photorealistic style, no file name, no version string
```

## [A] P2-F51 · 방화벽·DMZ 구축 유형 · 전면 재생성

```text
[A] P2-F51 · 방화벽·DMZ 구축 유형 · 전면 재생성

input_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\01_전면재생성\Part2\P2-F51.png
output_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\03_수정완료\Part2\P2-F51.png
canvas: 1600 x 850 px
output_filename: P2-F51.png
title_policy: 내부 전체 제목·그림 코드 금지

문제:
Dual-Homed·Screened Host·Screened Subnet의 배치 구조가 표준 개념과 다르다.

필수 수정:
Dual-Homed Host=두 NIC Bastion/Proxy, Screened Host=Screening Router+내부측 Bastion, Screened Subnet=두 필터링 지점이 DMZ 생성으로 재구성.

통합 가이드 세부 지침:
- `Dual-Homed Host`: 두 NIC를 가진 Bastion/Proxy가 외부와 내부 사이에 위치, 직접 라우팅 제한.
- `Screened Host`: Screening Router 뒤 내부측 Bastion Host, 외부 접근은 Bastion으로 제한.
- `Screened Subnet`: 두 필터링 지점 또는 3-leg 방화벽이 DMZ를 만들고 공개 서버를 DMZ에 배치.

기본 프롬프트:
정보보안기사 시험 대비용 한국어 교육 도식이다.
원본의 학습 목적만 유지하고, 아래에 지정한 정확한 구조와 허용 텍스트로 새로 그린다.
흰 배경, 네이비·틸·밝은 회색 중심, 위험·오류만 빨강, 단순한 벡터 스타일.
화살표는 실제 데이터·제어 흐름에만 사용하고 방향을 정확히 맞춘다.
허용 텍스트 외의 문구, 워터마크, 프롬프트 문장, 파일명, 가짜 수식, 의미 없는 약어를 넣지 않는다.
출력 크기와 제목 정책은 해당 코드의 매니페스트를 따른다.

공통 네거티브:
no watermark, no prompt text, no placeholder text, no pseudo-Korean,
no misspelled Korean, no duplicate labels, no invented formula,
no tiny text, no decorative arrows, no gradient background,
no photorealistic style, no file name, no version string
```

## [A] P2-F61 · TLS 1.3 핸드셰이크와 보호 범위 · 전면 재생성

```text
[A] P2-F61 · TLS 1.3 핸드셰이크와 보호 범위 · 전면 재생성

input_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\01_전면재생성\Part2\P2-F61.png
output_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\03_수정완료\Part2\P2-F61.png
canvas: 1600 x 850 px
output_filename: P2-F61.png
title_policy: 내부 전체 제목·그림 코드 금지

문제:
TLS 1.3의 EncryptedExtensions와 ServerHello 이후 핸드셰이크 보호 시작점이 빠졌다.

필수 수정:
ClientHello→ServerHello 후 핸드셰이크 키 보호 시작, EncryptedExtensions→Certificate→CertificateVerify→Server Finished→Client Finished→Application Data 순서.

통합 가이드 세부 지침:
`ClientHello → ServerHello → [후속 핸드셰이크 보호 시작] → EncryptedExtensions → Certificate → CertificateVerify → Server Finished → Client Finished → Application Data`

- 인증서 개인키는 CertificateVerify 서명에 사용된다.
- 대량 응용데이터를 인증서 RSA 키로 직접 암호화하지 않는다.

기본 프롬프트:
정보보안기사 시험 대비용 한국어 교육 도식이다.
원본의 학습 목적만 유지하고, 아래에 지정한 정확한 구조와 허용 텍스트로 새로 그린다.
흰 배경, 네이비·틸·밝은 회색 중심, 위험·오류만 빨강, 단순한 벡터 스타일.
화살표는 실제 데이터·제어 흐름에만 사용하고 방향을 정확히 맞춘다.
허용 텍스트 외의 문구, 워터마크, 프롬프트 문장, 파일명, 가짜 수식, 의미 없는 약어를 넣지 않는다.
출력 크기와 제목 정책은 해당 코드의 매니페스트를 따른다.

공통 네거티브:
no watermark, no prompt text, no placeholder text, no pseudo-Korean,
no misspelled Korean, no duplicate labels, no invented formula,
no tiny text, no decorative arrows, no gradient background,
no photorealistic style, no file name, no version string
```

## [A] P2-F62 · SSH 연결과 안전한 원격관리 · 전면 재생성

```text
[A] P2-F62 · SSH 연결과 안전한 원격관리 · 전면 재생성

input_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\01_전면재생성\Part2\P2-F62.png
output_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\03_수정완료\Part2\P2-F62.png
canvas: 1600 x 850 px
output_filename: P2-F62.png
title_policy: 내부 전체 제목·그림 코드 금지

문제:
SSH 호스트키 검증이 키 교환보다 먼저 일어나는 것으로 그려져 순서가 틀렸다.

필수 수정:
TCP 연결→버전 교환→KEX와 서버 Host Key 서명/known_hosts 검증→암호화 전송 성립→사용자 인증→채널/셸/포워딩 순서로 재구성.

통합 가이드 세부 지침:
`TCP 연결 → 버전 교환 → 알고리즘 협상·KEX → 서버 Host Key 서명과 known_hosts/CA 검증 → 암호화 전송 성립 → 사용자 인증 → 채널·셸·포트포워딩`

사용자 인증은 호스트 인증 뒤에 수행한다. 하단에 MFA·Jump Server·키 보호·세션 기록을 둔다.

기본 프롬프트:
정보보안기사 시험 대비용 한국어 교육 도식이다.
원본의 학습 목적만 유지하고, 아래에 지정한 정확한 구조와 허용 텍스트로 새로 그린다.
흰 배경, 네이비·틸·밝은 회색 중심, 위험·오류만 빨강, 단순한 벡터 스타일.
화살표는 실제 데이터·제어 흐름에만 사용하고 방향을 정확히 맞춘다.
허용 텍스트 외의 문구, 워터마크, 프롬프트 문장, 파일명, 가짜 수식, 의미 없는 약어를 넣지 않는다.
출력 크기와 제목 정책은 해당 코드의 매니페스트를 따른다.

공통 네거티브:
no watermark, no prompt text, no placeholder text, no pseudo-Korean,
no misspelled Korean, no duplicate labels, no invented formula,
no tiny text, no decorative arrows, no gradient background,
no photorealistic style, no file name, no version string
```

## [A] P2-F65 · IKE 단계와 VPN 유형 · 전면 재생성

```text
[A] P2-F65 · IKE 단계와 VPN 유형 · 전면 재생성

input_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\01_전면재생성\Part2\P2-F65.png
output_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\03_수정완료\Part2\P2-F65.png
canvas: 1600 x 850 px
output_filename: P2-F65.png
title_policy: 내부 전체 제목·그림 코드 금지

문제:
IKEv2 왕복 구조에 IKEv1 역사 설명이 섞여 있다.

필수 수정:
IKE_SA_INIT Request/Response, IKE_AUTH Request/Response, CREATE_CHILD_SA로 재구성. IKEv1 `ISAKMP+Oakley/SKEME` 문구는 본도식에서 제거.

통합 가이드 세부 지침:
- `IKE_SA_INIT Request/Response`: 제안, DH, Nonce
- `IKE_AUTH Request/Response`: ID, AUTH, Traffic Selector, 첫 Child SA
- `CREATE_CHILD_SA`: 추가 SA·재키잉
- 오른쪽: Site-to-Site IPsec, Remote Access IPsec, SSL/TLS VPN
- IKEv1의 `ISAKMP+Oakley/SKEME` 문구는 제거한다.

기본 프롬프트:
정보보안기사 시험 대비용 한국어 교육 도식이다.
원본의 학습 목적만 유지하고, 아래에 지정한 정확한 구조와 허용 텍스트로 새로 그린다.
흰 배경, 네이비·틸·밝은 회색 중심, 위험·오류만 빨강, 단순한 벡터 스타일.
화살표는 실제 데이터·제어 흐름에만 사용하고 방향을 정확히 맞춘다.
허용 텍스트 외의 문구, 워터마크, 프롬프트 문장, 파일명, 가짜 수식, 의미 없는 약어를 넣지 않는다.
출력 크기와 제목 정책은 해당 코드의 매니페스트를 따른다.

공통 네거티브:
no watermark, no prompt text, no placeholder text, no pseudo-Korean,
no misspelled Korean, no duplicate labels, no invented formula,
no tiny text, no decorative arrows, no gradient background,
no photorealistic style, no file name, no version string
```

## [A] P3-F04 · FTP Active와 Passive 모드 · 전면 재생성

```text
[A] P3-F04 · FTP Active와 Passive 모드 · 전면 재생성

input_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\01_전면재생성\Part3\P3-F04.png
output_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\03_수정완료\Part3\P3-F04.png
canvas: 1800 x 1004 px
output_filename: P3-F04.png
title_policy: 내부 전체 제목·그림 코드 금지

문제:
Active/Passive 데이터 연결 방향과 NAT·방화벽 설명이 깨지고 혼재한다.

필수 수정:
제어 연결은 양 모드 모두 Client→Server TCP 21. Active는 Server TCP 20→Client 지정 포트, Passive는 Client→Server 고포트. NAT/방화벽 주의점 분리.

통합 가이드 세부 지침:
- 양 모드 모두 제어 연결은 Client→Server TCP 21.
- Active: Client가 PORT/EPRT로 포트를 알리고 Server가 전통적으로 TCP 20에서 Client 지정 포트로 데이터 연결 시작.
- Passive: Client가 PASV/EPSV 요청, Server가 고포트를 알리고 Client가 그 포트로 연결.
- Active는 클라이언트 인바운드/NAT, Passive는 서버 고포트 범위/방화벽을 주의점으로 분리한다.

기본 프롬프트:
정보보안기사 시험 대비용 한국어 교육 도식이다.
원본의 학습 목적만 유지하고, 아래에 지정한 정확한 구조와 허용 텍스트로 새로 그린다.
흰 배경, 네이비·틸·밝은 회색 중심, 위험·오류만 빨강, 단순한 벡터 스타일.
화살표는 실제 데이터·제어 흐름에만 사용하고 방향을 정확히 맞춘다.
허용 텍스트 외의 문구, 워터마크, 프롬프트 문장, 파일명, 가짜 수식, 의미 없는 약어를 넣지 않는다.
출력 크기와 제목 정책은 해당 코드의 매니페스트를 따른다.

공통 네거티브:
no watermark, no prompt text, no placeholder text, no pseudo-Korean,
no misspelled Korean, no duplicate labels, no invented formula,
no tiny text, no decorative arrows, no gradient background,
no photorealistic style, no file name, no version string
```

## [A] P3-F05 · FTP 명령과 응답 코드 흐름 · 전면 재생성

```text
[A] P3-F05 · FTP 명령과 응답 코드 흐름 · 전면 재생성

input_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\01_전면재생성\Part3\P3-F05.png
output_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\03_수정완료\Part3\P3-F05.png
canvas: 1800 x 1004 px
output_filename: P3-F05.png
title_policy: 내부 전체 제목·그림 코드 금지

문제:
FTP 명령·응답 화살표 방향과 전송 완료 응답 위치가 틀렸다.

필수 수정:
USER/PASS/PWD/CWD/LIST/RETR/STOR/QUIT는 C→S, 응답은 S→C. LIST/RETR/STOR의 별도 데이터 연결과 1xx preliminary, 226 final completion을 분리.

통합 가이드 세부 지침:
- USER/PASS/PWD/CWD/LIST/RETR/STOR/QUIT는 Client→Server.
- 응답은 Server→Client. `1xx=preliminary`, `2xx=success`, `3xx=additional input`, `4xx=temporary failure`, `5xx=permanent failure`.
- LIST/RETR/STOR가 별도 데이터 연결을 만들고, 전송 뒤 `226 Transfer complete` 같은 최종 2xx를 보낸다.

기본 프롬프트:
정보보안기사 시험 대비용 한국어 교육 도식이다.
원본의 학습 목적만 유지하고, 아래에 지정한 정확한 구조와 허용 텍스트로 새로 그린다.
흰 배경, 네이비·틸·밝은 회색 중심, 위험·오류만 빨강, 단순한 벡터 스타일.
화살표는 실제 데이터·제어 흐름에만 사용하고 방향을 정확히 맞춘다.
허용 텍스트 외의 문구, 워터마크, 프롬프트 문장, 파일명, 가짜 수식, 의미 없는 약어를 넣지 않는다.
출력 크기와 제목 정책은 해당 코드의 매니페스트를 따른다.

공통 네거티브:
no watermark, no prompt text, no placeholder text, no pseudo-Korean,
no misspelled Korean, no duplicate labels, no invented formula,
no tiny text, no decorative arrows, no gradient background,
no photorealistic style, no file name, no version string
```

## [A] P3-F09 · SMTP 대화와 포트 · 전면 재생성

```text
[A] P3-F09 · SMTP 대화와 포트 · 전면 재생성

input_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\01_전면재생성\Part3\P3-F09.png
output_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\03_수정완료\Part3\P3-F09.png
canvas: 1800 x 1004 px
output_filename: P3-F09.png
title_policy: 내부 전체 제목·그림 코드 금지

문제:
SMTP 명령·응답 방향과 STARTTLS 위치가 잘못 읽히며 제목도 깨졌다.

필수 수정:
EHLO C→S, 250 S→C, STARTTLS C→S, TLS 협상 후 MAIL FROM/RCPT TO/DATA/본문/`.` C→S, 250 S→C, QUIT C→S, 221 S→C. 25/587/465 역할 분리.

통합 가이드 세부 지침:
`EHLO → 250 capabilities → STARTTLS → TLS 협상 → MAIL FROM → RCPT TO → DATA → 본문·마침표 → 250 → QUIT → 221`

포트는 `25=서버 간 릴레이`, `587=인증된 Submission/STARTTLS`, `465=연결 시작부터 TLS Submission`으로 분리한다.

기본 프롬프트:
정보보안기사 시험 대비용 한국어 교육 도식이다.
원본의 학습 목적만 유지하고, 아래에 지정한 정확한 구조와 허용 텍스트로 새로 그린다.
흰 배경, 네이비·틸·밝은 회색 중심, 위험·오류만 빨강, 단순한 벡터 스타일.
화살표는 실제 데이터·제어 흐름에만 사용하고 방향을 정확히 맞춘다.
허용 텍스트 외의 문구, 워터마크, 프롬프트 문장, 파일명, 가짜 수식, 의미 없는 약어를 넣지 않는다.
출력 크기와 제목 정책은 해당 코드의 매니페스트를 따른다.

공통 네거티브:
no watermark, no prompt text, no placeholder text, no pseudo-Korean,
no misspelled Korean, no duplicate labels, no invented formula,
no tiny text, no decorative arrows, no gradient background,
no photorealistic style, no file name, no version string
```

## [A] P3-F11 · MIME 메시지 구조 · 전면 재생성

```text
[A] P3-F11 · MIME 메시지 구조 · 전면 재생성

input_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\01_전면재생성\Part3\P3-F11.png
output_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\03_수정완료\Part3\P3-F11.png
canvas: 1800 x 1004 px
output_filename: P3-F11.png
title_policy: 내부 전체 제목·그림 코드 금지

문제:
MIME 헤더·본문·첨부 예시가 광범위하게 깨져 구조를 신뢰할 수 없다.

필수 수정:
정상 MIME 예시로 재작성: MIME-Version, multipart/mixed boundary, text/plain UTF-8, application/pdf attachment, Content-Disposition, Base64. `Base64는 암호화가 아님` 표시.

통합 가이드 세부 지침:
정상 예시만 사용한다.

- `MIME-Version: 1.0`
- `Content-Type: multipart/mixed; boundary="..."`
- 첫 파트: `text/plain; charset=UTF-8`
- 첨부: `application/pdf`, `Content-Disposition: attachment; filename="report.pdf"`, `Content-Transfer-Encoding: base64`
- 하단: `Base64는 인코딩이며 암호화가 아니다`, `확장자·MIME만 믿지 말고 실제 내용 검사`

기본 프롬프트:
정보보안기사 시험 대비용 한국어 교육 도식이다.
원본의 학습 목적만 유지하고, 아래에 지정한 정확한 구조와 허용 텍스트로 새로 그린다.
흰 배경, 네이비·틸·밝은 회색 중심, 위험·오류만 빨강, 단순한 벡터 스타일.
화살표는 실제 데이터·제어 흐름에만 사용하고 방향을 정확히 맞춘다.
허용 텍스트 외의 문구, 워터마크, 프롬프트 문장, 파일명, 가짜 수식, 의미 없는 약어를 넣지 않는다.
출력 크기와 제목 정책은 해당 코드의 매니페스트를 따른다.

공통 네거티브:
no watermark, no prompt text, no placeholder text, no pseudo-Korean,
no misspelled Korean, no duplicate labels, no invented formula,
no tiny text, no decorative arrows, no gradient background,
no photorealistic style, no file name, no version string
```

## [A] P3-F12 · 메일 헤더 추적과 Authentication-Results · 전면 재생성

```text
[A] P3-F12 · 메일 헤더 추적과 Authentication-Results · 전면 재생성

input_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\01_전면재생성\Part3\P3-F12.png
output_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\03_수정완료\Part3\P3-F12.png
canvas: 1800 x 1004 px
output_filename: P3-F12.png
title_policy: 내부 전체 제목·그림 코드 금지

문제:
Received·주소·인증결과가 깨지고 SPF/DKIM/DMARC 결과가 서로 모순된다.

필수 수정:
Received는 위쪽에 누적되고 아래→위로 추적. Header From·Return-Path·Message-ID·Authentication-Results를 분리하고 일관된 `spf=pass`, `dkim=pass`, `dmarc=pass` 예시 사용.

통합 가이드 세부 지침:
- 각 MTA는 Received를 위쪽에 추가하며 경로는 일반적으로 아래→위로 읽는다.
- Header From, Return-Path(Envelope From), Reply-To, Message-ID, Authentication-Results를 구분한다.
- 일관된 예시: `spf=pass`, `dkim=pass`, `dmarc=pass`; DMARC 근거는 SPF 정렬 또는 DKIM 정렬.

기본 프롬프트:
정보보안기사 시험 대비용 한국어 교육 도식이다.
원본의 학습 목적만 유지하고, 아래에 지정한 정확한 구조와 허용 텍스트로 새로 그린다.
흰 배경, 네이비·틸·밝은 회색 중심, 위험·오류만 빨강, 단순한 벡터 스타일.
화살표는 실제 데이터·제어 흐름에만 사용하고 방향을 정확히 맞춘다.
허용 텍스트 외의 문구, 워터마크, 프롬프트 문장, 파일명, 가짜 수식, 의미 없는 약어를 넣지 않는다.
출력 크기와 제목 정책은 해당 코드의 매니페스트를 따른다.

공통 네거티브:
no watermark, no prompt text, no placeholder text, no pseudo-Korean,
no misspelled Korean, no duplicate labels, no invented formula,
no tiny text, no decorative arrows, no gradient background,
no photorealistic style, no file name, no version string
```

## [A] P3-F14 · DKIM 서명과 검증 · 전면 재생성

```text
[A] P3-F14 · DKIM 서명과 검증 · 전면 재생성

input_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\01_전면재생성\Part3\P3-F14.png
output_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\03_수정완료\Part3\P3-F14.png
canvas: 1800 x 1004 px
output_filename: P3-F14.png
title_policy: 내부 전체 제목·그림 코드 금지

문제:
DKIM 공개키·해시·서명 검증 흐름이 뒤섞여 역할과 방향이 틀렸다.

필수 수정:
발신 MTA가 선택 헤더·본문을 정규화/해시하고 도메인 개인키로 서명. 수신자는 `selector._domainkey` 공개키를 DNS에서 받아 동일 데이터의 서명과 body hash를 검증.

통합 가이드 세부 지침:
- 발신 MTA: 선택 헤더·본문 정규화 → body hash → 도메인 개인키로 서명 → DKIM-Signature(d=, s=, bh=, b=).
- DNS: `selector._domainkey.example`에 공개키 TXT.
- 수신 MTA: DNS 공개키 조회 → 동일 정규화·해시 → 서명과 body hash 검증.
- 개인키는 DNS에 두지 않고, 공개키가 해시를 생성하는 것처럼 그리지 않는다.

기본 프롬프트:
정보보안기사 시험 대비용 한국어 교육 도식이다.
원본의 학습 목적만 유지하고, 아래에 지정한 정확한 구조와 허용 텍스트로 새로 그린다.
흰 배경, 네이비·틸·밝은 회색 중심, 위험·오류만 빨강, 단순한 벡터 스타일.
화살표는 실제 데이터·제어 흐름에만 사용하고 방향을 정확히 맞춘다.
허용 텍스트 외의 문구, 워터마크, 프롬프트 문장, 파일명, 가짜 수식, 의미 없는 약어를 넣지 않는다.
출력 크기와 제목 정책은 해당 코드의 매니페스트를 따른다.

공통 네거티브:
no watermark, no prompt text, no placeholder text, no pseudo-Korean,
no misspelled Korean, no duplicate labels, no invented formula,
no tiny text, no decorative arrows, no gradient background,
no photorealistic style, no file name, no version string
```

## [A] P3-F15 · DMARC 정렬·정책·보고 · 전면 재생성

```text
[A] P3-F15 · DMARC 정렬·정책·보고 · 전면 재생성

input_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\01_전면재생성\Part3\P3-F15.png
output_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\03_수정완료\Part3\P3-F15.png
canvas: 1800 x 1004 px
output_filename: P3-F15.png
title_policy: 내부 전체 제목·그림 코드 금지

문제:
DMARC 판정이 SPF와 DKIM을 모두 요구하는 것처럼 보이며 한글 손상이 광범위하다.

필수 수정:
DMARC 통과 조건을 `(SPF pass AND aligned) OR (DKIM pass AND aligned)`로 표시. Header From 정렬, p=none/quarantine/reject, 보고를 분리.

통합 가이드 세부 지침:
중앙에 Header From을 두고 두 분기를 OR로 결합한다.

`(SPF pass AND SPF authenticated domain aligned) OR (DKIM pass AND d= aligned) → DMARC pass`

오른쪽에 `p=none`, `quarantine`, `reject`, 집계/포렌식 보고를 별도 표시한다.

기본 프롬프트:
정보보안기사 시험 대비용 한국어 교육 도식이다.
원본의 학습 목적만 유지하고, 아래에 지정한 정확한 구조와 허용 텍스트로 새로 그린다.
흰 배경, 네이비·틸·밝은 회색 중심, 위험·오류만 빨강, 단순한 벡터 스타일.
화살표는 실제 데이터·제어 흐름에만 사용하고 방향을 정확히 맞춘다.
허용 텍스트 외의 문구, 워터마크, 프롬프트 문장, 파일명, 가짜 수식, 의미 없는 약어를 넣지 않는다.
출력 크기와 제목 정책은 해당 코드의 매니페스트를 따른다.

공통 네거티브:
no watermark, no prompt text, no placeholder text, no pseudo-Korean,
no misspelled Korean, no duplicate labels, no invented formula,
no tiny text, no decorative arrows, no gradient background,
no photorealistic style, no file name, no version string
```

## [A] P3-F19 · URL과 HTTP 요청·응답 구조 · 전면 재생성

```text
[A] P3-F19 · URL과 HTTP 요청·응답 구조 · 전면 재생성

input_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\01_전면재생성\Part3\P3-F19.png
output_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\03_수정완료\Part3\P3-F19.png
canvas: 1800 x 1004 px
output_filename: P3-F19.png
title_policy: 내부 전체 제목·그림 코드 금지

문제:
URL 구성요소와 HTTP 예시가 깨지고 path·fragment 설명이 잘못 읽힌다.

필수 수정:
URL을 scheme/host/port/path/query/fragment로 정확히 분해하고 fragment는 서버에 전송되지 않음을 표시. 정상 HTTP 요청·응답 예시로 교체.

통합 가이드 세부 지침:
URL 예: `https://www.example.com:8443/orders/123?view=detail#history`

- scheme=https, host=www.example.com, port=8443, path=/orders/123, query=view=detail, fragment=history
- `fragment는 일반적으로 HTTP 요청으로 서버에 전송되지 않음`
- 정상 GET 요청과 200 OK 응답 예시를 사용한다.

기본 프롬프트:
정보보안기사 시험 대비용 한국어 교육 도식이다.
원본의 학습 목적만 유지하고, 아래에 지정한 정확한 구조와 허용 텍스트로 새로 그린다.
흰 배경, 네이비·틸·밝은 회색 중심, 위험·오류만 빨강, 단순한 벡터 스타일.
화살표는 실제 데이터·제어 흐름에만 사용하고 방향을 정확히 맞춘다.
허용 텍스트 외의 문구, 워터마크, 프롬프트 문장, 파일명, 가짜 수식, 의미 없는 약어를 넣지 않는다.
출력 크기와 제목 정책은 해당 코드의 매니페스트를 따른다.

공통 네거티브:
no watermark, no prompt text, no placeholder text, no pseudo-Korean,
no misspelled Korean, no duplicate labels, no invented formula,
no tiny text, no decorative arrows, no gradient background,
no photorealistic style, no file name, no version string
```

## [A] P3-F25 · 서버 인증서 검증과 신뢰사슬 · 전면 재생성

```text
[A] P3-F25 · 서버 인증서 검증과 신뢰사슬 · 전면 재생성

input_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\01_전면재생성\Part3\P3-F25.png
output_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\03_수정완료\Part3\P3-F25.png
canvas: 1800 x 1004 px
output_filename: P3-F25.png
title_policy: 내부 전체 제목·그림 코드 금지

문제:
서버 인증서를 Root CA처럼 보이게 하며 체인·호스트명·폐기 검증 구조가 혼재한다.

필수 수정:
서버 Leaf+Intermediate→로컬 Root Trust Anchor 체인으로 표시하고 서명·유효기간·SAN hostname·KU/EKU·Basic Constraints·폐기상태를 검증.

통합 가이드 세부 지침:
- Server는 Leaf와 Intermediate를 제시한다.
- Client는 로컬 Trust Store의 Root까지 체인을 구성한다.
- 검증: 서명사슬, 유효기간, SAN hostname, KU/EKU, Basic Constraints, 경로 길이, 폐기상태.
- 서버 Leaf 인증서를 Root CA로 표시하지 않는다.

기본 프롬프트:
정보보안기사 시험 대비용 한국어 교육 도식이다.
원본의 학습 목적만 유지하고, 아래에 지정한 정확한 구조와 허용 텍스트로 새로 그린다.
흰 배경, 네이비·틸·밝은 회색 중심, 위험·오류만 빨강, 단순한 벡터 스타일.
화살표는 실제 데이터·제어 흐름에만 사용하고 방향을 정확히 맞춘다.
허용 텍스트 외의 문구, 워터마크, 프롬프트 문장, 파일명, 가짜 수식, 의미 없는 약어를 넣지 않는다.
출력 크기와 제목 정책은 해당 코드의 매니페스트를 따른다.

공통 네거티브:
no watermark, no prompt text, no placeholder text, no pseudo-Korean,
no misspelled Korean, no duplicate labels, no invented formula,
no tiny text, no decorative arrows, no gradient background,
no photorealistic style, no file name, no version string
```

## [A] P3-F33 · Broken Access Control과 IDOR · 전면 재생성

```text
[A] P3-F33 · Broken Access Control과 IDOR · 전면 재생성

input_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\01_전면재생성\Part3\P3-F33.png
output_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\03_수정완료\Part3\P3-F33.png
canvas: 1800 x 1004 px
output_filename: P3-F33.png
title_policy: 내부 전체 제목·그림 코드 금지

문제:
제목과 본문이 광범위하게 깨져 서버측 객체 인가 원리가 전달되지 않는다.

필수 수정:
User A의 자기 객체 요청은 Allow, 타 사용자 객체 ID 변경 요청은 서버측 소유권·역할·테넌트 검사 후 Deny. UUID·버튼 숨김은 인가 대체가 아님 표시.

통합 가이드 세부 지침:
- 정상: User A가 자기 주문 `/orders/123` 요청 → 사용자·테넌트·소유권·역할 검사 → Allow.
- 공격: User A가 `/orders/456`으로 변경 → User B 소유 확인 → Deny.
- `모든 요청의 서버측 객체·기능·필드 인가`, `Deny by Default`, `감사` 표시.
- UUID·버튼 숨김은 인가 대체가 아니다.

기본 프롬프트:
정보보안기사 시험 대비용 한국어 교육 도식이다.
원본의 학습 목적만 유지하고, 아래에 지정한 정확한 구조와 허용 텍스트로 새로 그린다.
흰 배경, 네이비·틸·밝은 회색 중심, 위험·오류만 빨강, 단순한 벡터 스타일.
화살표는 실제 데이터·제어 흐름에만 사용하고 방향을 정확히 맞춘다.
허용 텍스트 외의 문구, 워터마크, 프롬프트 문장, 파일명, 가짜 수식, 의미 없는 약어를 넣지 않는다.
출력 크기와 제목 정책은 해당 코드의 매니페스트를 따른다.

공통 네거티브:
no watermark, no prompt text, no placeholder text, no pseudo-Korean,
no misspelled Korean, no duplicate labels, no invented formula,
no tiny text, no decorative arrows, no gradient background,
no photorealistic style, no file name, no version string
```

## [A] P3-F47 · DNS 레코드 유형 · 전면 재생성

```text
[A] P3-F47 · DNS 레코드 유형 · 전면 재생성

input_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\01_전면재생성\Part3\P3-F47.png
output_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\03_수정완료\Part3\P3-F47.png
canvas: 1800 x 1004 px
output_filename: P3-F47.png
title_policy: 내부 전체 제목·그림 코드 금지

문제:
AAAA를 별칭처럼 표시하고 NS를 중복하는 등 레코드 매핑이 틀렸다.

필수 수정:
A/AAAA/CNAME/MX/NS/SOA/TXT/PTR/SRV의 정확한 이름→값 매핑 표로 재구성.

통합 가이드 세부 지침:
`A=이름→IPv4`, `AAAA=이름→IPv6`, `CNAME=별칭→정규 이름`, `MX=메일 서버+우선순위`, `NS=권한 네임서버`, `SOA=Zone 기본정보·Serial`, `TXT=정책·검증`, `PTR=IP→이름`, `SRV=서비스→대상·포트·우선순위·가중치`.

기본 프롬프트:
정보보안기사 시험 대비용 한국어 교육 도식이다.
원본의 학습 목적만 유지하고, 아래에 지정한 정확한 구조와 허용 텍스트로 새로 그린다.
흰 배경, 네이비·틸·밝은 회색 중심, 위험·오류만 빨강, 단순한 벡터 스타일.
화살표는 실제 데이터·제어 흐름에만 사용하고 방향을 정확히 맞춘다.
허용 텍스트 외의 문구, 워터마크, 프롬프트 문장, 파일명, 가짜 수식, 의미 없는 약어를 넣지 않는다.
출력 크기와 제목 정책은 해당 코드의 매니페스트를 따른다.

공통 네거티브:
no watermark, no prompt text, no placeholder text, no pseudo-Korean,
no misspelled Korean, no duplicate labels, no invented formula,
no tiny text, no decorative arrows, no gradient background,
no photorealistic style, no file name, no version string
```

## [A] P3-F49 · DNS 공격과 대응 지도 · 전면 재생성

```text
[A] P3-F49 · DNS 공격과 대응 지도 · 전면 재생성

input_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\01_전면재생성\Part3\P3-F49.png
output_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\03_수정완료\Part3\P3-F49.png
canvas: 1800 x 1004 px
output_filename: P3-F49.png
title_policy: 내부 전체 제목·그림 코드 금지

문제:
DNSSEC·BCP38·터널링·증폭 대응의 연결이 잘못 매핑되었다.

필수 수정:
Poisoning→TXID/Port randomization·Bailiwick·DNSSEC, Amplification→Open resolver 제거·RRL·BCP38, Tunneling→Resolver egress·행위분석, Hijacking→Registrar MFA/Lock으로 재매핑.

통합 가이드 세부 지침:
- Poisoning/Spoofing → TXID·Source Port 무작위화, Bailiwick, DNSSEC
- Amplification → Open Resolver 제거, RRL, BCP38
- Tunneling → 지정 Resolver Egress, 긴·고엔트로피 이름/NXDOMAIN/빈도 분석
- Hijacking/Domain Shadowing → Registrar MFA·Lock, DNS 변경 알림

기본 프롬프트:
정보보안기사 시험 대비용 한국어 교육 도식이다.
원본의 학습 목적만 유지하고, 아래에 지정한 정확한 구조와 허용 텍스트로 새로 그린다.
흰 배경, 네이비·틸·밝은 회색 중심, 위험·오류만 빨강, 단순한 벡터 스타일.
화살표는 실제 데이터·제어 흐름에만 사용하고 방향을 정확히 맞춘다.
허용 텍스트 외의 문구, 워터마크, 프롬프트 문장, 파일명, 가짜 수식, 의미 없는 약어를 넣지 않는다.
출력 크기와 제목 정책은 해당 코드의 매니페스트를 따른다.

공통 네거티브:
no watermark, no prompt text, no placeholder text, no pseudo-Korean,
no misspelled Korean, no duplicate labels, no invented formula,
no tiny text, no decorative arrows, no gradient background,
no photorealistic style, no file name, no version string
```

## [A] P3-F50 · DNSSEC 신뢰사슬 · 전면 재생성

```text
[A] P3-F50 · DNSSEC 신뢰사슬 · 전면 재생성

input_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\01_전면재생성\Part3\P3-F50.png
output_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\03_수정완료\Part3\P3-F50.png
canvas: 1800 x 1004 px
output_filename: P3-F50.png
title_policy: 내부 전체 제목·그림 코드 금지

문제:
부모 존의 DS 위치와 Root Trust Anchor 검증 사슬이 틀렸다.

필수 수정:
Root Trust Anchor→Root DNSKEY 검증, 부모 Zone의 DS→자식 DNSKEY/KSK, 자식 RRset의 RRSIG 검증 흐름으로 재구성. NSEC/NSEC3는 인증된 부재.

통합 가이드 세부 지침:
`Root Trust Anchor → Root DNSKEY → 부모 Zone의 DS → 자식 DNSKEY/KSK → RRset의 RRSIG`

- DS는 자식 Zone이 아니라 부모 Zone에 존재한다.
- NSEC/NSEC3는 인증된 부재 증명.
- DNSSEC는 출처 인증·무결성이지 기밀성이 아니다.

기본 프롬프트:
정보보안기사 시험 대비용 한국어 교육 도식이다.
원본의 학습 목적만 유지하고, 아래에 지정한 정확한 구조와 허용 텍스트로 새로 그린다.
흰 배경, 네이비·틸·밝은 회색 중심, 위험·오류만 빨강, 단순한 벡터 스타일.
화살표는 실제 데이터·제어 흐름에만 사용하고 방향을 정확히 맞춘다.
허용 텍스트 외의 문구, 워터마크, 프롬프트 문장, 파일명, 가짜 수식, 의미 없는 약어를 넣지 않는다.
출력 크기와 제목 정책은 해당 코드의 매니페스트를 따른다.

공통 네거티브:
no watermark, no prompt text, no placeholder text, no pseudo-Korean,
no misspelled Korean, no duplicate labels, no invented formula,
no tiny text, no decorative arrows, no gradient background,
no photorealistic style, no file name, no version string
```

## [A] P3-F54 · DB 암호화와 키 관리 · 전면 재생성

```text
[A] P3-F54 · DB 암호화와 키 관리 · 전면 재생성

input_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\01_전면재생성\Part3\P3-F54.png
output_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\03_수정완료\Part3\P3-F54.png
canvas: 1800 x 1004 px
output_filename: P3-F54.png
title_policy: 내부 전체 제목·그림 코드 금지

문제:
DB 암호화 계층과 키 보관·역할 설명이 깨지고 혼재한다.

필수 수정:
전송 TLS, 저장 TDE, 열/필드 암호화, 애플리케이션 계층 암호화, KMS/HSM 분리를 계층화. 암호화가 SQLi·권한 오남용을 자동 차단하지 않음을 표시.

통합 가이드 세부 지침:
- 전송 TLS
- TDE: 데이터파일·로그·백업 저장매체 보호
- 열/필드 암호화
- 애플리케이션 계층 암호화
- KMS/HSM과 키 생성·회전·백업·폐기, 데이터 접근권한과 키 접근권한 분리
- `암호화는 SQL Injection·권한 오남용을 자동 차단하지 않음`

기본 프롬프트:
정보보안기사 시험 대비용 한국어 교육 도식이다.
원본의 학습 목적만 유지하고, 아래에 지정한 정확한 구조와 허용 텍스트로 새로 그린다.
흰 배경, 네이비·틸·밝은 회색 중심, 위험·오류만 빨강, 단순한 벡터 스타일.
화살표는 실제 데이터·제어 흐름에만 사용하고 방향을 정확히 맞춘다.
허용 텍스트 외의 문구, 워터마크, 프롬프트 문장, 파일명, 가짜 수식, 의미 없는 약어를 넣지 않는다.
출력 크기와 제목 정책은 해당 코드의 매니페스트를 따른다.

공통 네거티브:
no watermark, no prompt text, no placeholder text, no pseudo-Korean,
no misspelled Korean, no duplicate labels, no invented formula,
no tiny text, no decorative arrows, no gradient background,
no photorealistic style, no file name, no version string
```

## [A] P3-F56 · 전자상거래 신뢰모델과 보안요소 · 전면 재생성

```text
[A] P3-F56 · 전자상거래 신뢰모델과 보안요소 · 전면 재생성

input_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\01_전면재생성\Part3\P3-F56.png
output_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\03_수정완료\Part3\P3-F56.png
canvas: 1800 x 1004 px
output_filename: P3-F56.png
title_policy: 내부 전체 제목·그림 코드 금지

문제:
구매자·가맹점·게이트웨이·금융기관의 정보 흐름과 역할이 깨졌다.

필수 수정:
구매자·가맹점·PG/VAN/Payment Gateway·발급사·매입사/은행·CA를 분리하고 주문·지급·승인·정산 흐름 및 보안요소를 재구성.

통합 가이드 세부 지침:
참여자: 구매자, 가맹점, PG/VAN·Payment Gateway, 발급사, 매입사·은행, CA.

흐름은 주문정보, 지급정보·승인요청, 승인·정산, 인증서·신뢰로 분리하고 기밀성·무결성·인증·부인방지·가용성·개인정보 최소처리를 배치한다.

기본 프롬프트:
정보보안기사 시험 대비용 한국어 교육 도식이다.
원본의 학습 목적만 유지하고, 아래에 지정한 정확한 구조와 허용 텍스트로 새로 그린다.
흰 배경, 네이비·틸·밝은 회색 중심, 위험·오류만 빨강, 단순한 벡터 스타일.
화살표는 실제 데이터·제어 흐름에만 사용하고 방향을 정확히 맞춘다.
허용 텍스트 외의 문구, 워터마크, 프롬프트 문장, 파일명, 가짜 수식, 의미 없는 약어를 넣지 않는다.
출력 크기와 제목 정책은 해당 코드의 매니페스트를 따른다.

공통 네거티브:
no watermark, no prompt text, no placeholder text, no pseudo-Korean,
no misspelled Korean, no duplicate labels, no invented formula,
no tiny text, no decorative arrows, no gradient background,
no photorealistic style, no file name, no version string
```

## [A] P3-F57 · 전자지불 수단과 보안요소 · 전면 재생성

```text
[A] P3-F57 · 전자지불 수단과 보안요소 · 전면 재생성

input_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\01_전면재생성\Part3\P3-F57.png
output_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\03_수정완료\Part3\P3-F57.png
canvas: 1800 x 1004 px
output_filename: P3-F57.png
title_policy: 내부 전체 제목·그림 코드 금지

문제:
전자지불 수단별 위험·통제가 중복·오탈자로 신뢰하기 어렵다.

필수 수정:
신용카드·계좌이체·전자화폐/선불·모바일결제별 핵심 위험과 보호 통제를 4열 비교로 단순화.

통합 가이드 세부 지침:
신용카드, 계좌이체, 전자화폐·선불, 모바일 결제를 각각 `핵심 위험`과 `핵심 보호`로 비교한다. 토큰화·거래내용 확인·이중지불 방지·TEE/Secure Element·FIDO 등을 정확히 배치한다.

기본 프롬프트:
정보보안기사 시험 대비용 한국어 교육 도식이다.
원본의 학습 목적만 유지하고, 아래에 지정한 정확한 구조와 허용 텍스트로 새로 그린다.
흰 배경, 네이비·틸·밝은 회색 중심, 위험·오류만 빨강, 단순한 벡터 스타일.
화살표는 실제 데이터·제어 흐름에만 사용하고 방향을 정확히 맞춘다.
허용 텍스트 외의 문구, 워터마크, 프롬프트 문장, 파일명, 가짜 수식, 의미 없는 약어를 넣지 않는다.
출력 크기와 제목 정책은 해당 코드의 매니페스트를 따른다.

공통 네거티브:
no watermark, no prompt text, no placeholder text, no pseudo-Korean,
no misspelled Korean, no duplicate labels, no invented formula,
no tiny text, no decorative arrows, no gradient background,
no photorealistic style, no file name, no version string
```

## [A] P3-F58 · SET 참여자와 거래 흐름 · 전면 재생성

```text
[A] P3-F58 · SET 참여자와 거래 흐름 · 전면 재생성

input_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\01_전면재생성\Part3\P3-F58.png
output_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\03_수정완료\Part3\P3-F58.png
canvas: 1800 x 1004 px
output_filename: P3-F58.png
title_policy: 내부 전체 제목·그림 코드 금지

문제:
SET 참여자·주문정보·지급정보·승인 흐름의 방향이 모호하거나 틀렸다.

필수 수정:
Cardholder→Merchant 주문정보, 지급정보는 Payment Gateway 공개키로 보호, Merchant→Gateway 승인요청, Gateway↔Issuer/Acquirer 승인·정산, CA는 인증서 지원으로 재구성.

통합 가이드 세부 지침:
- Cardholder가 OI와 PI를 만들고 이중서명을 생성.
- Merchant는 OI를 처리하고 PI 평문을 읽지 않는다.
- Payment Gateway는 PI를 처리하고 OI 전체를 보지 않는다.
- Gateway↔Issuer/Acquirer 승인·정산, CA는 인증서 지원.

기본 프롬프트:
정보보안기사 시험 대비용 한국어 교육 도식이다.
원본의 학습 목적만 유지하고, 아래에 지정한 정확한 구조와 허용 텍스트로 새로 그린다.
흰 배경, 네이비·틸·밝은 회색 중심, 위험·오류만 빨강, 단순한 벡터 스타일.
화살표는 실제 데이터·제어 흐름에만 사용하고 방향을 정확히 맞춘다.
허용 텍스트 외의 문구, 워터마크, 프롬프트 문장, 파일명, 가짜 수식, 의미 없는 약어를 넣지 않는다.
출력 크기와 제목 정책은 해당 코드의 매니페스트를 따른다.

공통 네거티브:
no watermark, no prompt text, no placeholder text, no pseudo-Korean,
no misspelled Korean, no duplicate labels, no invented formula,
no tiny text, no decorative arrows, no gradient background,
no photorealistic style, no file name, no version string
```

## [A] P3-F59 · SET 이중서명 · 전면 재생성

```text
[A] P3-F59 · SET 이중서명 · 전면 재생성

input_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\01_전면재생성\Part3\P3-F59.png
output_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\03_수정완료\Part3\P3-F59.png
canvas: 1800 x 1004 px
output_filename: P3-F59.png
title_policy: 내부 전체 제목·그림 코드 금지

문제:
고객 공개키가 서명 생성에 쓰이는 것처럼 보이고 이중서명 검증식이 틀렸다.

필수 수정:
`PIMD=H(PI)`, `OIMD=H(OI)`, `POMD=H(PIMD||OIMD)`, `DS=Sign_customer_private(POMD)`. Merchant는 OI+PIMD, Gateway는 PI+OIMD로 고객 공개키 검증.

통합 가이드 세부 지침:
`PIMD=H(PI)`, `OIMD=H(OI)`, `POMD=H(PIMD || OIMD)`, `DS=Sign_customer_private(POMD)`.

- Merchant: OI + PIMD + DS + 고객 공개키로 검증.
- Gateway: PI + OIMD + DS + 고객 공개키로 검증.
- 고객 공개키를 서명 생성 입력에 넣지 않는다.

기본 프롬프트:
정보보안기사 시험 대비용 한국어 교육 도식이다.
원본의 학습 목적만 유지하고, 아래에 지정한 정확한 구조와 허용 텍스트로 새로 그린다.
흰 배경, 네이비·틸·밝은 회색 중심, 위험·오류만 빨강, 단순한 벡터 스타일.
화살표는 실제 데이터·제어 흐름에만 사용하고 방향을 정확히 맞춘다.
허용 텍스트 외의 문구, 워터마크, 프롬프트 문장, 파일명, 가짜 수식, 의미 없는 약어를 넣지 않는다.
출력 크기와 제목 정책은 해당 코드의 매니페스트를 따른다.

공통 네거티브:
no watermark, no prompt text, no placeholder text, no pseudo-Korean,
no misspelled Korean, no duplicate labels, no invented formula,
no tiny text, no decorative arrows, no gradient background,
no photorealistic style, no file name, no version string
```

## [A] P3-F60 · 전자화폐와 은닉서명 · 전면 재생성

```text
[A] P3-F60 · 전자화폐와 은닉서명 · 전면 재생성

input_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\01_전면재생성\Part3\P3-F60.png
output_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\03_수정완료\Part3\P3-F60.png
canvas: 1800 x 1004 px
output_filename: P3-F60.png
title_policy: 내부 전체 제목·그림 코드 금지

문제:
은닉·서명·해제·이중지불 확인의 흐름이 뒤섞여 있다.

필수 수정:
사용자 Blind→은행이 Blinded value 서명→사용자 Unblind→상점이 은행 공개키 검증→발행기관/DB가 이중지불 확인 순서.

통합 가이드 세부 지침:
`사용자 원문/화폐정보 → Blind(r) → 은행이 Blinded Value에 개인키 서명 → 사용자 Unblind → 상점이 은행 공개키 검증 → 발행기관/DB가 이중지불 확인`.

기본 프롬프트:
정보보안기사 시험 대비용 한국어 교육 도식이다.
원본의 학습 목적만 유지하고, 아래에 지정한 정확한 구조와 허용 텍스트로 새로 그린다.
흰 배경, 네이비·틸·밝은 회색 중심, 위험·오류만 빨강, 단순한 벡터 스타일.
화살표는 실제 데이터·제어 흐름에만 사용하고 방향을 정확히 맞춘다.
허용 텍스트 외의 문구, 워터마크, 프롬프트 문장, 파일명, 가짜 수식, 의미 없는 약어를 넣지 않는다.
출력 크기와 제목 정책은 해당 코드의 매니페스트를 따른다.

공통 네거티브:
no watermark, no prompt text, no placeholder text, no pseudo-Korean,
no misspelled Korean, no duplicate labels, no invented formula,
no tiny text, no decorative arrows, no gradient background,
no photorealistic style, no file name, no version string
```

## [A] P3-F61 · 전자서명·PKI·시점확인 · 전면 재생성

```text
[A] P3-F61 · 전자서명·PKI·시점확인 · 전면 재생성

input_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\01_전면재생성\Part3\P3-F61.png
output_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\03_수정완료\Part3\P3-F61.png
canvas: 1800 x 1004 px
output_filename: P3-F61.png
title_policy: 내부 전체 제목·그림 코드 금지

문제:
전자서명, 인증서 경로, TSA의 역할이 한 흐름에서 뒤섞여 잘못 읽힌다.

필수 수정:
서명 생성/검증, 인증서 경로/폐기 검증, TSA Timestamp Token을 세 패널로 분리하고 TSA는 데이터 해시+신뢰시각을 서명한다고 표시.

통합 가이드 세부 지침:
세 패널로 분리한다.

1. 메시지 해시+서명자 개인키 → 전자서명, 공개키 검증
2. 인증서가 공개키와 신원을 결속, 체인·유효기간·폐기 확인
3. TSA가 데이터/서명 해시와 신뢰시각을 묶어 Timestamp Token 서명

기본 프롬프트:
정보보안기사 시험 대비용 한국어 교육 도식이다.
원본의 학습 목적만 유지하고, 아래에 지정한 정확한 구조와 허용 텍스트로 새로 그린다.
흰 배경, 네이비·틸·밝은 회색 중심, 위험·오류만 빨강, 단순한 벡터 스타일.
화살표는 실제 데이터·제어 흐름에만 사용하고 방향을 정확히 맞춘다.
허용 텍스트 외의 문구, 워터마크, 프롬프트 문장, 파일명, 가짜 수식, 의미 없는 약어를 넣지 않는다.
출력 크기와 제목 정책은 해당 코드의 매니페스트를 따른다.

공통 네거티브:
no watermark, no prompt text, no placeholder text, no pseudo-Korean,
no misspelled Korean, no duplicate labels, no invented formula,
no tiny text, no decorative arrows, no gradient background,
no photorealistic style, no file name, no version string
```

## [A] P3-F66 · Secure SDLC 보안활동 · 전면 재생성

```text
[A] P3-F66 · Secure SDLC 보안활동 · 전면 재생성

input_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\01_전면재생성\Part3\P3-F66.png
output_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\03_수정완료\Part3\P3-F66.png
canvas: 1800 x 1004 px
output_filename: P3-F66.png
title_policy: 내부 전체 제목·그림 코드 금지

문제:
Secure SDLC 단계 순서가 틀리고 Build 단계에 폐기·삭제가 배치되어 있다.

필수 수정:
Plan/Requirements→Design/Threat Modeling→Implement/Secure Coding→Build/SBOM·무결성→Test→Deploy→Operate→Retire/데이터 삭제·키 폐기 순서로 재구성.

통합 가이드 세부 지침:
`Plan/Requirements → Design/Threat Modeling → Implement/Secure Coding → Build/SBOM·Artifact Integrity → Test(SAST/DAST/SCA/Fuzz) → Deploy/Config·Secrets → Operate/Monitor·Patch·IR → Retire/Data Deletion·Key Revocation`

기본 프롬프트:
정보보안기사 시험 대비용 한국어 교육 도식이다.
원본의 학습 목적만 유지하고, 아래에 지정한 정확한 구조와 허용 텍스트로 새로 그린다.
흰 배경, 네이비·틸·밝은 회색 중심, 위험·오류만 빨강, 단순한 벡터 스타일.
화살표는 실제 데이터·제어 흐름에만 사용하고 방향을 정확히 맞춘다.
허용 텍스트 외의 문구, 워터마크, 프롬프트 문장, 파일명, 가짜 수식, 의미 없는 약어를 넣지 않는다.
출력 크기와 제목 정책은 해당 코드의 매니페스트를 따른다.

공통 네거티브:
no watermark, no prompt text, no placeholder text, no pseudo-Korean,
no misspelled Korean, no duplicate labels, no invented formula,
no tiny text, no decorative arrows, no gradient background,
no photorealistic style, no file name, no version string
```

## [A] P3-F13 · SPF 검증 흐름 · 부분 수정

```text
[A] P3-F13 · SPF 검증 흐름 · 부분 수정

input_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\02_부분수정\Part3\P3-F13.png
output_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\03_수정완료\Part3\P3-F13.png
canvas: 1800 x 1004 px
output_filename: P3-F13.png
title_policy: 내부 전체 제목·그림 코드 금지

문제:
SPF result 의미가 잘못되었다. softfail은 임시 오류가 아니고, 정책 없음은 none이다.

필수 수정:
결과 라벨을 pass=허용, fail=명시적 비허용, softfail=약한 실패, neutral=정책 판단 없음, none=SPF 레코드 없음, temperror/permerror로 교체.

통합 가이드 세부 지침: CSV required_correction을 따른다.

기본 프롬프트:
마스킹하지 않은 픽셀, 구도, 아이콘, 선, 화살표, 색상, 여백, 정확한 문구를 그대로 유지한다.
마스킹 영역의 코드·중복 제목·오탈자·잘못된 짧은 라벨만 삭제하거나 지정 문자열로 교체한다.
삭제 영역은 원래 흰 배경과 기존 테두리를 자연스럽게 복원한다.
새 제목, 새 코드, 워터마크, 생성 지시문, 설명문을 추가하지 않는다.
마스킹 영역 밖은 변경하지 않는다.
원본 픽셀 크기를 유지한다.

공통 네거티브:
no watermark, no prompt text, no placeholder text, no pseudo-Korean,
no misspelled Korean, no duplicate labels, no invented formula,
no tiny text, no decorative arrows, no gradient background,
no photorealistic style, no file name, no version string
```

## [A] P3-F24 · TLS 1.3 핸드셰이크 · 부분 수정

```text
[A] P3-F24 · TLS 1.3 핸드셰이크 · 부분 수정

input_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\02_부분수정\Part3\P3-F24.png
output_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\03_수정완료\Part3\P3-F24.png
canvas: 1800 x 1004 px
output_filename: P3-F24.png
title_policy: 내부 전체 제목·그림 코드 금지

문제:
TLS 1.3 보호 시작점과 CertificateVerify·Finished의 역할 라벨이 부정확하다.

필수 수정:
ServerHello 이후 후속 핸드셰이크가 보호됨을 표시. CertificateVerify=`인증서 개인키 보유 증명/Transcript 서명`, Finished=`Transcript MAC·키 확인`으로 교체.

통합 가이드 세부 지침: CSV required_correction을 따른다.

기본 프롬프트:
마스킹하지 않은 픽셀, 구도, 아이콘, 선, 화살표, 색상, 여백, 정확한 문구를 그대로 유지한다.
마스킹 영역의 코드·중복 제목·오탈자·잘못된 짧은 라벨만 삭제하거나 지정 문자열로 교체한다.
삭제 영역은 원래 흰 배경과 기존 테두리를 자연스럽게 복원한다.
새 제목, 새 코드, 워터마크, 생성 지시문, 설명문을 추가하지 않는다.
마스킹 영역 밖은 변경하지 않는다.
원본 픽셀 크기를 유지한다.

공통 네거티브:
no watermark, no prompt text, no placeholder text, no pseudo-Korean,
no misspelled Korean, no duplicate labels, no invented formula,
no tiny text, no decorative arrows, no gradient background,
no photorealistic style, no file name, no version string
```

## [A] P3-F31 · CSRF 공격과 방어 · 부분 수정

```text
[A] P3-F31 · CSRF 공격과 방어 · 부분 수정

input_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\02_부분수정\Part3\P3-F31.png
output_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\03_수정완료\Part3\P3-F31.png
canvas: 1800 x 1004 px
output_filename: P3-F31.png
title_policy: 내부 전체 제목·그림 코드 금지

문제:
SameSite Lax/Strict/None 설명과 재인증 예시가 부정확하다.

필수 수정:
Lax=`일부 최상위 안전 탐색에 전송`, Strict=`교차 사이트에서 미전송`, None=`교차 사이트 허용+Secure 필수`. 민감행위 대응은 CAPTCHA 대신 비밀번호/MFA 재인증·거래 확인.

통합 가이드 세부 지침: CSV required_correction을 따른다.

기본 프롬프트:
마스킹하지 않은 픽셀, 구도, 아이콘, 선, 화살표, 색상, 여백, 정확한 문구를 그대로 유지한다.
마스킹 영역의 코드·중복 제목·오탈자·잘못된 짧은 라벨만 삭제하거나 지정 문자열로 교체한다.
삭제 영역은 원래 흰 배경과 기존 테두리를 자연스럽게 복원한다.
새 제목, 새 코드, 워터마크, 생성 지시문, 설명문을 추가하지 않는다.
마스킹 영역 밖은 변경하지 않는다.
원본 픽셀 크기를 유지한다.

공통 네거티브:
no watermark, no prompt text, no placeholder text, no pseudo-Korean,
no misspelled Korean, no duplicate labels, no invented formula,
no tiny text, no decorative arrows, no gradient background,
no photorealistic style, no file name, no version string
```

## [A] P3-F42 · Same-Origin Policy와 CORS · 부분 수정

```text
[A] P3-F42 · Same-Origin Policy와 CORS · 부분 수정

input_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\02_부분수정\Part3\P3-F42.png
output_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\03_수정완료\Part3\P3-F42.png
canvas: 1800 x 1004 px
output_filename: P3-F42.png
title_policy: 내부 전체 제목·그림 코드 금지

문제:
CORS 자격증명 헤더와 Origin 구성 설명을 정확히 고쳐야 한다.

필수 수정:
상단 전체 제목 삭제. `Access-Control-Allow-Credentials: true`를 정확히 표기하고 Origin은 scheme+host+port 중 하나라도 다르면 다름을 명시.

통합 가이드 세부 지침: CSV required_correction을 따른다.

기본 프롬프트:
마스킹하지 않은 픽셀, 구도, 아이콘, 선, 화살표, 색상, 여백, 정확한 문구를 그대로 유지한다.
마스킹 영역의 코드·중복 제목·오탈자·잘못된 짧은 라벨만 삭제하거나 지정 문자열로 교체한다.
삭제 영역은 원래 흰 배경과 기존 테두리를 자연스럽게 복원한다.
새 제목, 새 코드, 워터마크, 생성 지시문, 설명문을 추가하지 않는다.
마스킹 영역 밖은 변경하지 않는다.
원본 픽셀 크기를 유지한다.

공통 네거티브:
no watermark, no prompt text, no placeholder text, no pseudo-Korean,
no misspelled Korean, no duplicate labels, no invented formula,
no tiny text, no decorative arrows, no gradient background,
no photorealistic style, no file name, no version string
```

## [A] P4-F11 · FAR·FRR·EER 관계 곡선 · 전면 재생성

```text
[A] P4-F11 · FAR·FRR·EER 관계 곡선 · 전면 재생성

input_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\01_전면재생성\Part4\P4-F11.png
output_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\03_수정완료\Part4\P4-F11.png
canvas: 1600 x 893 px
output_filename: P4-F11.png
title_policy: 내부 전체 제목·그림 코드 금지

문제:
개념 구조·수치·화살표 또는 한글 손상이 있어 전면 재생성이 필요하다.

필수 수정:
통합 가이드의 `P4-F11` 상세 지침과 허용 텍스트를 그대로 적용.

통합 가이드 세부 지침:
문제

- 상단 제목이 깨져 있고 곡선 라벨이 중복되어 FAR/FRR을 잘못 읽을 위험이 있다.

정확한 구조

- 가로축: `판정 임계값` 또는 `임계값이 엄격해짐 →`
- 세로축: `오류율`
- 엄격한 임계값으로 갈수록 `FAR 감소`, `FRR 증가`
- 두 곡선의 교점: `EER` 또는 `CER`
- 하단 주석: `EER이 낮을수록 일반적으로 분리 성능이 좋다`

허용 텍스트

`판정 임계값`, `엄격해짐`, `오류율`, `FAR`, `FRR`, `EER`, `오인수락률`, `오인거부율`, `낮을수록 분리 성능 우수`

기본 프롬프트:
정보보안기사 시험 대비용 한국어 교육 도식이다.
원본의 학습 목적만 유지하고, 아래에 지정한 정확한 구조와 허용 텍스트로 새로 그린다.
흰 배경, 네이비·틸·밝은 회색 중심, 위험·오류만 빨강, 단순한 벡터 스타일.
화살표는 실제 데이터·제어 흐름에만 사용하고 방향을 정확히 맞춘다.
허용 텍스트 외의 문구, 워터마크, 프롬프트 문장, 파일명, 가짜 수식, 의미 없는 약어를 넣지 않는다.
출력 크기와 제목 정책은 해당 코드의 매니페스트를 따른다.

공통 네거티브:
no watermark, no prompt text, no placeholder text, no pseudo-Korean,
no misspelled Korean, no duplicate labels, no invented formula,
no tiny text, no decorative arrows, no gradient background,
no photorealistic style, no file name, no version string
```

## [A] P4-F13 · 영지식 증명의 Prover·Verifier 흐름 · 전면 재생성

```text
[A] P4-F13 · 영지식 증명의 Prover·Verifier 흐름 · 전면 재생성

input_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\01_전면재생성\Part4\P4-F13.png
output_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\03_수정완료\Part4\P4-F13.png
canvas: 1600 x 893 px
output_filename: P4-F13.png
title_policy: 내부 전체 제목·그림 코드 금지

문제:
개념 구조·수치·화살표 또는 한글 손상이 있어 전면 재생성이 필요하다.

필수 수정:
통합 가이드의 `P4-F13` 상세 지침과 허용 텍스트를 그대로 적용.

통합 가이드 세부 지침:
문제

- 제목과 내부 문구가 광범위하게 깨졌다.

정확한 구조

- 좌측 `증명자(Prover)`, 우측 `검증자(Verifier)`
- `Commit → Challenge → Response → Verify`
- 하단 세 성질: `완전성`, `건전성`, `영지식성`
- 비밀 자체는 공개하지 않음을 자물쇠 아이콘으로 표현한다.

허용 텍스트

`증명자`, `검증자`, `비밀`, `Commit`, `Challenge`, `Response`, `Verify`, `완전성`, `건전성`, `영지식성`, `비밀 자체는 공개하지 않음`

기본 프롬프트:
정보보안기사 시험 대비용 한국어 교육 도식이다.
원본의 학습 목적만 유지하고, 아래에 지정한 정확한 구조와 허용 텍스트로 새로 그린다.
흰 배경, 네이비·틸·밝은 회색 중심, 위험·오류만 빨강, 단순한 벡터 스타일.
화살표는 실제 데이터·제어 흐름에만 사용하고 방향을 정확히 맞춘다.
허용 텍스트 외의 문구, 워터마크, 프롬프트 문장, 파일명, 가짜 수식, 의미 없는 약어를 넣지 않는다.
출력 크기와 제목 정책은 해당 코드의 매니페스트를 따른다.

공통 네거티브:
no watermark, no prompt text, no placeholder text, no pseudo-Korean,
no misspelled Korean, no duplicate labels, no invented formula,
no tiny text, no decorative arrows, no gradient background,
no photorealistic style, no file name, no version string
```

## [A] P4-F24 · Clark-Wilson 무결성 모델 · 전면 재생성

```text
[A] P4-F24 · Clark-Wilson 무결성 모델 · 전면 재생성

input_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\01_전면재생성\Part4\P4-F24.png
output_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\03_수정완료\Part4\P4-F24.png
canvas: 1600 x 893 px
output_filename: P4-F24.png
title_policy: 내부 전체 제목·그림 코드 금지

문제:
개념 구조·수치·화살표 또는 한글 손상이 있어 전면 재생성이 필요하다.

필수 수정:
통합 가이드의 `P4-F24` 상세 지침과 허용 텍스트를 그대로 적용.

통합 가이드 세부 지침:
문제

- 코드와 제목이 섞였고 CDI·UDI·TP·IVP 라벨 일부가 깨졌다.

정확한 구조

- `UDI → 인증된 변환절차(TP) → CDI`
- `IVP`가 CDI의 유효 상태를 검증
- 사용자는 CDI를 직접 변경하지 않고 승인된 TP만 사용
- 보조 원칙: `직무분리`, `감사`

허용 텍스트

`사용자`, `UDI`, `TP`, `CDI`, `IVP`, `인증된 변환절차`, `무결성 검증`, `직무분리`, `감사`, `직접 변경 금지`

기본 프롬프트:
정보보안기사 시험 대비용 한국어 교육 도식이다.
원본의 학습 목적만 유지하고, 아래에 지정한 정확한 구조와 허용 텍스트로 새로 그린다.
흰 배경, 네이비·틸·밝은 회색 중심, 위험·오류만 빨강, 단순한 벡터 스타일.
화살표는 실제 데이터·제어 흐름에만 사용하고 방향을 정확히 맞춘다.
허용 텍스트 외의 문구, 워터마크, 프롬프트 문장, 파일명, 가짜 수식, 의미 없는 약어를 넣지 않는다.
출력 크기와 제목 정책은 해당 코드의 매니페스트를 따른다.

공통 네거티브:
no watermark, no prompt text, no placeholder text, no pseudo-Korean,
no misspelled Korean, no duplicate labels, no invented formula,
no tiny text, no decorative arrows, no gradient background,
no photorealistic style, no file name, no version string
```

## [A] P4-F33 · 인증 없는 DH의 MITM · 전면 재생성

```text
[A] P4-F33 · 인증 없는 DH의 MITM · 전면 재생성

input_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\01_전면재생성\Part4\P4-F33.png
output_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\03_수정완료\Part4\P4-F33.png
canvas: 1600 x 893 px
output_filename: P4-F33.png
title_policy: 내부 전체 제목·그림 코드 금지

문제:
개념 구조·수치·화살표 또는 한글 손상이 있어 전면 재생성이 필요하다.

필수 수정:
통합 가이드의 `P4-F33` 상세 지침과 허용 텍스트를 그대로 적용.

통합 가이드 세부 지침:
문제

- 제목과 내부 라벨이 깨졌으며 공격 흐름이 불명확하다.

정확한 구조

- Alice와 Bob 사이에 Mallory를 둔다.
- Mallory가 양쪽 공개값을 대체하여 `Alice–Mallory 공유키`와 `Mallory–Bob 공유키`를 각각 만든다.
- Mallory가 `복호화 → 변조 가능 → 재암호화`한다.
- 방어: `전자서명`, `인증서`, `PSK`, `인증된 키 교환`

허용 텍스트

`Alice`, `Bob`, `Mallory`, `공개값 대체`, `Alice–Mallory 공유키`, `Mallory–Bob 공유키`, `복호화`, `변조`, `재암호화`, `전자서명`, `인증서`, `PSK`, `인증된 키 교환`

기본 프롬프트:
정보보안기사 시험 대비용 한국어 교육 도식이다.
원본의 학습 목적만 유지하고, 아래에 지정한 정확한 구조와 허용 텍스트로 새로 그린다.
흰 배경, 네이비·틸·밝은 회색 중심, 위험·오류만 빨강, 단순한 벡터 스타일.
화살표는 실제 데이터·제어 흐름에만 사용하고 방향을 정확히 맞춘다.
허용 텍스트 외의 문구, 워터마크, 프롬프트 문장, 파일명, 가짜 수식, 의미 없는 약어를 넣지 않는다.
출력 크기와 제목 정책은 해당 코드의 매니페스트를 따른다.

공통 네거티브:
no watermark, no prompt text, no placeholder text, no pseudo-Korean,
no misspelled Korean, no duplicate labels, no invented formula,
no tiny text, no decorative arrows, no gradient background,
no photorealistic style, no file name, no version string
```

## [A] P4-F53 · Feistel과 SPN 구조 비교 · 전면 재생성

```text
[A] P4-F53 · Feistel과 SPN 구조 비교 · 전면 재생성

input_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\01_전면재생성\Part4\P4-F53.png
output_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\03_수정완료\Part4\P4-F53.png
canvas: 1600 x 893 px
output_filename: P4-F53.png
title_policy: 내부 전체 제목·그림 코드 금지

문제:
개념 구조·수치·화살표 또는 한글 손상이 있어 전면 재생성이 필요하다.

필수 수정:
통합 가이드의 `P4-F53` 상세 지침과 허용 텍스트를 그대로 적용.

통합 가이드 세부 지침:
문제

- 제목과 수식이 깨졌고 Feistel 데이터 흐름이 표준 구조와 다르게 보인다.

정확한 구조

- Feistel: `Lᵢ₊₁ = Rᵢ`, `Rᵢ₊₁ = Lᵢ ⊕ F(Rᵢ, Kᵢ)`
- 복호화는 같은 구조에서 라운드키 순서를 반대로 적용
- SPN: `AddRoundKey → Substitution(S-box) → Permutation/Linear Layer` 반복
- 복호화 시 역변환 필요

허용 텍스트

`Feistel`, `SPN`, `Lᵢ`, `Rᵢ`, `F`, `Kᵢ`, `XOR`, `AddRoundKey`, `Substitution`, `S-box`, `Permutation`, `Linear Layer`, `같은 구조·키 순서 반대`, `역변환 필요`

기본 프롬프트:
정보보안기사 시험 대비용 한국어 교육 도식이다.
원본의 학습 목적만 유지하고, 아래에 지정한 정확한 구조와 허용 텍스트로 새로 그린다.
흰 배경, 네이비·틸·밝은 회색 중심, 위험·오류만 빨강, 단순한 벡터 스타일.
화살표는 실제 데이터·제어 흐름에만 사용하고 방향을 정확히 맞춘다.
허용 텍스트 외의 문구, 워터마크, 프롬프트 문장, 파일명, 가짜 수식, 의미 없는 약어를 넣지 않는다.
출력 크기와 제목 정책은 해당 코드의 매니페스트를 따른다.

공통 네거티브:
no watermark, no prompt text, no placeholder text, no pseudo-Korean,
no misspelled Korean, no duplicate labels, no invented formula,
no tiny text, no decorative arrows, no gradient background,
no photorealistic style, no file name, no version string
```

## [A] P4-F54 · 블록암호와 스트림암호 비교 · 전면 재생성

```text
[A] P4-F54 · 블록암호와 스트림암호 비교 · 전면 재생성

input_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\01_전면재생성\Part4\P4-F54.png
output_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\03_수정완료\Part4\P4-F54.png
canvas: 1600 x 893 px
output_filename: P4-F54.png
title_policy: 내부 전체 제목·그림 코드 금지

문제:
개념 구조·수치·화살표 또는 한글 손상이 있어 전면 재생성이 필요하다.

필수 수정:
통합 가이드의 `P4-F54` 상세 지침과 허용 텍스트를 그대로 적용.

통합 가이드 세부 지침:
문제

- 스트림암호 패널이 중복되고 AES 예시와 패딩 설명이 혼재되어 있다.

정확한 구조

- 블록암호: 고정 크기 블록, 운용모드 필요, 예 `AES·ARIA·SEED`
- `ECB/CBC는 패딩이 필요할 수 있음`, `CTR/GCM은 패딩 불필요`
- 스트림암호: 키스트림과 평문을 XOR, 패딩 불필요, 예 `ChaCha20`
- 공통 경고: `키·Nonce 또는 키스트림 재사용 금지`
- 하단 주석: `CTR/OFB/CFB는 블록암호 운용모드이며 스트림처럼 동작`

허용 텍스트

`블록암호`, `스트림암호`, `고정 크기 블록`, `운용모드`, `키스트림`, `XOR`, `패딩`, `AES`, `ARIA`, `SEED`, `ChaCha20`, `Nonce 재사용 금지`, `CTR/OFB/CFB는 블록암호 운용모드`

기본 프롬프트:
정보보안기사 시험 대비용 한국어 교육 도식이다.
원본의 학습 목적만 유지하고, 아래에 지정한 정확한 구조와 허용 텍스트로 새로 그린다.
흰 배경, 네이비·틸·밝은 회색 중심, 위험·오류만 빨강, 단순한 벡터 스타일.
화살표는 실제 데이터·제어 흐름에만 사용하고 방향을 정확히 맞춘다.
허용 텍스트 외의 문구, 워터마크, 프롬프트 문장, 파일명, 가짜 수식, 의미 없는 약어를 넣지 않는다.
출력 크기와 제목 정책은 해당 코드의 매니페스트를 따른다.

공통 네거티브:
no watermark, no prompt text, no placeholder text, no pseudo-Korean,
no misspelled Korean, no duplicate labels, no invented formula,
no tiny text, no decorative arrows, no gradient background,
no photorealistic style, no file name, no version string
```

## [A] P4-F58 · 대표 대칭키 알고리즘 비교 · 전면 재생성

```text
[A] P4-F58 · 대표 대칭키 알고리즘 비교 · 전면 재생성

input_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\01_전면재생성\Part4\P4-F58.png
output_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\03_수정완료\Part4\P4-F58.png
canvas: 1600 x 893 px
output_filename: P4-F58.png
title_policy: 내부 전체 제목·그림 코드 금지

문제:
개념 구조·수치·화살표 또는 한글 손상이 있어 전면 재생성이 필요하다.

필수 수정:
통합 가이드의 `P4-F58` 상세 지침과 허용 텍스트를 그대로 적용.

통합 가이드 세부 지침:
문제

- 그림 제목이 주제와 다르고, RC4 분류·키 길이·알고리즘 행이 혼재되어 있다.

권장 표

| 알고리즘 | 종류 | 블록/키 | 구조·위치 |
|---|---|---|---|
| DES | 블록 | 64 / 유효 56비트 | Feistel, 레거시 |
| 3DES | 블록 | 64 / 2키·3키 | EDE, 레거시 |
| AES | 블록 | 128 / 128·192·256 | SPN, 현재 중심 |
| SEED | 블록 | 128 / 128 | Feistel |
| ARIA | 블록 | 128 / 128·192·256 | SPN |
| HIGHT | 블록 | 64 / 128 | 경량 환경 |
| IDEA | 블록 | 64 / 128 | 레거시·역사적 |
| RC4 | 스트림 | 가변 | 사용 중단·레거시 |

그림은 표 형식으로 단순화하고 제품 인증과 관련된 제목은 제거한다.

기본 프롬프트:
정보보안기사 시험 대비용 한국어 교육 도식이다.
원본의 학습 목적만 유지하고, 아래에 지정한 정확한 구조와 허용 텍스트로 새로 그린다.
흰 배경, 네이비·틸·밝은 회색 중심, 위험·오류만 빨강, 단순한 벡터 스타일.
화살표는 실제 데이터·제어 흐름에만 사용하고 방향을 정확히 맞춘다.
허용 텍스트 외의 문구, 워터마크, 프롬프트 문장, 파일명, 가짜 수식, 의미 없는 약어를 넣지 않는다.
출력 크기와 제목 정책은 해당 코드의 매니페스트를 따른다.

공통 네거티브:
no watermark, no prompt text, no placeholder text, no pseudo-Korean,
no misspelled Korean, no duplicate labels, no invented formula,
no tiny text, no decorative arrows, no gradient background,
no photorealistic style, no file name, no version string
```

## [A] P4-F64 · 암호분석 공격 지도 · 전면 재생성

```text
[A] P4-F64 · 암호분석 공격 지도 · 전면 재생성

input_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\01_전면재생성\Part4\P4-F64.png
output_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\03_수정완료\Part4\P4-F64.png
canvas: 1600 x 893 px
output_filename: P4-F64.png
title_policy: 내부 전체 제목·그림 코드 금지

문제:
개념 구조·수치·화살표 또는 한글 손상이 있어 전면 재생성이 필요하다.

필수 수정:
통합 가이드의 `P4-F64` 상세 지침과 허용 텍스트를 그대로 적용.

통합 가이드 세부 지침:
문제

- 작은 글자가 광범위하게 깨졌고 의미 없는 수식과 중복 분류가 있다.

정확한 분류

- 키 탐색: `전수공격`
- 통계·구조: `차분암호분석`, `선형암호분석`
- 다중 암호: `중간일치 공격`
- 키 관계: `관련키 공격`
- 구현 누출: `타이밍`, `전력`, `캐시`, `전자파`
- 오류 유도: `결함 주입 공격`

수식은 넣지 말고 각 공격의 입력·관찰점만 아이콘과 한 문장으로 나타낸다.

기본 프롬프트:
정보보안기사 시험 대비용 한국어 교육 도식이다.
원본의 학습 목적만 유지하고, 아래에 지정한 정확한 구조와 허용 텍스트로 새로 그린다.
흰 배경, 네이비·틸·밝은 회색 중심, 위험·오류만 빨강, 단순한 벡터 스타일.
화살표는 실제 데이터·제어 흐름에만 사용하고 방향을 정확히 맞춘다.
허용 텍스트 외의 문구, 워터마크, 프롬프트 문장, 파일명, 가짜 수식, 의미 없는 약어를 넣지 않는다.
출력 크기와 제목 정책은 해당 코드의 매니페스트를 따른다.

공통 네거티브:
no watermark, no prompt text, no placeholder text, no pseudo-Korean,
no misspelled Korean, no duplicate labels, no invented formula,
no tiny text, no decorative arrows, no gradient background,
no photorealistic style, no file name, no version string
```

## [A] P4-F65 · 공개키 암호의 난제 지도 · 전면 재생성

```text
[A] P4-F65 · 공개키 암호의 난제 지도 · 전면 재생성

input_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\01_전면재생성\Part4\P4-F65.png
output_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\03_수정완료\Part4\P4-F65.png
canvas: 1600 x 893 px
output_filename: P4-F65.png
title_policy: 내부 전체 제목·그림 코드 금지

문제:
개념 구조·수치·화살표 또는 한글 손상이 있어 전면 재생성이 필요하다.

필수 수정:
통합 가이드의 `P4-F65` 상세 지침과 허용 텍스트를 그대로 적용.

통합 가이드 세부 지침:
문제

- 제목이 중복되고 RSA·ECC 보안강도 비교 수치가 잘못되어 있다.

정확한 구조

- `정수 인수분해 문제 → RSA·Rabin`
- `유한체 이산로그 문제 → DH·ElGamal·DSA`
- `타원곡선 이산로그 문제 → ECDH·ECDSA`
- 하단: `양자컴퓨터의 Shor 알고리즘은 세 난제를 위협`
- 수치표가 필요하면 최소한 `RSA 2048 ≈ ECC 224(약 112비트)`, `RSA 3072 ≈ ECC 256(약 128비트)` 정도만 넣는다.
- 숫자 비교가 핵심이 아니면 “동일 보안강도에서 ECC 키가 더 짧다”로 대체한다.

기본 프롬프트:
정보보안기사 시험 대비용 한국어 교육 도식이다.
원본의 학습 목적만 유지하고, 아래에 지정한 정확한 구조와 허용 텍스트로 새로 그린다.
흰 배경, 네이비·틸·밝은 회색 중심, 위험·오류만 빨강, 단순한 벡터 스타일.
화살표는 실제 데이터·제어 흐름에만 사용하고 방향을 정확히 맞춘다.
허용 텍스트 외의 문구, 워터마크, 프롬프트 문장, 파일명, 가짜 수식, 의미 없는 약어를 넣지 않는다.
출력 크기와 제목 정책은 해당 코드의 매니페스트를 따른다.

공통 네거티브:
no watermark, no prompt text, no placeholder text, no pseudo-Korean,
no misspelled Korean, no duplicate labels, no invented formula,
no tiny text, no decorative arrows, no gradient background,
no photorealistic style, no file name, no version string
```

## [A] P4-F73 · 비밀번호 Salt·Pepper·KDF 저장 구조 · 전면 재생성

```text
[A] P4-F73 · 비밀번호 Salt·Pepper·KDF 저장 구조 · 전면 재생성

input_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\01_전면재생성\Part4\P4-F73.png
output_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\03_수정완료\Part4\P4-F73.png
canvas: 1600 x 893 px
output_filename: P4-F73.png
title_policy: 내부 전체 제목·그림 코드 금지

문제:
개념 구조·수치·화살표 또는 한글 손상이 있어 전면 재생성이 필요하다.

필수 수정:
통합 가이드의 `P4-F73` 상세 지침과 허용 텍스트를 그대로 적용.

통합 가이드 세부 지침:
문제

- Pepper 유출 경로에서 방어가 강화되는 것처럼 표현되어 논리적으로 반대다.

정확한 구조

- `비밀번호 + 사용자별 Salt → 느린 Password KDF → 검증자 저장`
- Salt는 사용자별 고유값이며 DB에 함께 저장 가능
- Pepper는 선택 사항이며 `KMS/HSM` 등 DB와 분리된 영역에 보관
- DB만 유출되면 공격자는 KDF 비용과 미지의 Pepper를 모두 상대해야 함
- Pepper까지 유출되면 Pepper가 주던 추가 방어층은 사라짐

허용 텍스트

`비밀번호`, `Salt`, `Password KDF`, `Argon2id`, `scrypt`, `bcrypt`, `PBKDF2`, `검증자`, `Pepper`, `KMS/HSM`, `DB와 분리`, `Pepper 유출 시 추가 방어 상실`

기본 프롬프트:
정보보안기사 시험 대비용 한국어 교육 도식이다.
원본의 학습 목적만 유지하고, 아래에 지정한 정확한 구조와 허용 텍스트로 새로 그린다.
흰 배경, 네이비·틸·밝은 회색 중심, 위험·오류만 빨강, 단순한 벡터 스타일.
화살표는 실제 데이터·제어 흐름에만 사용하고 방향을 정확히 맞춘다.
허용 텍스트 외의 문구, 워터마크, 프롬프트 문장, 파일명, 가짜 수식, 의미 없는 약어를 넣지 않는다.
출력 크기와 제목 정책은 해당 코드의 매니페스트를 따른다.

공통 네거티브:
no watermark, no prompt text, no placeholder text, no pseudo-Korean,
no misspelled Korean, no duplicate labels, no invented formula,
no tiny text, no decorative arrows, no gradient background,
no photorealistic style, no file name, no version string
```

## [A] P4-F74 · KDF와 키 분리 · 전면 재생성

```text
[A] P4-F74 · KDF와 키 분리 · 전면 재생성

input_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\01_전면재생성\Part4\P4-F74.png
output_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\03_수정완료\Part4\P4-F74.png
canvas: 1600 x 893 px
output_filename: P4-F74.png
title_policy: 내부 전체 제목·그림 코드 금지

문제:
개념 구조·수치·화살표 또는 한글 손상이 있어 전면 재생성이 필요하다.

필수 수정:
통합 가이드의 `P4-F74` 상세 지침과 허용 텍스트를 그대로 적용.

통합 가이드 세부 지침:
문제

- 제목과 라벨이 깨졌고 Password KDF·HKDF·Nonce의 역할이 혼재되어 있다.

정확한 구조

- 왼쪽: 저엔트로피 비밀번호는 `Password KDF`로 강화
- 오른쪽: 고엔트로피 입력키 재료는 `HKDF-Extract → PRK → HKDF-Expand(info)`
- 서로 다른 `info/label/context`로 `암호화 키`, `MAC 키`, `Exporter 키`를 분리 파생
- `Nonce는 일반적으로 비밀키가 아니며 고유성이 핵심`
- 잘못된 예: 같은 원시 키를 암호화와 MAC에 직접 재사용

---

기본 프롬프트:
정보보안기사 시험 대비용 한국어 교육 도식이다.
원본의 학습 목적만 유지하고, 아래에 지정한 정확한 구조와 허용 텍스트로 새로 그린다.
흰 배경, 네이비·틸·밝은 회색 중심, 위험·오류만 빨강, 단순한 벡터 스타일.
화살표는 실제 데이터·제어 흐름에만 사용하고 방향을 정확히 맞춘다.
허용 텍스트 외의 문구, 워터마크, 프롬프트 문장, 파일명, 가짜 수식, 의미 없는 약어를 넣지 않는다.
출력 크기와 제목 정책은 해당 코드의 매니페스트를 따른다.

공통 네거티브:
no watermark, no prompt text, no placeholder text, no pseudo-Korean,
no misspelled Korean, no duplicate labels, no invented formula,
no tiny text, no decorative arrows, no gradient background,
no photorealistic style, no file name, no version string
```

## [A] P4-F66 · RSA 키 생성과 작은 수 계산 · 부분 수정

```text
[A] P4-F66 · RSA 키 생성과 작은 수 계산 · 부분 수정

input_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\02_부분수정\Part4\P4-F66.png
output_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\03_수정완료\Part4\P4-F66.png
canvas: 1600 x 893 px
output_filename: P4-F66.png
title_policy: 내부 전체 제목·그림 코드 금지

문제:
그림 내부 코드·중복 제목·지시문 또는 국소 오탈자가 남아 있다.

필수 수정:
상단 코드·전체 제목 삭제. 주석을 `실제 RSA는 n을 충분히 크게 사용한다. 예: n 2048비트 이상, p와 q는 보통 그 절반 정도 비트 길이`로 교체. 작은 수 계산 자체는 유지.

통합 가이드 세부 지침: CSV required_correction을 따른다.

기본 프롬프트:
마스킹하지 않은 픽셀, 구도, 아이콘, 선, 화살표, 색상, 여백, 정확한 문구를 그대로 유지한다.
마스킹 영역의 코드·중복 제목·오탈자·잘못된 짧은 라벨만 삭제하거나 지정 문자열로 교체한다.
삭제 영역은 원래 흰 배경과 기존 테두리를 자연스럽게 복원한다.
새 제목, 새 코드, 워터마크, 생성 지시문, 설명문을 추가하지 않는다.
마스킹 영역 밖은 변경하지 않는다.
원본 픽셀 크기를 유지한다.

공통 네거티브:
no watermark, no prompt text, no placeholder text, no pseudo-Korean,
no misspelled Korean, no duplicate labels, no invented formula,
no tiny text, no decorative arrows, no gradient background,
no photorealistic style, no file name, no version string
```

## [A] P5-F05 · 정보보호 조직과 RACI · 전면 재생성

```text
[A] P5-F05 · 정보보호 조직과 RACI · 전면 재생성

input_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\01_전면재생성\Part5\P5-F05.png
output_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\03_수정완료\Part5\P5-F05.png
canvas: 1600 x 893 px
output_filename: P5-F05.png
title_policy: 내부 전체 제목·그림 코드 금지

문제:
개념 구조·수치·화살표 또는 한글 손상이 있어 전면 재생성이 필요하다.

필수 수정:
통합 가이드의 `P5-F05` 상세 지침과 허용 텍스트를 그대로 적용.

통합 가이드 세부 지침:
문제

- 제목과 내부 문구가 깨졌고 RACI를 흐름도로 오해할 수 있다.

정확한 구조

- 행: 업무, 열: 역할의 **책임 매트릭스**
- `R(수행책임)`, `A(최종책임)`, `C(자문)`, `I(통보)`
- 업무 하나마다 A는 원칙적으로 1명
- R은 여러 명 가능, C는 양방향 자문, I는 일방향 통보

허용 텍스트

`업무`, `최고경영진`, `CISO`, `자산소유자`, `운영자`, `내부감사`, `R 수행책임`, `A 최종책임`, `C 자문`, `I 통보`, `업무별 A 1명`

기본 프롬프트:
정보보안기사 시험 대비용 한국어 교육 도식이다.
원본의 학습 목적만 유지하고, 아래에 지정한 정확한 구조와 허용 텍스트로 새로 그린다.
흰 배경, 네이비·틸·밝은 회색 중심, 위험·오류만 빨강, 단순한 벡터 스타일.
화살표는 실제 데이터·제어 흐름에만 사용하고 방향을 정확히 맞춘다.
허용 텍스트 외의 문구, 워터마크, 프롬프트 문장, 파일명, 가짜 수식, 의미 없는 약어를 넣지 않는다.
출력 크기와 제목 정책은 해당 코드의 매니페스트를 따른다.

공통 네거티브:
no watermark, no prompt text, no placeholder text, no pseudo-Korean,
no misspelled Korean, no duplicate labels, no invented formula,
no tiny text, no decorative arrows, no gradient background,
no photorealistic style, no file name, no version string
```

## [A] P5-F26 · 물리보안 구역과 출입통제 · 전면 재생성

```text
[A] P5-F26 · 물리보안 구역과 출입통제 · 전면 재생성

input_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\01_전면재생성\Part5\P5-F26.png
output_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\03_수정완료\Part5\P5-F26.png
canvas: 1600 x 893 px
output_filename: P5-F26.png
title_policy: 내부 전체 제목·그림 코드 금지

문제:
개념 구조·수치·화살표 또는 한글 손상이 있어 전면 재생성이 필요하다.

필수 수정:
통합 가이드의 `P5-F26` 상세 지침과 허용 텍스트를 그대로 적용.

통합 가이드 세부 지침:
문제

- 구역명과 통제 문구가 여러 곳 깨졌다.

정확한 구조

`공개 구역 → 통제 구역 → 제한 구역 → 핵심 구역`

단계가 높아질수록 `사전 승인`, `강한 인증`, `방문자 동행`, `출입기록`, `반입·반출 통제`를 강화한다. 옆에는 `Tailgating 방지`, `CCTV`, `방문증 회수`, `정기 권한검토`, `화재·누수·전원·온습도`를 배치한다.

기본 프롬프트:
정보보안기사 시험 대비용 한국어 교육 도식이다.
원본의 학습 목적만 유지하고, 아래에 지정한 정확한 구조와 허용 텍스트로 새로 그린다.
흰 배경, 네이비·틸·밝은 회색 중심, 위험·오류만 빨강, 단순한 벡터 스타일.
화살표는 실제 데이터·제어 흐름에만 사용하고 방향을 정확히 맞춘다.
허용 텍스트 외의 문구, 워터마크, 프롬프트 문장, 파일명, 가짜 수식, 의미 없는 약어를 넣지 않는다.
출력 크기와 제목 정책은 해당 코드의 매니페스트를 따른다.

공통 네거티브:
no watermark, no prompt text, no placeholder text, no pseudo-Korean,
no misspelled Korean, no duplicate labels, no invented formula,
no tiny text, no decorative arrows, no gradient background,
no photorealistic style, no file name, no version string
```

## [A] P5-F41 · 휘발성 증거 수집 우선순위 · 전면 재생성

```text
[A] P5-F41 · 휘발성 증거 수집 우선순위 · 전면 재생성

input_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\01_전면재생성\Part5\P5-F41.png
output_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\03_수정완료\Part5\P5-F41.png
canvas: 1600 x 893 px
output_filename: P5-F41.png
title_policy: 내부 전체 제목·그림 코드 금지

문제:
개념 구조·수치·화살표 또는 한글 손상이 있어 전면 재생성이 필요하다.

필수 수정:
통합 가이드의 `P5-F41` 상세 지침과 허용 텍스트를 그대로 적용.

통합 가이드 세부 지침:
문제

- 제목과 설명문이 광범위하게 깨졌다.

정확한 순서

`CPU 레지스터·캐시 → 메모리·프로세스 → 네트워크 상태 → 임시 데이터 → 디스크 → 원격 로그·백업`

하단 주석

`현장 안전, 악성행위 진행 여부, 서비스 가용성, 증거가치를 함께 고려하여 순서를 조정할 수 있다.`

기본 프롬프트:
정보보안기사 시험 대비용 한국어 교육 도식이다.
원본의 학습 목적만 유지하고, 아래에 지정한 정확한 구조와 허용 텍스트로 새로 그린다.
흰 배경, 네이비·틸·밝은 회색 중심, 위험·오류만 빨강, 단순한 벡터 스타일.
화살표는 실제 데이터·제어 흐름에만 사용하고 방향을 정확히 맞춘다.
허용 텍스트 외의 문구, 워터마크, 프롬프트 문장, 파일명, 가짜 수식, 의미 없는 약어를 넣지 않는다.
출력 크기와 제목 정책은 해당 코드의 매니페스트를 따른다.

공통 네거티브:
no watermark, no prompt text, no placeholder text, no pseudo-Korean,
no misspelled Korean, no duplicate labels, no invented formula,
no tiny text, no decorative arrows, no gradient background,
no photorealistic style, no file name, no version string
```

## [A] P5-F42 · 디지털 증거 처리 생명주기 · 전면 재생성

```text
[A] P5-F42 · 디지털 증거 처리 생명주기 · 전면 재생성

input_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\01_전면재생성\Part5\P5-F42.png
output_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\03_수정완료\Part5\P5-F42.png
canvas: 1600 x 893 px
output_filename: P5-F42.png
title_policy: 내부 전체 제목·그림 코드 금지

문제:
개념 구조·수치·화살표 또는 한글 손상이 있어 전면 재생성이 필요하다.

필수 수정:
통합 가이드의 `P5-F42` 상세 지침과 허용 텍스트를 그대로 적용.

통합 가이드 세부 지침:
문제

- 단계명이 깨졌고 좌측 라벨이 의미 없는 문자로 보인다.

정확한 구조

`식별 → 보존 → 수집·획득 → 검사 → 분석 → 보고 → 보관·폐기`

전 단계 공통 띠

`해시`, `기록`, `연계보관성`, `도구·버전·시간 문서화`

하단 주석

`원본은 가능한 한 보존하고 검증된 작업복사본에서 분석한다.`

기본 프롬프트:
정보보안기사 시험 대비용 한국어 교육 도식이다.
원본의 학습 목적만 유지하고, 아래에 지정한 정확한 구조와 허용 텍스트로 새로 그린다.
흰 배경, 네이비·틸·밝은 회색 중심, 위험·오류만 빨강, 단순한 벡터 스타일.
화살표는 실제 데이터·제어 흐름에만 사용하고 방향을 정확히 맞춘다.
허용 텍스트 외의 문구, 워터마크, 프롬프트 문장, 파일명, 가짜 수식, 의미 없는 약어를 넣지 않는다.
출력 크기와 제목 정책은 해당 코드의 매니페스트를 따른다.

공통 네거티브:
no watermark, no prompt text, no placeholder text, no pseudo-Korean,
no misspelled Korean, no duplicate labels, no invented formula,
no tiny text, no decorative arrows, no gradient background,
no photorealistic style, no file name, no version string
```

## [A] P5-F46 · ISMS-P 인증기준 16·64·21 · 전면 재생성

```text
[A] P5-F46 · ISMS-P 인증기준 16·64·21 · 전면 재생성

input_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\01_전면재생성\Part5\P5-F46.png
output_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\03_수정완료\Part5\P5-F46.png
canvas: 1600 x 893 px
output_filename: P5-F46.png
title_policy: 내부 전체 제목·그림 코드 금지

문제:
개념 구조·수치·화살표 또는 한글 손상이 있어 전면 재생성이 필요하다.

필수 수정:
통합 가이드의 `P5-F46` 상세 지침과 허용 텍스트를 그대로 적용.

통합 가이드 세부 지침:
문제

- 큰 숫자는 맞지만 제목과 세부 라벨이 광범위하게 깨졌다.

정확한 구조

- `관리체계 수립 및 운영 16개`
- `보호대책 요구사항 64개`
- `개인정보 처리단계별 요구사항 21개`
- 합계 `101개 기준`
- 과거 `22개` 표기는 개정 전 수치라는 작은 역사 주석만 허용

기본 프롬프트:
정보보안기사 시험 대비용 한국어 교육 도식이다.
원본의 학습 목적만 유지하고, 아래에 지정한 정확한 구조와 허용 텍스트로 새로 그린다.
흰 배경, 네이비·틸·밝은 회색 중심, 위험·오류만 빨강, 단순한 벡터 스타일.
화살표는 실제 데이터·제어 흐름에만 사용하고 방향을 정확히 맞춘다.
허용 텍스트 외의 문구, 워터마크, 프롬프트 문장, 파일명, 가짜 수식, 의미 없는 약어를 넣지 않는다.
출력 크기와 제목 정책은 해당 코드의 매니페스트를 따른다.

공통 네거티브:
no watermark, no prompt text, no placeholder text, no pseudo-Korean,
no misspelled Korean, no duplicate labels, no invented formula,
no tiny text, no decorative arrows, no gradient background,
no photorealistic style, no file name, no version string
```

## [A] P5-F49 · 공통평가기준 CC 전체 구조 · 전면 재생성

```text
[A] P5-F49 · 공통평가기준 CC 전체 구조 · 전면 재생성

input_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\01_전면재생성\Part5\P5-F49.png
output_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\03_수정완료\Part5\P5-F49.png
canvas: 1600 x 893 px
output_filename: P5-F49.png
title_policy: 내부 전체 제목·그림 코드 금지

문제:
개념 구조·수치·화살표 또는 한글 손상이 있어 전면 재생성이 필요하다.

필수 수정:
통합 가이드의 `P5-F49` 상세 지침과 허용 텍스트를 그대로 적용.

통합 가이드 세부 지침:
문제

- 코드·제목 중복 외에 SFR 패널이 중복되고 PP·ST·TOE 관계가 모호하다.

정확한 구조

- `PP`: 제품 유형 공통 보안요구
- `ST`: 특정 TOE의 보안 주장
- `TOE`: 실제 평가대상
- `SFR`: 보안기능 요구사항
- `SAR`: 보증 요구사항
- `평가기관`: 평가 수행
- `인증기관`: 인증 결정
- `EAL`: 보증 패키지의 깊이·엄격성, 기능 우열 점수 아님

기본 프롬프트:
정보보안기사 시험 대비용 한국어 교육 도식이다.
원본의 학습 목적만 유지하고, 아래에 지정한 정확한 구조와 허용 텍스트로 새로 그린다.
흰 배경, 네이비·틸·밝은 회색 중심, 위험·오류만 빨강, 단순한 벡터 스타일.
화살표는 실제 데이터·제어 흐름에만 사용하고 방향을 정확히 맞춘다.
허용 텍스트 외의 문구, 워터마크, 프롬프트 문장, 파일명, 가짜 수식, 의미 없는 약어를 넣지 않는다.
출력 크기와 제목 정책은 해당 코드의 매니페스트를 따른다.

공통 네거티브:
no watermark, no prompt text, no placeholder text, no pseudo-Korean,
no misspelled Korean, no duplicate labels, no invented formula,
no tiny text, no decorative arrows, no gradient background,
no photorealistic style, no file name, no version string
```

## [A] P5-F53 · 정보보호 제품인증 의사결정 · 전면 재생성

```text
[A] P5-F53 · 정보보호 제품인증 의사결정 · 전면 재생성

input_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\01_전면재생성\Part5\P5-F53.png
output_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\03_수정완료\Part5\P5-F53.png
canvas: 1600 x 893 px
output_filename: P5-F53.png
title_policy: 내부 전체 제목·그림 코드 금지

문제:
개념 구조·수치·화살표 또는 한글 손상이 있어 전면 재생성이 필요하다.

필수 수정:
통합 가이드의 `P5-F53` 상세 지침과 허용 텍스트를 그대로 적용.

통합 가이드 세부 지침:
문제

- 제목과 패널 라벨이 깨졌다.

정확한 구조

- 질문 1: 평가대상이 조직의 관리체계인가? → `ISMS / ISMS-P`
- 질문 2: 평가대상이 특정 IT 보안제품의 기능·보증인가? → `CC`
- 하단: `인증은 평가 시점·범위·가정 안에서 신뢰를 제공하며 운영 중 변경을 자동 보증하지 않는다.`

기본 프롬프트:
정보보안기사 시험 대비용 한국어 교육 도식이다.
원본의 학습 목적만 유지하고, 아래에 지정한 정확한 구조와 허용 텍스트로 새로 그린다.
흰 배경, 네이비·틸·밝은 회색 중심, 위험·오류만 빨강, 단순한 벡터 스타일.
화살표는 실제 데이터·제어 흐름에만 사용하고 방향을 정확히 맞춘다.
허용 텍스트 외의 문구, 워터마크, 프롬프트 문장, 파일명, 가짜 수식, 의미 없는 약어를 넣지 않는다.
출력 크기와 제목 정책은 해당 코드의 매니페스트를 따른다.

공통 네거티브:
no watermark, no prompt text, no placeholder text, no pseudo-Korean,
no misspelled Korean, no duplicate labels, no invented formula,
no tiny text, no decorative arrows, no gradient background,
no photorealistic style, no file name, no version string
```

## [A] P5-F54 · 사이버 윤리 전체 지도 · 전면 재생성

```text
[A] P5-F54 · 사이버 윤리 전체 지도 · 전면 재생성

input_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\01_전면재생성\Part5\P5-F54.png
output_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\03_수정완료\Part5\P5-F54.png
canvas: 1600 x 893 px
output_filename: P5-F54.png
title_policy: 내부 전체 제목·그림 코드 금지

문제:
개념 구조·수치·화살표 또는 한글 손상이 있어 전면 재생성이 필요하다.

필수 수정:
통합 가이드의 `P5-F54` 상세 지침과 허용 텍스트를 그대로 적용.

통합 가이드 세부 지침:
문제

- 제목이 “사이버 윤회”로 깨지고 윤리 축이 중복·누락되어 있다.

정확한 6개 축

`책임`, `존중`, `공정`, `안전`, `프라이버시`, `지식재산`

중앙: `디지털 시민의 판단`

하단: `합법이라고 항상 윤리적인 것은 아니며, 표현의 자유와 타인의 권리를 함께 고려한다.`

기본 프롬프트:
정보보안기사 시험 대비용 한국어 교육 도식이다.
원본의 학습 목적만 유지하고, 아래에 지정한 정확한 구조와 허용 텍스트로 새로 그린다.
흰 배경, 네이비·틸·밝은 회색 중심, 위험·오류만 빨강, 단순한 벡터 스타일.
화살표는 실제 데이터·제어 흐름에만 사용하고 방향을 정확히 맞춘다.
허용 텍스트 외의 문구, 워터마크, 프롬프트 문장, 파일명, 가짜 수식, 의미 없는 약어를 넣지 않는다.
출력 크기와 제목 정책은 해당 코드의 매니페스트를 따른다.

공통 네거티브:
no watermark, no prompt text, no placeholder text, no pseudo-Korean,
no misspelled Korean, no duplicate labels, no invented formula,
no tiny text, no decorative arrows, no gradient background,
no photorealistic style, no file name, no version string
```

## [A] P5-F55 · 디지털 시민의 책임 · 전면 재생성

```text
[A] P5-F55 · 디지털 시민의 책임 · 전면 재생성

input_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\01_전면재생성\Part5\P5-F55.png
output_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\03_수정완료\Part5\P5-F55.png
canvas: 1600 x 893 px
output_filename: P5-F55.png
title_policy: 내부 전체 제목·그림 코드 금지

문제:
개념 구조·수치·화살표 또는 한글 손상이 있어 전면 재생성이 필요하다.

필수 수정:
통합 가이드의 `P5-F55` 상세 지침과 허용 텍스트를 그대로 적용.

통합 가이드 세부 지침:
문제

- 코드·제목과 함께 다수 문장이 깨졌다.

정확한 구조

- 게시 전: `사실 확인`, `동의·프라이버시`, `출처·저작권`, `보안 위험`
- 게시 후: `빠른 확산`, `검색 가능성`, `장기 잔존`, `2차 피해`
- 문제 발생 시: `증거 보존`, `신고`, `정정·삭제`, `피해자 보호`
- 하단: `익명성은 책임을 없애지 않는다.`

기본 프롬프트:
정보보안기사 시험 대비용 한국어 교육 도식이다.
원본의 학습 목적만 유지하고, 아래에 지정한 정확한 구조와 허용 텍스트로 새로 그린다.
흰 배경, 네이비·틸·밝은 회색 중심, 위험·오류만 빨강, 단순한 벡터 스타일.
화살표는 실제 데이터·제어 흐름에만 사용하고 방향을 정확히 맞춘다.
허용 텍스트 외의 문구, 워터마크, 프롬프트 문장, 파일명, 가짜 수식, 의미 없는 약어를 넣지 않는다.
출력 크기와 제목 정책은 해당 코드의 매니페스트를 따른다.

공통 네거티브:
no watermark, no prompt text, no placeholder text, no pseudo-Korean,
no misspelled Korean, no duplicate labels, no invented formula,
no tiny text, no decorative arrows, no gradient background,
no photorealistic style, no file name, no version string
```

## [A] P5-F64 · 국내 정보보호 법제 지도 · 전면 재생성

```text
[A] P5-F64 · 국내 정보보호 법제 지도 · 전면 재생성

input_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\01_전면재생성\Part5\P5-F64.png
output_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\03_수정완료\Part5\P5-F64.png
canvas: 1600 x 893 px
output_filename: P5-F64.png
title_policy: 내부 전체 제목·그림 코드 금지

문제:
개념 구조·수치·화살표 또는 한글 손상이 있어 전면 재생성이 필요하다.

필수 수정:
통합 가이드의 `P5-F64` 상세 지침과 허용 텍스트를 그대로 적용.

통합 가이드 세부 지침:
문제

- 영어 제목이 주제와 무관하고 법률명과 범위가 여러 곳 깨졌다.

정확한 법률 블록

- `정보통신망법`: 망 안정성, 침해행위·악성프로그램·서비스 방해, 불법정보·스팸, ISMS
- `정보통신기반 보호법`: 주요정보통신기반시설의 지정·보호
- `전자서명법`: 전자서명·인증서비스의 신뢰
- `개인정보 보호법`: 개인정보 처리와 정보주체 권리의 일반법
- `저작권법`: 디지털 저작권과 이용

법률 간 우열을 화살표로 표현하지 말고 `보호대상과 목적이 다름`을 중심에 둔다.

기본 프롬프트:
정보보안기사 시험 대비용 한국어 교육 도식이다.
원본의 학습 목적만 유지하고, 아래에 지정한 정확한 구조와 허용 텍스트로 새로 그린다.
흰 배경, 네이비·틸·밝은 회색 중심, 위험·오류만 빨강, 단순한 벡터 스타일.
화살표는 실제 데이터·제어 흐름에만 사용하고 방향을 정확히 맞춘다.
허용 텍스트 외의 문구, 워터마크, 프롬프트 문장, 파일명, 가짜 수식, 의미 없는 약어를 넣지 않는다.
출력 크기와 제목 정책은 해당 코드의 매니페스트를 따른다.

공통 네거티브:
no watermark, no prompt text, no placeholder text, no pseudo-Korean,
no misspelled Korean, no duplicate labels, no invented formula,
no tiny text, no decorative arrows, no gradient background,
no photorealistic style, no file name, no version string
```

## [A] P5-F68 · 주요정보통신기반시설 보호체계 · 전면 재생성

```text
[A] P5-F68 · 주요정보통신기반시설 보호체계 · 전면 재생성

input_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\01_전면재생성\Part5\P5-F68.png
output_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\03_수정완료\Part5\P5-F68.png
canvas: 1600 x 893 px
output_filename: P5-F68.png
title_policy: 내부 전체 제목·그림 코드 금지

문제:
개념 구조·수치·화살표 또는 한글 손상이 있어 전면 재생성이 필요하다.

필수 수정:
통합 가이드의 `P5-F68` 상세 지침과 허용 텍스트를 그대로 적용.

통합 가이드 세부 지침:
문제

- 제목과 기관 역할 라벨이 깨졌다.

정확한 주체

- `위원회`: 정책·조정
- `관계 중앙행정기관`: 지정·감독·지원
- `관리기관`: 취약점 분석·평가, 보호대책 수립·이행
- `전문기관`: 기술지원

보고·지원 화살표의 방향을 명확히 한다.

기본 프롬프트:
정보보안기사 시험 대비용 한국어 교육 도식이다.
원본의 학습 목적만 유지하고, 아래에 지정한 정확한 구조와 허용 텍스트로 새로 그린다.
흰 배경, 네이비·틸·밝은 회색 중심, 위험·오류만 빨강, 단순한 벡터 스타일.
화살표는 실제 데이터·제어 흐름에만 사용하고 방향을 정확히 맞춘다.
허용 텍스트 외의 문구, 워터마크, 프롬프트 문장, 파일명, 가짜 수식, 의미 없는 약어를 넣지 않는다.
출력 크기와 제목 정책은 해당 코드의 매니페스트를 따른다.

공통 네거티브:
no watermark, no prompt text, no placeholder text, no pseudo-Korean,
no misspelled Korean, no duplicate labels, no invented formula,
no tiny text, no decorative arrows, no gradient background,
no photorealistic style, no file name, no version string
```

## [A] P5-F73 · 전자서명법 현재와 역사 · 전면 재생성

```text
[A] P5-F73 · 전자서명법 현재와 역사 · 전면 재생성

input_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\01_전면재생성\Part5\P5-F73.png
output_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\03_수정완료\Part5\P5-F73.png
canvas: 1600 x 893 px
output_filename: P5-F73.png
title_policy: 내부 전체 제목·그림 코드 금지

문제:
개념 구조·수치·화살표 또는 한글 손상이 있어 전면 재생성이 필요하다.

필수 수정:
통합 가이드의 `P5-F73` 상세 지침과 허용 텍스트를 그대로 적용.

통합 가이드 세부 지침:
문제

- 제목과 역사·현행 비교 문구가 광범위하게 깨졌다.

정확한 구조

- 좌측 `2020년 제도 개편 전`: 공인전자서명·공인인증기관·공인인증서 중심의 역사적 표현
- 우측 `제도 개편 후`: 다양한 전자서명수단이 경쟁하는 기술중립적 체계
- 하단: `과거 기출 표현과 현행 제도를 구분`

기본 프롬프트:
정보보안기사 시험 대비용 한국어 교육 도식이다.
원본의 학습 목적만 유지하고, 아래에 지정한 정확한 구조와 허용 텍스트로 새로 그린다.
흰 배경, 네이비·틸·밝은 회색 중심, 위험·오류만 빨강, 단순한 벡터 스타일.
화살표는 실제 데이터·제어 흐름에만 사용하고 방향을 정확히 맞춘다.
허용 텍스트 외의 문구, 워터마크, 프롬프트 문장, 파일명, 가짜 수식, 의미 없는 약어를 넣지 않는다.
출력 크기와 제목 정책은 해당 코드의 매니페스트를 따른다.

공통 네거티브:
no watermark, no prompt text, no placeholder text, no pseudo-Korean,
no misspelled Korean, no duplicate labels, no invented formula,
no tiny text, no decorative arrows, no gradient background,
no photorealistic style, no file name, no version string
```

## [A] P5-F74 · 개인정보 보호법 전체 지도 · 전면 재생성

```text
[A] P5-F74 · 개인정보 보호법 전체 지도 · 전면 재생성

input_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\01_전면재생성\Part5\P5-F74.png
output_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\03_수정완료\Part5\P5-F74.png
canvas: 1600 x 893 px
output_filename: P5-F74.png
title_policy: 내부 전체 제목·그림 코드 금지

문제:
개념 구조·수치·화살표 또는 한글 손상이 있어 전면 재생성이 필요하다.

필수 수정:
통합 가이드의 `P5-F74` 상세 지침과 허용 텍스트를 그대로 적용.

통합 가이드 세부 지침:
문제

- 코드·제목 외에 권리·의무·안전조치 문구가 여러 곳 깨졌다.

정확한 6개 영역

`처리 원칙`, `처리 생명주기`, `정보주체 권리`, `개인정보처리자 의무`, `안전성 확보조치·침해대응`, `감독·구제`

중앙: `개인정보 보호법`

기본 프롬프트:
정보보안기사 시험 대비용 한국어 교육 도식이다.
원본의 학습 목적만 유지하고, 아래에 지정한 정확한 구조와 허용 텍스트로 새로 그린다.
흰 배경, 네이비·틸·밝은 회색 중심, 위험·오류만 빨강, 단순한 벡터 스타일.
화살표는 실제 데이터·제어 흐름에만 사용하고 방향을 정확히 맞춘다.
허용 텍스트 외의 문구, 워터마크, 프롬프트 문장, 파일명, 가짜 수식, 의미 없는 약어를 넣지 않는다.
출력 크기와 제목 정책은 해당 코드의 매니페스트를 따른다.

공통 네거티브:
no watermark, no prompt text, no placeholder text, no pseudo-Korean,
no misspelled Korean, no duplicate labels, no invented formula,
no tiny text, no decorative arrows, no gradient background,
no photorealistic style, no file name, no version string
```

## [A] P5-F77 · 개인정보 처리 생명주기와 적법 근거 · 전면 재생성

```text
[A] P5-F77 · 개인정보 처리 생명주기와 적법 근거 · 전면 재생성

input_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\01_전면재생성\Part5\P5-F77.png
output_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\03_수정완료\Part5\P5-F77.png
canvas: 1600 x 893 px
output_filename: P5-F77.png
title_policy: 내부 전체 제목·그림 코드 금지

문제:
개념 구조·수치·화살표 또는 한글 손상이 있어 전면 재생성이 필요하다.

필수 수정:
통합 가이드의 `P5-F77` 상세 지침과 허용 텍스트를 그대로 적용.

통합 가이드 세부 지침:
문제

- 제목과 단계 라벨이 깨졌다.

정확한 구조

`수집 → 이용 → 제공·위탁 → 보관 → 권리행사 대응·정정 → 파기`

각 단계 아래 공통 통제

`적법한 근거`, `목적 제한`, `최소 수집`, `투명성`, `안전조치`, `처리기록`, `보유기간 종료 시 지체 없이 파기`

기본 프롬프트:
정보보안기사 시험 대비용 한국어 교육 도식이다.
원본의 학습 목적만 유지하고, 아래에 지정한 정확한 구조와 허용 텍스트로 새로 그린다.
흰 배경, 네이비·틸·밝은 회색 중심, 위험·오류만 빨강, 단순한 벡터 스타일.
화살표는 실제 데이터·제어 흐름에만 사용하고 방향을 정확히 맞춘다.
허용 텍스트 외의 문구, 워터마크, 프롬프트 문장, 파일명, 가짜 수식, 의미 없는 약어를 넣지 않는다.
출력 크기와 제목 정책은 해당 코드의 매니페스트를 따른다.

공통 네거티브:
no watermark, no prompt text, no placeholder text, no pseudo-Korean,
no misspelled Korean, no duplicate labels, no invented formula,
no tiny text, no decorative arrows, no gradient background,
no photorealistic style, no file name, no version string
```

## [A] P5-F83 · 개인정보 처리방침 · 전면 재생성

```text
[A] P5-F83 · 개인정보 처리방침 · 전면 재생성

input_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\01_전면재생성\Part5\P5-F83.png
output_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\03_수정완료\Part5\P5-F83.png
canvas: 1600 x 893 px
output_filename: P5-F83.png
title_policy: 내부 전체 제목·그림 코드 금지

문제:
개념 구조·수치·화살표 또는 한글 손상이 있어 전면 재생성이 필요하다.

필수 수정:
통합 가이드의 `P5-F83` 상세 지침과 허용 텍스트를 그대로 적용.

통합 가이드 세부 지침:
문제

- 제목과 표 항목이 다수 깨졌다.

정확한 항목

`처리 목적`, `처리 항목`, `보유기간`, `제3자 제공`, `처리위탁`, `파기`, `정보주체 권리`, `안전성 확보조치`, `개인정보 보호책임자·연락처`, `자동수집·쿠키(해당 시)`, `변경 이력`

하단: `처리방침은 실제 처리와 일치해야 하며 동의를 대신하지 않는다.`

---

기본 프롬프트:
정보보안기사 시험 대비용 한국어 교육 도식이다.
원본의 학습 목적만 유지하고, 아래에 지정한 정확한 구조와 허용 텍스트로 새로 그린다.
흰 배경, 네이비·틸·밝은 회색 중심, 위험·오류만 빨강, 단순한 벡터 스타일.
화살표는 실제 데이터·제어 흐름에만 사용하고 방향을 정확히 맞춘다.
허용 텍스트 외의 문구, 워터마크, 프롬프트 문장, 파일명, 가짜 수식, 의미 없는 약어를 넣지 않는다.
출력 크기와 제목 정책은 해당 코드의 매니페스트를 따른다.

공통 네거티브:
no watermark, no prompt text, no placeholder text, no pseudo-Korean,
no misspelled Korean, no duplicate labels, no invented formula,
no tiny text, no decorative arrows, no gradient background,
no photorealistic style, no file name, no version string
```

## [B] P1-F24 · UNIX/Linux 권한과 8진수 계산 · 부분 수정

```text
[B] P1-F24 · UNIX/Linux 권한과 8진수 계산 · 부분 수정

input_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\02_부분수정\Part1\P1-F24.png
output_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\03_수정완료\Part1\P1-F24.png
canvas: 2048 x 1136 px
output_filename: P1-F24.png
title_policy: 내부 전체 제목 1개 유지, 그림 코드 금지

문제:
상단 권한 합산 주석이 혼동을 일으킨다. 본체 계산값은 맞으므로 해당 주석만 교체한다.

필수 수정:
상단 주석을 `rwx=4+2+1=7`, `r-x=4+0+1=5`, `---=0+0+0=0`으로 교체. 나머지 구조와 내부 전체 제목은 유지.

통합 가이드 세부 지침: CSV required_correction을 따른다.

기본 프롬프트:
마스킹하지 않은 픽셀, 구도, 아이콘, 선, 화살표, 색상, 여백, 정확한 문구를 그대로 유지한다.
마스킹 영역의 코드·중복 제목·오탈자·잘못된 짧은 라벨만 삭제하거나 지정 문자열로 교체한다.
삭제 영역은 원래 흰 배경과 기존 테두리를 자연스럽게 복원한다.
새 제목, 새 코드, 워터마크, 생성 지시문, 설명문을 추가하지 않는다.
마스킹 영역 밖은 변경하지 않는다.
원본 픽셀 크기를 유지한다.

공통 네거티브:
no watermark, no prompt text, no placeholder text, no pseudo-Korean,
no misspelled Korean, no duplicate labels, no invented formula,
no tiny text, no decorative arrows, no gradient background,
no photorealistic style, no file name, no version string
```

## [B] P1-F30 · 이벤트 상관분석 타임라인 · 부분 수정

```text
[B] P1-F30 · 이벤트 상관분석 타임라인 · 부분 수정

input_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\02_부분수정\Part1\P1-F30.png
output_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\03_수정완료\Part1\P1-F30.png
canvas: 2048 x 1210 px
output_filename: P1-F30.png
title_policy: 내부 전체 제목 1개 유지, 그림 코드 금지

문제:
첫 번째 로그인 실패 상자와 타임라인 선·노드가 겹친다.

필수 수정:
첫 상자만 위로 이동하거나 높이를 줄여 선·노드와 겹치지 않게 조정. 다른 픽셀과 내부 제목 유지.

통합 가이드 세부 지침: CSV required_correction을 따른다.

기본 프롬프트:
마스킹하지 않은 픽셀, 구도, 아이콘, 선, 화살표, 색상, 여백, 정확한 문구를 그대로 유지한다.
마스킹 영역의 코드·중복 제목·오탈자·잘못된 짧은 라벨만 삭제하거나 지정 문자열로 교체한다.
삭제 영역은 원래 흰 배경과 기존 테두리를 자연스럽게 복원한다.
새 제목, 새 코드, 워터마크, 생성 지시문, 설명문을 추가하지 않는다.
마스킹 영역 밖은 변경하지 않는다.
원본 픽셀 크기를 유지한다.

공통 네거티브:
no watermark, no prompt text, no placeholder text, no pseudo-Korean,
no misspelled Korean, no duplicate labels, no invented formula,
no tiny text, no decorative arrows, no gradient background,
no photorealistic style, no file name, no version string
```

## [B] P2-F14 · 서브넷팅·CIDR·VLSM · 전면 재생성

```text
[B] P2-F14 · 서브넷팅·CIDR·VLSM · 전면 재생성

input_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\01_전면재생성\Part2\P2-F14.png
output_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\03_수정완료\Part2\P2-F14.png
canvas: 1600 x 850 px
output_filename: P2-F14.png
title_policy: 내부 전체 제목·그림 코드 금지

문제:
한 /24에서 /25·/26·/27이 동시에 분기하여 중첩 VLSM 배정처럼 보인다.

필수 수정:
`192.168.10.0/24`를 `/25`, `/26`, `/27`, 남은 `/27`로 비중첩 순차 배정. 큰 요구부터, 경계 정렬, 중첩 금지 표시.

통합 가이드 세부 지침:
`192.168.10.0/24`를 중첩 없이 순차 배정한다.

- 100호스트: `192.168.10.0/25`, 사용 가능 `.1~.126`, Broadcast `.127`
- 50호스트: `192.168.10.128/26`, `.129~.190`, Broadcast `.191`
- 20호스트: `192.168.10.192/27`, `.193~.222`, Broadcast `.223`
- 남은 공간: `192.168.10.224/27`
- 하단: `큰 요구부터 배정`, `경계 정렬`, `중첩 금지`

기본 프롬프트:
정보보안기사 시험 대비용 한국어 교육 도식이다.
원본의 학습 목적만 유지하고, 아래에 지정한 정확한 구조와 허용 텍스트로 새로 그린다.
흰 배경, 네이비·틸·밝은 회색 중심, 위험·오류만 빨강, 단순한 벡터 스타일.
화살표는 실제 데이터·제어 흐름에만 사용하고 방향을 정확히 맞춘다.
허용 텍스트 외의 문구, 워터마크, 프롬프트 문장, 파일명, 가짜 수식, 의미 없는 약어를 넣지 않는다.
출력 크기와 제목 정책은 해당 코드의 매니페스트를 따른다.

공통 네거티브:
no watermark, no prompt text, no placeholder text, no pseudo-Korean,
no misspelled Korean, no duplicate labels, no invented formula,
no tiny text, no decorative arrows, no gradient background,
no photorealistic style, no file name, no version string
```

## [B] P2-F18 · IPv6 NDP와 전환 기술 · 전면 재생성

```text
[B] P2-F18 · IPv6 NDP와 전환 기술 · 전면 재생성

input_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\01_전면재생성\Part2\P2-F18.png
output_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\03_수정완료\Part2\P2-F18.png
canvas: 1600 x 850 px
output_filename: P2-F18.png
title_policy: 내부 전체 제목·그림 코드 금지

문제:
RS/RA와 NS/NA의 통신 상대가 시각적으로 섞여 NDP 기능이 모호하다.

필수 수정:
호스트↔라우터 `RS/RA`, 호스트↔이웃 `NS/NA`, `DAD`를 분리. 하단은 Dual Stack/Tunneling/Translation을 별도 패널로 유지.

통합 가이드 세부 지침:
- `호스트 ↔ 라우터`: RS, RA
- `호스트 ↔ 이웃`: NS, NA
- `DAD`: 주소 중복 확인
- 하단은 `Dual Stack`, `Tunneling`, `Translation(NAT64/DNS64)`을 별도 패널로 둔다.

기본 프롬프트:
정보보안기사 시험 대비용 한국어 교육 도식이다.
원본의 학습 목적만 유지하고, 아래에 지정한 정확한 구조와 허용 텍스트로 새로 그린다.
흰 배경, 네이비·틸·밝은 회색 중심, 위험·오류만 빨강, 단순한 벡터 스타일.
화살표는 실제 데이터·제어 흐름에만 사용하고 방향을 정확히 맞춘다.
허용 텍스트 외의 문구, 워터마크, 프롬프트 문장, 파일명, 가짜 수식, 의미 없는 약어를 넣지 않는다.
출력 크기와 제목 정책은 해당 코드의 매니페스트를 따른다.

공통 네거티브:
no watermark, no prompt text, no placeholder text, no pseudo-Korean,
no misspelled Korean, no duplicate labels, no invented formula,
no tiny text, no decorative arrows, no gradient background,
no photorealistic style, no file name, no version string
```

## [B] P2-F21 · ICMP·IGMP와 전송 범위 · 부분 수정

```text
[B] P2-F21 · ICMP·IGMP와 전송 범위 · 부분 수정

input_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\02_부분수정\Part2\P2-F21.png
output_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\03_수정완료\Part2\P2-F21.png
canvas: 1600 x 850 px
output_filename: P2-F21.png
title_policy: 내부 전체 제목·그림 코드 금지

문제:
ping·traceroute 설명이 IGMP 영역에 들어가 있고 Anycast를 지리적으로 가장 가까운 노드처럼 단정한다.

필수 수정:
ping·traceroute 설명을 ICMP 영역으로 이동. Anycast는 `동일 주소를 광고한 노드 중 라우팅상 가까운/최적 1곳`으로 교체.

통합 가이드 세부 지침: CSV required_correction을 따른다.

기본 프롬프트:
마스킹하지 않은 픽셀, 구도, 아이콘, 선, 화살표, 색상, 여백, 정확한 문구를 그대로 유지한다.
마스킹 영역의 코드·중복 제목·오탈자·잘못된 짧은 라벨만 삭제하거나 지정 문자열로 교체한다.
삭제 영역은 원래 흰 배경과 기존 테두리를 자연스럽게 복원한다.
새 제목, 새 코드, 워터마크, 생성 지시문, 설명문을 추가하지 않는다.
마스킹 영역 밖은 변경하지 않는다.
원본 픽셀 크기를 유지한다.

공통 네거티브:
no watermark, no prompt text, no placeholder text, no pseudo-Korean,
no misspelled Korean, no duplicate labels, no invented formula,
no tiny text, no decorative arrows, no gradient background,
no photorealistic style, no file name, no version string
```

## [B] P2-F33 · 무선 공격과 대응 지도 · 부분 수정

```text
[B] P2-F33 · 무선 공격과 대응 지도 · 부분 수정

input_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\02_부분수정\Part2\P2-F33.png
output_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\03_수정완료\Part2\P2-F33.png
canvas: 1600 x 850 px
output_filename: P2-F33.png
title_policy: 내부 전체 제목·그림 코드 금지

문제:
KRACK·PMF·Rogue AP·Evil Twin 방어의 대응 관계가 섞여 있다.

필수 수정:
PMF는 deauth/disassoc 완화, WIDS/WIPS·AP inventory는 Rogue/Evil Twin, 패치·안전한 구현은 KRACK, 링크 암호화는 스니핑 완화로 정확히 연결.

통합 가이드 세부 지침: CSV required_correction을 따른다.

기본 프롬프트:
마스킹하지 않은 픽셀, 구도, 아이콘, 선, 화살표, 색상, 여백, 정확한 문구를 그대로 유지한다.
마스킹 영역의 코드·중복 제목·오탈자·잘못된 짧은 라벨만 삭제하거나 지정 문자열로 교체한다.
삭제 영역은 원래 흰 배경과 기존 테두리를 자연스럽게 복원한다.
새 제목, 새 코드, 워터마크, 생성 지시문, 설명문을 추가하지 않는다.
마스킹 영역 밖은 변경하지 않는다.
원본 픽셀 크기를 유지한다.

공통 네거티브:
no watermark, no prompt text, no placeholder text, no pseudo-Korean,
no misspelled Korean, no duplicate labels, no invented formula,
no tiny text, no decorative arrows, no gradient background,
no photorealistic style, no file name, no version string
```

## [B] P2-F64 · AH·ESP와 Transport·Tunnel 모드 · 부분 수정

```text
[B] P2-F64 · AH·ESP와 Transport·Tunnel 모드 · 부분 수정

input_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\02_부분수정\Part2\P2-F64.png
output_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\03_수정완료\Part2\P2-F64.png
canvas: 1600 x 850 px
output_filename: P2-F64.png
title_policy: 내부 전체 제목·그림 코드 금지

문제:
AH가 IP 헤더 전체를 보호하는 것처럼 읽히고 Transport/Tunnel 사용 범위를 절대적으로 표현한다.

필수 수정:
AH는 변하지 않는 IP 헤더 필드와 Payload를 인증하며 전송 중 변경되는 필드는 제외한다고 명시. Transport/Tunnel은 대표 사용 예로 표현.

통합 가이드 세부 지침: CSV required_correction을 따른다.

기본 프롬프트:
마스킹하지 않은 픽셀, 구도, 아이콘, 선, 화살표, 색상, 여백, 정확한 문구를 그대로 유지한다.
마스킹 영역의 코드·중복 제목·오탈자·잘못된 짧은 라벨만 삭제하거나 지정 문자열로 교체한다.
삭제 영역은 원래 흰 배경과 기존 테두리를 자연스럽게 복원한다.
새 제목, 새 코드, 워터마크, 생성 지시문, 설명문을 추가하지 않는다.
마스킹 영역 밖은 변경하지 않는다.
원본 픽셀 크기를 유지한다.

공통 네거티브:
no watermark, no prompt text, no placeholder text, no pseudo-Korean,
no misspelled Korean, no duplicate labels, no invented formula,
no tiny text, no decorative arrows, no gradient background,
no photorealistic style, no file name, no version string
```

## [B] P3-F28 · 입력·출력·상태 경계 공격 지도 · 부분 수정

```text
[B] P3-F28 · 입력·출력·상태 경계 공격 지도 · 부분 수정

input_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\02_부분수정\Part3\P3-F28.png
output_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\03_수정완료\Part3\P3-F28.png
canvas: 1800 x 1004 px
output_filename: P3-F28.png
title_policy: 내부 전체 제목·그림 코드 금지

문제:
깨진 제목과 “특수문자 이스케이프”의 과도한 일반화가 남아 있다.

필수 수정:
상단 깨진 제목 삭제. 해석기별 대응을 유지하고 모든 공격에 공통인 것처럼 보이는 `특수문자 이스케이프` 문구를 `문맥별 안전 API·파라미터화·출력 인코딩`으로 교체.

통합 가이드 세부 지침: CSV required_correction을 따른다.

기본 프롬프트:
마스킹하지 않은 픽셀, 구도, 아이콘, 선, 화살표, 색상, 여백, 정확한 문구를 그대로 유지한다.
마스킹 영역의 코드·중복 제목·오탈자·잘못된 짧은 라벨만 삭제하거나 지정 문자열로 교체한다.
삭제 영역은 원래 흰 배경과 기존 테두리를 자연스럽게 복원한다.
새 제목, 새 코드, 워터마크, 생성 지시문, 설명문을 추가하지 않는다.
마스킹 영역 밖은 변경하지 않는다.
원본 픽셀 크기를 유지한다.

공통 네거티브:
no watermark, no prompt text, no placeholder text, no pseudo-Korean,
no misspelled Korean, no duplicate labels, no invented formula,
no tiny text, no decorative arrows, no gradient background,
no photorealistic style, no file name, no version string
```

## [B] P3-F55 · DB 감사·백업·복구 · 부분 수정

```text
[B] P3-F55 · DB 감사·백업·복구 · 부분 수정

input_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\02_부분수정\Part3\P3-F55.png
output_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\03_수정완료\Part3\P3-F55.png
canvas: 1800 x 1004 px
output_filename: P3-F55.png
title_policy: 내부 전체 제목·그림 코드 금지

문제:
상단 잘못된 교재 제목과 “시험 주성 포인” 오탈자가 남아 있다.

필수 수정:
상단 `정보보안 인증 교제`를 삭제하고 `시험 주성 포인`을 `시험 핵심 포인트`로 교체. 나머지 유지.

통합 가이드 세부 지침: CSV required_correction을 따른다.

기본 프롬프트:
마스킹하지 않은 픽셀, 구도, 아이콘, 선, 화살표, 색상, 여백, 정확한 문구를 그대로 유지한다.
마스킹 영역의 코드·중복 제목·오탈자·잘못된 짧은 라벨만 삭제하거나 지정 문자열로 교체한다.
삭제 영역은 원래 흰 배경과 기존 테두리를 자연스럽게 복원한다.
새 제목, 새 코드, 워터마크, 생성 지시문, 설명문을 추가하지 않는다.
마스킹 영역 밖은 변경하지 않는다.
원본 픽셀 크기를 유지한다.

공통 네거티브:
no watermark, no prompt text, no placeholder text, no pseudo-Korean,
no misspelled Korean, no duplicate labels, no invented formula,
no tiny text, no decorative arrows, no gradient background,
no photorealistic style, no file name, no version string
```

## [B] P3-F68 · 입력검증·출력인코딩·인증·세션 보안 · 부분 수정

```text
[B] P3-F68 · 입력검증·출력인코딩·인증·세션 보안 · 부분 수정

input_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\02_부분수정\Part3\P3-F68.png
output_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\03_수정완료\Part3\P3-F68.png
canvas: 1800 x 1004 px
output_filename: P3-F68.png
title_policy: 내부 전체 제목·그림 코드 금지

문제:
깨진 제목과 일부 라벨을 정리하면 구조를 유지할 수 있다.

필수 수정:
상단 깨진 전체 제목을 삭제하고 일부 깨진 라벨만 본문 용어에 맞게 교체. 입력검증·출력인코딩·인증·인가·세션의 구분은 유지.

통합 가이드 세부 지침: CSV required_correction을 따른다.

기본 프롬프트:
마스킹하지 않은 픽셀, 구도, 아이콘, 선, 화살표, 색상, 여백, 정확한 문구를 그대로 유지한다.
마스킹 영역의 코드·중복 제목·오탈자·잘못된 짧은 라벨만 삭제하거나 지정 문자열로 교체한다.
삭제 영역은 원래 흰 배경과 기존 테두리를 자연스럽게 복원한다.
새 제목, 새 코드, 워터마크, 생성 지시문, 설명문을 추가하지 않는다.
마스킹 영역 밖은 변경하지 않는다.
원본 픽셀 크기를 유지한다.

공통 네거티브:
no watermark, no prompt text, no placeholder text, no pseudo-Korean,
no misspelled Korean, no duplicate labels, no invented formula,
no tiny text, no decorative arrows, no gradient background,
no photorealistic style, no file name, no version string
```

## [B] P4-F75 · 서명·디지털봉투 결합 보안메시지 · 부분 수정

```text
[B] P4-F75 · 서명·디지털봉투 결합 보안메시지 · 부분 수정

input_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\02_부분수정\Part4\P4-F75.png
output_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\03_수정완료\Part4\P4-F75.png
canvas: 1600 x 893 px
output_filename: P4-F75.png
title_policy: 내부 전체 제목·그림 코드 금지

문제:
그림 내부 코드·중복 제목·지시문 또는 국소 오탈자가 남아 있다.

필수 수정:
상단 코드·전체 제목 삭제. `시컴 포인트`를 `시험 포인트`로 교체.

통합 가이드 세부 지침: CSV required_correction을 따른다.

기본 프롬프트:
마스킹하지 않은 픽셀, 구도, 아이콘, 선, 화살표, 색상, 여백, 정확한 문구를 그대로 유지한다.
마스킹 영역의 코드·중복 제목·오탈자·잘못된 짧은 라벨만 삭제하거나 지정 문자열로 교체한다.
삭제 영역은 원래 흰 배경과 기존 테두리를 자연스럽게 복원한다.
새 제목, 새 코드, 워터마크, 생성 지시문, 설명문을 추가하지 않는다.
마스킹 영역 밖은 변경하지 않는다.
원본 픽셀 크기를 유지한다.

공통 네거티브:
no watermark, no prompt text, no placeholder text, no pseudo-Korean,
no misspelled Korean, no duplicate labels, no invented formula,
no tiny text, no decorative arrows, no gradient background,
no photorealistic style, no file name, no version string
```

## [B] P5-F40 · 연계보관성 Chain of Custody · 부분 수정

```text
[B] P5-F40 · 연계보관성 Chain of Custody · 부분 수정

input_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\02_부분수정\Part5\P5-F40.png
output_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\03_수정완료\Part5\P5-F40.png
canvas: 1600 x 893 px
output_filename: P5-F40.png
title_policy: 내부 전체 제목·그림 코드 금지

문제:
그림 내부 코드·중복 제목·지시문 또는 국소 오탈자가 남아 있다.

필수 수정:
상단 코드·전체 제목과 `Only for descriptive purposes...` 지시문을 완전히 삭제. 나머지 연계보관 흐름은 유지.

통합 가이드 세부 지침: CSV required_correction을 따른다.

기본 프롬프트:
마스킹하지 않은 픽셀, 구도, 아이콘, 선, 화살표, 색상, 여백, 정확한 문구를 그대로 유지한다.
마스킹 영역의 코드·중복 제목·오탈자·잘못된 짧은 라벨만 삭제하거나 지정 문자열로 교체한다.
삭제 영역은 원래 흰 배경과 기존 테두리를 자연스럽게 복원한다.
새 제목, 새 코드, 워터마크, 생성 지시문, 설명문을 추가하지 않는다.
마스킹 영역 밖은 변경하지 않는다.
원본 픽셀 크기를 유지한다.

공통 네거티브:
no watermark, no prompt text, no placeholder text, no pseudo-Korean,
no misspelled Korean, no duplicate labels, no invented formula,
no tiny text, no decorative arrows, no gradient background,
no photorealistic style, no file name, no version string
```

## [C] P1-F42 · 파일·명령 실행 취약점 비교 · 부분 수정

```text
[C] P1-F42 · 파일·명령 실행 취약점 비교 · 부분 수정

input_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\02_부분수정\Part1\P1-F42.png
output_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\03_수정완료\Part1\P1-F42.png
canvas: 2048 x 1136 px
output_filename: P1-F42.png
title_policy: 내부 전체 제목 1개 유지, 그림 코드 금지

문제:
기술적으로는 대체로 맞지만 영문 소형문자가 많아 한국어 교재의 본문 크기에서 가독성이 낮다.

필수 수정:
구조는 유지하고 작은 영문 핵심 라벨을 `경로 조작`, `파일 포함(LFI/RFI)`, `파일 업로드`, `명령어 삽입`, `허용목록`, `기준 경로`, `비실행 저장`, `셸 호출 회피` 등으로 한국어화. 우선순위 C.

통합 가이드 세부 지침: CSV required_correction을 따른다.

기본 프롬프트:
마스킹하지 않은 픽셀, 구도, 아이콘, 선, 화살표, 색상, 여백, 정확한 문구를 그대로 유지한다.
마스킹 영역의 코드·중복 제목·오탈자·잘못된 짧은 라벨만 삭제하거나 지정 문자열로 교체한다.
삭제 영역은 원래 흰 배경과 기존 테두리를 자연스럽게 복원한다.
새 제목, 새 코드, 워터마크, 생성 지시문, 설명문을 추가하지 않는다.
마스킹 영역 밖은 변경하지 않는다.
원본 픽셀 크기를 유지한다.

공통 네거티브:
no watermark, no prompt text, no placeholder text, no pseudo-Korean,
no misspelled Korean, no duplicate labels, no invented formula,
no tiny text, no decorative arrows, no gradient background,
no photorealistic style, no file name, no version string
```

## [C] P2-F05 · Ethernet 프레임과 MAC 주소 · 부분 수정

```text
[C] P2-F05 · Ethernet 프레임과 MAC 주소 · 부분 수정

input_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\02_부분수정\Part2\P2-F05.png
output_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\03_수정완료\Part2\P2-F05.png
canvas: 2816 x 1536 px
output_filename: P2-F05.png
title_policy: 내부 전체 제목·그림 코드 금지

문제:
외부 캡션과 중복되는 그림 내부 전체 제목이 남아 있다.

필수 수정:
상단 내부 전체 제목·코드만 삭제. 프레임 필드와 MAC 설명은 그대로 유지.

통합 가이드 세부 지침: CSV required_correction을 따른다.

기본 프롬프트:
마스킹하지 않은 픽셀, 구도, 아이콘, 선, 화살표, 색상, 여백, 정확한 문구를 그대로 유지한다.
마스킹 영역의 코드·중복 제목·오탈자·잘못된 짧은 라벨만 삭제하거나 지정 문자열로 교체한다.
삭제 영역은 원래 흰 배경과 기존 테두리를 자연스럽게 복원한다.
새 제목, 새 코드, 워터마크, 생성 지시문, 설명문을 추가하지 않는다.
마스킹 영역 밖은 변경하지 않는다.
원본 픽셀 크기를 유지한다.

공통 네거티브:
no watermark, no prompt text, no placeholder text, no pseudo-Korean,
no misspelled Korean, no duplicate labels, no invented formula,
no tiny text, no decorative arrows, no gradient background,
no photorealistic style, no file name, no version string
```

## [C] P3-F01 · 애플리케이션보안 출제범위 전체 지도 · 부분 수정

```text
[C] P3-F01 · 애플리케이션보안 출제범위 전체 지도 · 부분 수정

input_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\02_부분수정\Part3\P3-F01.png
output_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\03_수정완료\Part3\P3-F01.png
canvas: 1800 x 1004 px
output_filename: P3-F01.png
title_policy: 내부 전체 제목·그림 코드 금지

문제:
외부 캡션과 중복되는 전체 제목·코드를 제거해야 한다.

필수 수정:
상단 전체 제목·코드만 삭제. 패널 본체 유지.

통합 가이드 세부 지침: CSV required_correction을 따른다.

기본 프롬프트:
마스킹하지 않은 픽셀, 구도, 아이콘, 선, 화살표, 색상, 여백, 정확한 문구를 그대로 유지한다.
마스킹 영역의 코드·중복 제목·오탈자·잘못된 짧은 라벨만 삭제하거나 지정 문자열로 교체한다.
삭제 영역은 원래 흰 배경과 기존 테두리를 자연스럽게 복원한다.
새 제목, 새 코드, 워터마크, 생성 지시문, 설명문을 추가하지 않는다.
마스킹 영역 밖은 변경하지 않는다.
원본 픽셀 크기를 유지한다.

공통 네거티브:
no watermark, no prompt text, no placeholder text, no pseudo-Korean,
no misspelled Korean, no duplicate labels, no invented formula,
no tiny text, no decorative arrows, no gradient background,
no photorealistic style, no file name, no version string
```

## [C] P3-F02 · 애플리케이션 신뢰경계와 데이터 흐름 · 부분 수정

```text
[C] P3-F02 · 애플리케이션 신뢰경계와 데이터 흐름 · 부분 수정

input_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\02_부분수정\Part3\P3-F02.png
output_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\03_수정완료\Part3\P3-F02.png
canvas: 1800 x 1004 px
output_filename: P3-F02.png
title_policy: 내부 전체 제목·그림 코드 금지

문제:
외부 캡션과 중복되는 전체 제목·코드를 제거해야 한다.

필수 수정:
상단 전체 제목·코드만 삭제. 패널 본체 유지.

통합 가이드 세부 지침: CSV required_correction을 따른다.

기본 프롬프트:
마스킹하지 않은 픽셀, 구도, 아이콘, 선, 화살표, 색상, 여백, 정확한 문구를 그대로 유지한다.
마스킹 영역의 코드·중복 제목·오탈자·잘못된 짧은 라벨만 삭제하거나 지정 문자열로 교체한다.
삭제 영역은 원래 흰 배경과 기존 테두리를 자연스럽게 복원한다.
새 제목, 새 코드, 워터마크, 생성 지시문, 설명문을 추가하지 않는다.
마스킹 영역 밖은 변경하지 않는다.
원본 픽셀 크기를 유지한다.

공통 네거티브:
no watermark, no prompt text, no placeholder text, no pseudo-Korean,
no misspelled Korean, no duplicate labels, no invented formula,
no tiny text, no decorative arrows, no gradient background,
no photorealistic style, no file name, no version string
```

## [C] P3-F03 · FTP 제어 채널과 데이터 채널 · 부분 수정

```text
[C] P3-F03 · FTP 제어 채널과 데이터 채널 · 부분 수정

input_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\02_부분수정\Part3\P3-F03.png
output_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\03_수정완료\Part3\P3-F03.png
canvas: 1800 x 1004 px
output_filename: P3-F03.png
title_policy: 내부 전체 제목·그림 코드 금지

문제:
상단 제목이 깨졌고 “디렉터리 목록 목록” 중복 문구가 있다.

필수 수정:
상단 깨진 제목·코드를 삭제하고 `디렉터리 목록 목록`을 `디렉터리 목록`으로 교체.

통합 가이드 세부 지침: CSV required_correction을 따른다.

기본 프롬프트:
마스킹하지 않은 픽셀, 구도, 아이콘, 선, 화살표, 색상, 여백, 정확한 문구를 그대로 유지한다.
마스킹 영역의 코드·중복 제목·오탈자·잘못된 짧은 라벨만 삭제하거나 지정 문자열로 교체한다.
삭제 영역은 원래 흰 배경과 기존 테두리를 자연스럽게 복원한다.
새 제목, 새 코드, 워터마크, 생성 지시문, 설명문을 추가하지 않는다.
마스킹 영역 밖은 변경하지 않는다.
원본 픽셀 크기를 유지한다.

공통 네거티브:
no watermark, no prompt text, no placeholder text, no pseudo-Korean,
no misspelled Korean, no duplicate labels, no invented formula,
no tiny text, no decorative arrows, no gradient background,
no photorealistic style, no file name, no version string
```

## [C] P3-F17 · 메일 위협과 다층 방어 · 부분 수정

```text
[C] P3-F17 · 메일 위협과 다층 방어 · 부분 수정

input_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\02_부분수정\Part3\P3-F17.png
output_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\03_수정완료\Part3\P3-F17.png
canvas: 1800 x 1004 px
output_filename: P3-F17.png
title_policy: 내부 전체 제목·그림 코드 금지

문제:
외부 캡션과 중복되는 전체 제목·코드를 제거해야 한다.

필수 수정:
상단 전체 제목·코드만 삭제. 본체 유지.

통합 가이드 세부 지침: CSV required_correction을 따른다.

기본 프롬프트:
마스킹하지 않은 픽셀, 구도, 아이콘, 선, 화살표, 색상, 여백, 정확한 문구를 그대로 유지한다.
마스킹 영역의 코드·중복 제목·오탈자·잘못된 짧은 라벨만 삭제하거나 지정 문자열로 교체한다.
삭제 영역은 원래 흰 배경과 기존 테두리를 자연스럽게 복원한다.
새 제목, 새 코드, 워터마크, 생성 지시문, 설명문을 추가하지 않는다.
마스킹 영역 밖은 변경하지 않는다.
원본 픽셀 크기를 유지한다.

공통 네거티브:
no watermark, no prompt text, no placeholder text, no pseudo-Korean,
no misspelled Korean, no duplicate labels, no invented formula,
no tiny text, no decorative arrows, no gradient background,
no photorealistic style, no file name, no version string
```

## [C] P3-F21 · 쿠키 기반 세션 흐름 · 부분 수정

```text
[C] P3-F21 · 쿠키 기반 세션 흐름 · 부분 수정

input_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\02_부분수정\Part3\P3-F21.png
output_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\03_수정완료\Part3\P3-F21.png
canvas: 1800 x 1004 px
output_filename: P3-F21.png
title_policy: 내부 전체 제목·그림 코드 금지

문제:
외부 캡션과 중복되는 전체 제목·코드를 제거해야 한다.

필수 수정:
상단 전체 제목·코드만 삭제. 본체 유지.

통합 가이드 세부 지침: CSV required_correction을 따른다.

기본 프롬프트:
마스킹하지 않은 픽셀, 구도, 아이콘, 선, 화살표, 색상, 여백, 정확한 문구를 그대로 유지한다.
마스킹 영역의 코드·중복 제목·오탈자·잘못된 짧은 라벨만 삭제하거나 지정 문자열로 교체한다.
삭제 영역은 원래 흰 배경과 기존 테두리를 자연스럽게 복원한다.
새 제목, 새 코드, 워터마크, 생성 지시문, 설명문을 추가하지 않는다.
마스킹 영역 밖은 변경하지 않는다.
원본 픽셀 크기를 유지한다.

공통 네거티브:
no watermark, no prompt text, no placeholder text, no pseudo-Korean,
no misspelled Korean, no duplicate labels, no invented formula,
no tiny text, no decorative arrows, no gradient background,
no photorealistic style, no file name, no version string
```

## [C] P3-F26 · 웹서버·WAS 하드닝 · 부분 수정

```text
[C] P3-F26 · 웹서버·WAS 하드닝 · 부분 수정

input_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\02_부분수정\Part3\P3-F26.png
output_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\03_수정완료\Part3\P3-F26.png
canvas: 1800 x 1004 px
output_filename: P3-F26.png
title_policy: 내부 전체 제목·그림 코드 금지

문제:
동일 의미의 빨간 경고문이 중복되고 전체 제목이 외부 캡션과 중복된다.

필수 수정:
상단 전체 제목·코드와 중복 빨간 경고문 1개를 삭제. 하드닝 본체는 유지.

통합 가이드 세부 지침: CSV required_correction을 따른다.

기본 프롬프트:
마스킹하지 않은 픽셀, 구도, 아이콘, 선, 화살표, 색상, 여백, 정확한 문구를 그대로 유지한다.
마스킹 영역의 코드·중복 제목·오탈자·잘못된 짧은 라벨만 삭제하거나 지정 문자열로 교체한다.
삭제 영역은 원래 흰 배경과 기존 테두리를 자연스럽게 복원한다.
새 제목, 새 코드, 워터마크, 생성 지시문, 설명문을 추가하지 않는다.
마스킹 영역 밖은 변경하지 않는다.
원본 픽셀 크기를 유지한다.

공통 네거티브:
no watermark, no prompt text, no placeholder text, no pseudo-Korean,
no misspelled Korean, no duplicate labels, no invented formula,
no tiny text, no decorative arrows, no gradient background,
no photorealistic style, no file name, no version string
```

## [C] P3-F32 · 세션 고정·하이재킹·재생 공격 · 부분 수정

```text
[C] P3-F32 · 세션 고정·하이재킹·재생 공격 · 부분 수정

input_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\02_부분수정\Part3\P3-F32.png
output_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\03_수정완료\Part3\P3-F32.png
canvas: 1800 x 1004 px
output_filename: P3-F32.png
title_policy: 내부 전체 제목·그림 코드 금지

문제:
깨진 전체 제목만 제거하면 본체를 유지할 수 있다.

필수 수정:
상단 깨진 전체 제목만 삭제. 본체 유지.

통합 가이드 세부 지침: CSV required_correction을 따른다.

기본 프롬프트:
마스킹하지 않은 픽셀, 구도, 아이콘, 선, 화살표, 색상, 여백, 정확한 문구를 그대로 유지한다.
마스킹 영역의 코드·중복 제목·오탈자·잘못된 짧은 라벨만 삭제하거나 지정 문자열로 교체한다.
삭제 영역은 원래 흰 배경과 기존 테두리를 자연스럽게 복원한다.
새 제목, 새 코드, 워터마크, 생성 지시문, 설명문을 추가하지 않는다.
마스킹 영역 밖은 변경하지 않는다.
원본 픽셀 크기를 유지한다.

공통 네거티브:
no watermark, no prompt text, no placeholder text, no pseudo-Korean,
no misspelled Korean, no duplicate labels, no invented formula,
no tiny text, no decorative arrows, no gradient background,
no photorealistic style, no file name, no version string
```

## [C] P3-F34 · 안전한 파일 업로드 파이프라인 · 부분 수정

```text
[C] P3-F34 · 안전한 파일 업로드 파이프라인 · 부분 수정

input_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\02_부분수정\Part3\P3-F34.png
output_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\03_수정완료\Part3\P3-F34.png
canvas: 1800 x 1004 px
output_filename: P3-F34.png
title_policy: 내부 전체 제목·그림 코드 금지

문제:
외부 캡션과 중복되는 전체 제목·코드를 제거해야 한다.

필수 수정:
상단 전체 제목·코드만 삭제. 본체 유지.

통합 가이드 세부 지침: CSV required_correction을 따른다.

기본 프롬프트:
마스킹하지 않은 픽셀, 구도, 아이콘, 선, 화살표, 색상, 여백, 정확한 문구를 그대로 유지한다.
마스킹 영역의 코드·중복 제목·오탈자·잘못된 짧은 라벨만 삭제하거나 지정 문자열로 교체한다.
삭제 영역은 원래 흰 배경과 기존 테두리를 자연스럽게 복원한다.
새 제목, 새 코드, 워터마크, 생성 지시문, 설명문을 추가하지 않는다.
마스킹 영역 밖은 변경하지 않는다.
원본 픽셀 크기를 유지한다.

공통 네거티브:
no watermark, no prompt text, no placeholder text, no pseudo-Korean,
no misspelled Korean, no duplicate labels, no invented formula,
no tiny text, no decorative arrows, no gradient background,
no photorealistic style, no file name, no version string
```

## [C] P3-F37 · SSRF 공격과 Egress 통제 · 부분 수정

```text
[C] P3-F37 · SSRF 공격과 Egress 통제 · 부분 수정

input_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\02_부분수정\Part3\P3-F37.png
output_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\03_수정완료\Part3\P3-F37.png
canvas: 1800 x 1004 px
output_filename: P3-F37.png
title_policy: 내부 전체 제목·그림 코드 금지

문제:
상단 영문 제목이 외부 캡션과 중복된다.

필수 수정:
상단 `SSRF or Egress filtering` 전체 제목만 삭제. 본체 유지.

통합 가이드 세부 지침: CSV required_correction을 따른다.

기본 프롬프트:
마스킹하지 않은 픽셀, 구도, 아이콘, 선, 화살표, 색상, 여백, 정확한 문구를 그대로 유지한다.
마스킹 영역의 코드·중복 제목·오탈자·잘못된 짧은 라벨만 삭제하거나 지정 문자열로 교체한다.
삭제 영역은 원래 흰 배경과 기존 테두리를 자연스럽게 복원한다.
새 제목, 새 코드, 워터마크, 생성 지시문, 설명문을 추가하지 않는다.
마스킹 영역 밖은 변경하지 않는다.
원본 픽셀 크기를 유지한다.

공통 네거티브:
no watermark, no prompt text, no placeholder text, no pseudo-Korean,
no misspelled Korean, no duplicate labels, no invented formula,
no tiny text, no decorative arrows, no gradient background,
no photorealistic style, no file name, no version string
```

## [C] P3-F39 · 안전하지 않은 역직렬화 · 부분 수정

```text
[C] P3-F39 · 안전하지 않은 역직렬화 · 부분 수정

input_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\02_부분수정\Part3\P3-F39.png
output_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\03_수정완료\Part3\P3-F39.png
canvas: 1800 x 1004 px
output_filename: P3-F39.png
title_policy: 내부 전체 제목·그림 코드 금지

문제:
외부 캡션과 중복되는 전체 제목·코드를 제거해야 한다.

필수 수정:
상단 전체 제목·코드만 삭제. 본체 유지.

통합 가이드 세부 지침: CSV required_correction을 따른다.

기본 프롬프트:
마스킹하지 않은 픽셀, 구도, 아이콘, 선, 화살표, 색상, 여백, 정확한 문구를 그대로 유지한다.
마스킹 영역의 코드·중복 제목·오탈자·잘못된 짧은 라벨만 삭제하거나 지정 문자열로 교체한다.
삭제 영역은 원래 흰 배경과 기존 테두리를 자연스럽게 복원한다.
새 제목, 새 코드, 워터마크, 생성 지시문, 설명문을 추가하지 않는다.
마스킹 영역 밖은 변경하지 않는다.
원본 픽셀 크기를 유지한다.

공통 네거티브:
no watermark, no prompt text, no placeholder text, no pseudo-Korean,
no misspelled Korean, no duplicate labels, no invented formula,
no tiny text, no decorative arrows, no gradient background,
no photorealistic style, no file name, no version string
```

## [C] P3-F45 · 웹 방어 계층과 WAF의 위치 · 부분 수정

```text
[C] P3-F45 · 웹 방어 계층과 WAF의 위치 · 부분 수정

input_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\02_부분수정\Part3\P3-F45.png
output_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\03_수정완료\Part3\P3-F45.png
canvas: 1800 x 1004 px
output_filename: P3-F45.png
title_policy: 내부 전체 제목·그림 코드 금지

문제:
외부 캡션과 중복되는 전체 제목·코드를 제거해야 한다.

필수 수정:
상단 전체 제목·코드만 삭제. 본체 유지.

통합 가이드 세부 지침: CSV required_correction을 따른다.

기본 프롬프트:
마스킹하지 않은 픽셀, 구도, 아이콘, 선, 화살표, 색상, 여백, 정확한 문구를 그대로 유지한다.
마스킹 영역의 코드·중복 제목·오탈자·잘못된 짧은 라벨만 삭제하거나 지정 문자열로 교체한다.
삭제 영역은 원래 흰 배경과 기존 테두리를 자연스럽게 복원한다.
새 제목, 새 코드, 워터마크, 생성 지시문, 설명문을 추가하지 않는다.
마스킹 영역 밖은 변경하지 않는다.
원본 픽셀 크기를 유지한다.

공통 네거티브:
no watermark, no prompt text, no placeholder text, no pseudo-Korean,
no misspelled Korean, no duplicate labels, no invented formula,
no tiny text, no decorative arrows, no gradient background,
no photorealistic style, no file name, no version string
```

## [C] P3-F46 · DNS 이름해석과 캐시 · 부분 수정

```text
[C] P3-F46 · DNS 이름해석과 캐시 · 부분 수정

input_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\02_부분수정\Part3\P3-F46.png
output_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\03_수정완료\Part3\P3-F46.png
canvas: 1800 x 1004 px
output_filename: P3-F46.png
title_policy: 내부 전체 제목·그림 코드 금지

문제:
외부 캡션과 중복되는 전체 제목을 제거해야 한다.

필수 수정:
상단 전체 제목만 삭제. 본체 유지.

통합 가이드 세부 지침: CSV required_correction을 따른다.

기본 프롬프트:
마스킹하지 않은 픽셀, 구도, 아이콘, 선, 화살표, 색상, 여백, 정확한 문구를 그대로 유지한다.
마스킹 영역의 코드·중복 제목·오탈자·잘못된 짧은 라벨만 삭제하거나 지정 문자열로 교체한다.
삭제 영역은 원래 흰 배경과 기존 테두리를 자연스럽게 복원한다.
새 제목, 새 코드, 워터마크, 생성 지시문, 설명문을 추가하지 않는다.
마스킹 영역 밖은 변경하지 않는다.
원본 픽셀 크기를 유지한다.

공통 네거티브:
no watermark, no prompt text, no placeholder text, no pseudo-Korean,
no misspelled Korean, no duplicate labels, no invented formula,
no tiny text, no decorative arrows, no gradient background,
no photorealistic style, no file name, no version string
```

## [C] P3-F48 · 재귀 질의·반복 질의·영역전송 · 부분 수정

```text
[C] P3-F48 · 재귀 질의·반복 질의·영역전송 · 부분 수정

input_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\02_부분수정\Part3\P3-F48.png
output_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\03_수정완료\Part3\P3-F48.png
canvas: 1800 x 1004 px
output_filename: P3-F48.png
title_policy: 내부 전체 제목·그림 코드 금지

문제:
외부 캡션과 중복되는 전체 제목·코드를 제거해야 한다.

필수 수정:
상단 전체 제목·코드만 삭제. 본체 유지.

통합 가이드 세부 지침: CSV required_correction을 따른다.

기본 프롬프트:
마스킹하지 않은 픽셀, 구도, 아이콘, 선, 화살표, 색상, 여백, 정확한 문구를 그대로 유지한다.
마스킹 영역의 코드·중복 제목·오탈자·잘못된 짧은 라벨만 삭제하거나 지정 문자열로 교체한다.
삭제 영역은 원래 흰 배경과 기존 테두리를 자연스럽게 복원한다.
새 제목, 새 코드, 워터마크, 생성 지시문, 설명문을 추가하지 않는다.
마스킹 영역 밖은 변경하지 않는다.
원본 픽셀 크기를 유지한다.

공통 네거티브:
no watermark, no prompt text, no placeholder text, no pseudo-Korean,
no misspelled Korean, no duplicate labels, no invented formula,
no tiny text, no decorative arrows, no gradient background,
no photorealistic style, no file name, no version string
```

## [C] P3-F65 · OWASP Top 10:2025 지도 · 부분 수정

```text
[C] P3-F65 · OWASP Top 10:2025 지도 · 부분 수정

input_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\02_부분수정\Part3\P3-F65.png
output_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\03_수정완료\Part3\P3-F65.png
canvas: 1800 x 1004 px
output_filename: P3-F65.png
title_policy: 내부 전체 제목·그림 코드 금지

문제:
OWASP 본체는 유지 가능하며 상단의 깨진 한국어 제목만 제거하면 된다.

필수 수정:
상단 깨진 한국어 전체 제목만 삭제. A01~A10 본체는 유지.

통합 가이드 세부 지침: CSV required_correction을 따른다.

기본 프롬프트:
마스킹하지 않은 픽셀, 구도, 아이콘, 선, 화살표, 색상, 여백, 정확한 문구를 그대로 유지한다.
마스킹 영역의 코드·중복 제목·오탈자·잘못된 짧은 라벨만 삭제하거나 지정 문자열로 교체한다.
삭제 영역은 원래 흰 배경과 기존 테두리를 자연스럽게 복원한다.
새 제목, 새 코드, 워터마크, 생성 지시문, 설명문을 추가하지 않는다.
마스킹 영역 밖은 변경하지 않는다.
원본 픽셀 크기를 유지한다.

공통 네거티브:
no watermark, no prompt text, no placeholder text, no pseudo-Korean,
no misspelled Korean, no duplicate labels, no invented formula,
no tiny text, no decorative arrows, no gradient background,
no photorealistic style, no file name, no version string
```

## [C] P3-F69 · 암호·비밀·오류·로그 안전 코딩 · 부분 수정

```text
[C] P3-F69 · 암호·비밀·오류·로그 안전 코딩 · 부분 수정

input_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\02_부분수정\Part3\P3-F69.png
output_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\03_수정완료\Part3\P3-F69.png
canvas: 1800 x 1004 px
output_filename: P3-F69.png
title_policy: 내부 전체 제목·그림 코드 금지

문제:
외부 캡션과 중복되는 전체 제목·코드를 제거해야 한다.

필수 수정:
상단 전체 제목·코드만 삭제. 본체 유지.

통합 가이드 세부 지침: CSV required_correction을 따른다.

기본 프롬프트:
마스킹하지 않은 픽셀, 구도, 아이콘, 선, 화살표, 색상, 여백, 정확한 문구를 그대로 유지한다.
마스킹 영역의 코드·중복 제목·오탈자·잘못된 짧은 라벨만 삭제하거나 지정 문자열로 교체한다.
삭제 영역은 원래 흰 배경과 기존 테두리를 자연스럽게 복원한다.
새 제목, 새 코드, 워터마크, 생성 지시문, 설명문을 추가하지 않는다.
마스킹 영역 밖은 변경하지 않는다.
원본 픽셀 크기를 유지한다.

공통 네거티브:
no watermark, no prompt text, no placeholder text, no pseudo-Korean,
no misspelled Korean, no duplicate labels, no invented formula,
no tiny text, no decorative arrows, no gradient background,
no photorealistic style, no file name, no version string
```

## [C] P3-F70 · SAST·DAST·IAST·SCA·Fuzzing 비교 · 부분 수정

```text
[C] P3-F70 · SAST·DAST·IAST·SCA·Fuzzing 비교 · 부분 수정

input_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\02_부분수정\Part3\P3-F70.png
output_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\03_수정완료\Part3\P3-F70.png
canvas: 1800 x 1004 px
output_filename: P3-F70.png
title_policy: 내부 전체 제목·그림 코드 금지

문제:
외부 캡션과 중복되는 전체 제목·코드를 제거해야 한다.

필수 수정:
상단 전체 제목·코드만 삭제. 본체 유지.

통합 가이드 세부 지침: CSV required_correction을 따른다.

기본 프롬프트:
마스킹하지 않은 픽셀, 구도, 아이콘, 선, 화살표, 색상, 여백, 정확한 문구를 그대로 유지한다.
마스킹 영역의 코드·중복 제목·오탈자·잘못된 짧은 라벨만 삭제하거나 지정 문자열로 교체한다.
삭제 영역은 원래 흰 배경과 기존 테두리를 자연스럽게 복원한다.
새 제목, 새 코드, 워터마크, 생성 지시문, 설명문을 추가하지 않는다.
마스킹 영역 밖은 변경하지 않는다.
원본 픽셀 크기를 유지한다.

공통 네거티브:
no watermark, no prompt text, no placeholder text, no pseudo-Korean,
no misspelled Korean, no duplicate labels, no invented formula,
no tiny text, no decorative arrows, no gradient background,
no photorealistic style, no file name, no version string
```

## [C] P3-F71 · DevSecOps·공급망·SBOM · 부분 수정

```text
[C] P3-F71 · DevSecOps·공급망·SBOM · 부분 수정

input_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\02_부분수정\Part3\P3-F71.png
output_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\03_수정완료\Part3\P3-F71.png
canvas: 1800 x 1004 px
output_filename: P3-F71.png
title_policy: 내부 전체 제목·그림 코드 금지

문제:
외부 캡션과 중복되는 전체 제목·코드를 제거해야 한다.

필수 수정:
상단 전체 제목·코드만 삭제. 본체 유지.

통합 가이드 세부 지침: CSV required_correction을 따른다.

기본 프롬프트:
마스킹하지 않은 픽셀, 구도, 아이콘, 선, 화살표, 색상, 여백, 정확한 문구를 그대로 유지한다.
마스킹 영역의 코드·중복 제목·오탈자·잘못된 짧은 라벨만 삭제하거나 지정 문자열로 교체한다.
삭제 영역은 원래 흰 배경과 기존 테두리를 자연스럽게 복원한다.
새 제목, 새 코드, 워터마크, 생성 지시문, 설명문을 추가하지 않는다.
마스킹 영역 밖은 변경하지 않는다.
원본 픽셀 크기를 유지한다.

공통 네거티브:
no watermark, no prompt text, no placeholder text, no pseudo-Korean,
no misspelled Korean, no duplicate labels, no invented formula,
no tiny text, no decorative arrows, no gradient background,
no photorealistic style, no file name, no version string
```

## [C] P4-F01 · 정보보안 일반 출제범위 전체 지도 · 부분 수정

```text
[C] P4-F01 · 정보보안 일반 출제범위 전체 지도 · 부분 수정

input_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\02_부분수정\Part4\P4-F01.png
output_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\03_수정완료\Part4\P4-F01.png
canvas: 1600 x 893 px
output_filename: P4-F01.png
title_policy: 내부 전체 제목·그림 코드 금지

문제:
그림 내부 코드·중복 제목·지시문 또는 국소 오탈자가 남아 있다.

필수 수정:
상단의 코드와 전체 제목만 삭제. 본체 구조 유지.

통합 가이드 세부 지침: CSV required_correction을 따른다.

기본 프롬프트:
마스킹하지 않은 픽셀, 구도, 아이콘, 선, 화살표, 색상, 여백, 정확한 문구를 그대로 유지한다.
마스킹 영역의 코드·중복 제목·오탈자·잘못된 짧은 라벨만 삭제하거나 지정 문자열로 교체한다.
삭제 영역은 원래 흰 배경과 기존 테두리를 자연스럽게 복원한다.
새 제목, 새 코드, 워터마크, 생성 지시문, 설명문을 추가하지 않는다.
마스킹 영역 밖은 변경하지 않는다.
원본 픽셀 크기를 유지한다.

공통 네거티브:
no watermark, no prompt text, no placeholder text, no pseudo-Korean,
no misspelled Korean, no duplicate labels, no invented formula,
no tiny text, no decorative arrows, no gradient background,
no photorealistic style, no file name, no version string
```

## [C] P4-F03 · 식별·인증·인가·감사 흐름 · 부분 수정

```text
[C] P4-F03 · 식별·인증·인가·감사 흐름 · 부분 수정

input_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\02_부분수정\Part4\P4-F03.png
output_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\03_수정완료\Part4\P4-F03.png
canvas: 1600 x 893 px
output_filename: P4-F03.png
title_policy: 내부 전체 제목·그림 코드 금지

문제:
그림 내부 코드·중복 제목·지시문 또는 국소 오탈자가 남아 있다.

필수 수정:
상단 코드·영문 전체 제목 삭제.

통합 가이드 세부 지침: CSV required_correction을 따른다.

기본 프롬프트:
마스킹하지 않은 픽셀, 구도, 아이콘, 선, 화살표, 색상, 여백, 정확한 문구를 그대로 유지한다.
마스킹 영역의 코드·중복 제목·오탈자·잘못된 짧은 라벨만 삭제하거나 지정 문자열로 교체한다.
삭제 영역은 원래 흰 배경과 기존 테두리를 자연스럽게 복원한다.
새 제목, 새 코드, 워터마크, 생성 지시문, 설명문을 추가하지 않는다.
마스킹 영역 밖은 변경하지 않는다.
원본 픽셀 크기를 유지한다.

공통 네거티브:
no watermark, no prompt text, no placeholder text, no pseudo-Korean,
no misspelled Korean, no duplicate labels, no invented formula,
no tiny text, no decorative arrows, no gradient background,
no photorealistic style, no file name, no version string
```

## [C] P4-F05 · 비밀번호 생명주기와 검증자 저장 · 부분 수정

```text
[C] P4-F05 · 비밀번호 생명주기와 검증자 저장 · 부분 수정

input_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\02_부분수정\Part4\P4-F05.png
output_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\03_수정완료\Part4\P4-F05.png
canvas: 1600 x 893 px
output_filename: P4-F05.png
title_policy: 내부 전체 제목·그림 코드 금지

문제:
그림 내부 코드·중복 제목·지시문 또는 국소 오탈자가 남아 있다.

필수 수정:
상단 전체 제목 배너 삭제.

통합 가이드 세부 지침: CSV required_correction을 따른다.

기본 프롬프트:
마스킹하지 않은 픽셀, 구도, 아이콘, 선, 화살표, 색상, 여백, 정확한 문구를 그대로 유지한다.
마스킹 영역의 코드·중복 제목·오탈자·잘못된 짧은 라벨만 삭제하거나 지정 문자열로 교체한다.
삭제 영역은 원래 흰 배경과 기존 테두리를 자연스럽게 복원한다.
새 제목, 새 코드, 워터마크, 생성 지시문, 설명문을 추가하지 않는다.
마스킹 영역 밖은 변경하지 않는다.
원본 픽셀 크기를 유지한다.

공통 네거티브:
no watermark, no prompt text, no placeholder text, no pseudo-Korean,
no misspelled Korean, no duplicate labels, no invented formula,
no tiny text, no decorative arrows, no gradient background,
no photorealistic style, no file name, no version string
```

## [C] P4-F06 · 온라인·오프라인 비밀번호 공격 비교 · 부분 수정

```text
[C] P4-F06 · 온라인·오프라인 비밀번호 공격 비교 · 부분 수정

input_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\02_부분수정\Part4\P4-F06.png
output_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\03_수정완료\Part4\P4-F06.png
canvas: 1600 x 893 px
output_filename: P4-F06.png
title_policy: 내부 전체 제목·그림 코드 금지

문제:
그림 내부 코드·중복 제목·지시문 또는 국소 오탈자가 남아 있다.

필수 수정:
깨진 전체 제목 삭제. 패널 내부 `온라인 공격`, `오프라인 공격`은 유지.

통합 가이드 세부 지침: CSV required_correction을 따른다.

기본 프롬프트:
마스킹하지 않은 픽셀, 구도, 아이콘, 선, 화살표, 색상, 여백, 정확한 문구를 그대로 유지한다.
마스킹 영역의 코드·중복 제목·오탈자·잘못된 짧은 라벨만 삭제하거나 지정 문자열로 교체한다.
삭제 영역은 원래 흰 배경과 기존 테두리를 자연스럽게 복원한다.
새 제목, 새 코드, 워터마크, 생성 지시문, 설명문을 추가하지 않는다.
마스킹 영역 밖은 변경하지 않는다.
원본 픽셀 크기를 유지한다.

공통 네거티브:
no watermark, no prompt text, no placeholder text, no pseudo-Korean,
no misspelled Korean, no duplicate labels, no invented formula,
no tiny text, no decorative arrows, no gradient background,
no photorealistic style, no file name, no version string
```

## [C] P4-F10 · 바이오인증 등록·검증 파이프라인 · 부분 수정

```text
[C] P4-F10 · 바이오인증 등록·검증 파이프라인 · 부분 수정

input_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\02_부분수정\Part4\P4-F10.png
output_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\03_수정완료\Part4\P4-F10.png
canvas: 1600 x 893 px
output_filename: P4-F10.png
title_policy: 내부 전체 제목·그림 코드 금지

문제:
그림 내부 코드·중복 제목·지시문 또는 국소 오탈자가 남아 있다.

필수 수정:
상단 코드·전체 제목 삭제.

통합 가이드 세부 지침: CSV required_correction을 따른다.

기본 프롬프트:
마스킹하지 않은 픽셀, 구도, 아이콘, 선, 화살표, 색상, 여백, 정확한 문구를 그대로 유지한다.
마스킹 영역의 코드·중복 제목·오탈자·잘못된 짧은 라벨만 삭제하거나 지정 문자열로 교체한다.
삭제 영역은 원래 흰 배경과 기존 테두리를 자연스럽게 복원한다.
새 제목, 새 코드, 워터마크, 생성 지시문, 설명문을 추가하지 않는다.
마스킹 영역 밖은 변경하지 않는다.
원본 픽셀 크기를 유지한다.

공통 네거티브:
no watermark, no prompt text, no placeholder text, no pseudo-Korean,
no misspelled Korean, no duplicate labels, no invented formula,
no tiny text, no decorative arrows, no gradient background,
no photorealistic style, no file name, no version string
```

## [C] P4-F19 · DAC·MAC·RBAC·ABAC·CBAC 비교 · 부분 수정

```text
[C] P4-F19 · DAC·MAC·RBAC·ABAC·CBAC 비교 · 부분 수정

input_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\02_부분수정\Part4\P4-F19.png
output_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\03_수정완료\Part4\P4-F19.png
canvas: 1600 x 893 px
output_filename: P4-F19.png
title_policy: 내부 전체 제목·그림 코드 금지

문제:
그림 내부 코드·중복 제목·지시문 또는 국소 오탈자가 남아 있다.

필수 수정:
상단 코드·전체 제목 삭제.

통합 가이드 세부 지침: CSV required_correction을 따른다.

기본 프롬프트:
마스킹하지 않은 픽셀, 구도, 아이콘, 선, 화살표, 색상, 여백, 정확한 문구를 그대로 유지한다.
마스킹 영역의 코드·중복 제목·오탈자·잘못된 짧은 라벨만 삭제하거나 지정 문자열로 교체한다.
삭제 영역은 원래 흰 배경과 기존 테두리를 자연스럽게 복원한다.
새 제목, 새 코드, 워터마크, 생성 지시문, 설명문을 추가하지 않는다.
마스킹 영역 밖은 변경하지 않는다.
원본 픽셀 크기를 유지한다.

공통 네거티브:
no watermark, no prompt text, no placeholder text, no pseudo-Korean,
no misspelled Korean, no duplicate labels, no invented formula,
no tiny text, no decorative arrows, no gradient background,
no photorealistic style, no file name, no version string
```

## [C] P4-F20 · 최소권한·Need-to-Know·직무분리 · 부분 수정

```text
[C] P4-F20 · 최소권한·Need-to-Know·직무분리 · 부분 수정

input_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\02_부분수정\Part4\P4-F20.png
output_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\03_수정완료\Part4\P4-F20.png
canvas: 1600 x 893 px
output_filename: P4-F20.png
title_policy: 내부 전체 제목·그림 코드 금지

문제:
그림 내부 코드·중복 제목·지시문 또는 국소 오탈자가 남아 있다.

필수 수정:
상단 코드·전체 제목 삭제.

통합 가이드 세부 지침: CSV required_correction을 따른다.

기본 프롬프트:
마스킹하지 않은 픽셀, 구도, 아이콘, 선, 화살표, 색상, 여백, 정확한 문구를 그대로 유지한다.
마스킹 영역의 코드·중복 제목·오탈자·잘못된 짧은 라벨만 삭제하거나 지정 문자열로 교체한다.
삭제 영역은 원래 흰 배경과 기존 테두리를 자연스럽게 복원한다.
새 제목, 새 코드, 워터마크, 생성 지시문, 설명문을 추가하지 않는다.
마스킹 영역 밖은 변경하지 않는다.
원본 픽셀 크기를 유지한다.

공통 네거티브:
no watermark, no prompt text, no placeholder text, no pseudo-Korean,
no misspelled Korean, no duplicate labels, no invented formula,
no tiny text, no decorative arrows, no gradient background,
no photorealistic style, no file name, no version string
```

## [C] P4-F22 · Bell-LaPadula 기밀성 규칙 · 부분 수정

```text
[C] P4-F22 · Bell-LaPadula 기밀성 규칙 · 부분 수정

input_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\02_부분수정\Part4\P4-F22.png
output_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\03_수정완료\Part4\P4-F22.png
canvas: 1600 x 893 px
output_filename: P4-F22.png
title_policy: 내부 전체 제목·그림 코드 금지

문제:
그림 내부 코드·중복 제목·지시문 또는 국소 오탈자가 남아 있다.

필수 수정:
상단 코드·전체 제목 삭제. BLP 규칙은 유지.

통합 가이드 세부 지침: CSV required_correction을 따른다.

기본 프롬프트:
마스킹하지 않은 픽셀, 구도, 아이콘, 선, 화살표, 색상, 여백, 정확한 문구를 그대로 유지한다.
마스킹 영역의 코드·중복 제목·오탈자·잘못된 짧은 라벨만 삭제하거나 지정 문자열로 교체한다.
삭제 영역은 원래 흰 배경과 기존 테두리를 자연스럽게 복원한다.
새 제목, 새 코드, 워터마크, 생성 지시문, 설명문을 추가하지 않는다.
마스킹 영역 밖은 변경하지 않는다.
원본 픽셀 크기를 유지한다.

공통 네거티브:
no watermark, no prompt text, no placeholder text, no pseudo-Korean,
no misspelled Korean, no duplicate labels, no invented formula,
no tiny text, no decorative arrows, no gradient background,
no photorealistic style, no file name, no version string
```

## [C] P4-F23 · Biba 무결성 규칙 · 부분 수정

```text
[C] P4-F23 · Biba 무결성 규칙 · 부분 수정

input_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\02_부분수정\Part4\P4-F23.png
output_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\03_수정완료\Part4\P4-F23.png
canvas: 1600 x 893 px
output_filename: P4-F23.png
title_policy: 내부 전체 제목·그림 코드 금지

문제:
그림 내부 코드·중복 제목·지시문 또는 국소 오탈자가 남아 있다.

필수 수정:
깨진 전체 제목 삭제. 내부 `No Read Down`, `No Write Up`은 유지.

통합 가이드 세부 지침: CSV required_correction을 따른다.

기본 프롬프트:
마스킹하지 않은 픽셀, 구도, 아이콘, 선, 화살표, 색상, 여백, 정확한 문구를 그대로 유지한다.
마스킹 영역의 코드·중복 제목·오탈자·잘못된 짧은 라벨만 삭제하거나 지정 문자열로 교체한다.
삭제 영역은 원래 흰 배경과 기존 테두리를 자연스럽게 복원한다.
새 제목, 새 코드, 워터마크, 생성 지시문, 설명문을 추가하지 않는다.
마스킹 영역 밖은 변경하지 않는다.
원본 픽셀 크기를 유지한다.

공통 네거티브:
no watermark, no prompt text, no placeholder text, no pseudo-Korean,
no misspelled Korean, no duplicate labels, no invented formula,
no tiny text, no decorative arrows, no gradient background,
no photorealistic style, no file name, no version string
```

## [C] P4-F34 · 공개키 배포 방식 비교 · 부분 수정

```text
[C] P4-F34 · 공개키 배포 방식 비교 · 부분 수정

input_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\02_부분수정\Part4\P4-F34.png
output_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\03_수정완료\Part4\P4-F34.png
canvas: 1600 x 893 px
output_filename: P4-F34.png
title_policy: 내부 전체 제목·그림 코드 금지

문제:
그림 내부 코드·중복 제목·지시문 또는 국소 오탈자가 남아 있다.

필수 수정:
상단 코드·전체 제목 삭제.

통합 가이드 세부 지침: CSV required_correction을 따른다.

기본 프롬프트:
마스킹하지 않은 픽셀, 구도, 아이콘, 선, 화살표, 색상, 여백, 정확한 문구를 그대로 유지한다.
마스킹 영역의 코드·중복 제목·오탈자·잘못된 짧은 라벨만 삭제하거나 지정 문자열로 교체한다.
삭제 영역은 원래 흰 배경과 기존 테두리를 자연스럽게 복원한다.
새 제목, 새 코드, 워터마크, 생성 지시문, 설명문을 추가하지 않는다.
마스킹 영역 밖은 변경하지 않는다.
원본 픽셀 크기를 유지한다.

공통 네거티브:
no watermark, no prompt text, no placeholder text, no pseudo-Korean,
no misspelled Korean, no duplicate labels, no invented formula,
no tiny text, no decorative arrows, no gradient background,
no photorealistic style, no file name, no version string
```

## [C] P4-F35 · 하이브리드 암호와 디지털 봉투 · 부분 수정

```text
[C] P4-F35 · 하이브리드 암호와 디지털 봉투 · 부분 수정

input_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\02_부분수정\Part4\P4-F35.png
output_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\03_수정완료\Part4\P4-F35.png
canvas: 1600 x 893 px
output_filename: P4-F35.png
title_policy: 내부 전체 제목·그림 코드 금지

문제:
그림 내부 코드·중복 제목·지시문 또는 국소 오탈자가 남아 있다.

필수 수정:
상단 전체 제목 삭제.

통합 가이드 세부 지침: CSV required_correction을 따른다.

기본 프롬프트:
마스킹하지 않은 픽셀, 구도, 아이콘, 선, 화살표, 색상, 여백, 정확한 문구를 그대로 유지한다.
마스킹 영역의 코드·중복 제목·오탈자·잘못된 짧은 라벨만 삭제하거나 지정 문자열로 교체한다.
삭제 영역은 원래 흰 배경과 기존 테두리를 자연스럽게 복원한다.
새 제목, 새 코드, 워터마크, 생성 지시문, 설명문을 추가하지 않는다.
마스킹 영역 밖은 변경하지 않는다.
원본 픽셀 크기를 유지한다.

공통 네거티브:
no watermark, no prompt text, no placeholder text, no pseudo-Korean,
no misspelled Korean, no duplicate labels, no invented formula,
no tiny text, no decorative arrows, no gradient background,
no photorealistic style, no file name, no version string
```

## [C] P4-F36 · 전자서명 생성·검증 흐름 · 부분 수정

```text
[C] P4-F36 · 전자서명 생성·검증 흐름 · 부분 수정

input_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\02_부분수정\Part4\P4-F36.png
output_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\03_수정완료\Part4\P4-F36.png
canvas: 1600 x 893 px
output_filename: P4-F36.png
title_policy: 내부 전체 제목·그림 코드 금지

문제:
그림 내부 코드·중복 제목·지시문 또는 국소 오탈자가 남아 있다.

필수 수정:
상단 코드·전체 제목 삭제.

통합 가이드 세부 지침: CSV required_correction을 따른다.

기본 프롬프트:
마스킹하지 않은 픽셀, 구도, 아이콘, 선, 화살표, 색상, 여백, 정확한 문구를 그대로 유지한다.
마스킹 영역의 코드·중복 제목·오탈자·잘못된 짧은 라벨만 삭제하거나 지정 문자열로 교체한다.
삭제 영역은 원래 흰 배경과 기존 테두리를 자연스럽게 복원한다.
새 제목, 새 코드, 워터마크, 생성 지시문, 설명문을 추가하지 않는다.
마스킹 영역 밖은 변경하지 않는다.
원본 픽셀 크기를 유지한다.

공통 네거티브:
no watermark, no prompt text, no placeholder text, no pseudo-Korean,
no misspelled Korean, no duplicate labels, no invented formula,
no tiny text, no decorative arrows, no gradient background,
no photorealistic style, no file name, no version string
```

## [C] P4-F37 · 전자서명 보안요구와 한계 · 부분 수정

```text
[C] P4-F37 · 전자서명 보안요구와 한계 · 부분 수정

input_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\02_부분수정\Part4\P4-F37.png
output_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\03_수정완료\Part4\P4-F37.png
canvas: 1600 x 893 px
output_filename: P4-F37.png
title_policy: 내부 전체 제목·그림 코드 금지

문제:
그림 내부 코드·중복 제목·지시문 또는 국소 오탈자가 남아 있다.

필수 수정:
상단 코드·전체 제목 삭제.

통합 가이드 세부 지침: CSV required_correction을 따른다.

기본 프롬프트:
마스킹하지 않은 픽셀, 구도, 아이콘, 선, 화살표, 색상, 여백, 정확한 문구를 그대로 유지한다.
마스킹 영역의 코드·중복 제목·오탈자·잘못된 짧은 라벨만 삭제하거나 지정 문자열로 교체한다.
삭제 영역은 원래 흰 배경과 기존 테두리를 자연스럽게 복원한다.
새 제목, 새 코드, 워터마크, 생성 지시문, 설명문을 추가하지 않는다.
마스킹 영역 밖은 변경하지 않는다.
원본 픽셀 크기를 유지한다.

공통 네거티브:
no watermark, no prompt text, no placeholder text, no pseudo-Korean,
no misspelled Korean, no duplicate labels, no invented formula,
no tiny text, no decorative arrows, no gradient background,
no photorealistic style, no file name, no version string
```

## [C] P4-F41 · X.509 인증서 구조 · 부분 수정

```text
[C] P4-F41 · X.509 인증서 구조 · 부분 수정

input_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\02_부분수정\Part4\P4-F41.png
output_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\03_수정완료\Part4\P4-F41.png
canvas: 1600 x 893 px
output_filename: P4-F41.png
title_policy: 내부 전체 제목·그림 코드 금지

문제:
그림 내부 코드·중복 제목·지시문 또는 국소 오탈자가 남아 있다.

필수 수정:
상단 코드·전체 제목 삭제.

통합 가이드 세부 지침: CSV required_correction을 따른다.

기본 프롬프트:
마스킹하지 않은 픽셀, 구도, 아이콘, 선, 화살표, 색상, 여백, 정확한 문구를 그대로 유지한다.
마스킹 영역의 코드·중복 제목·오탈자·잘못된 짧은 라벨만 삭제하거나 지정 문자열로 교체한다.
삭제 영역은 원래 흰 배경과 기존 테두리를 자연스럽게 복원한다.
새 제목, 새 코드, 워터마크, 생성 지시문, 설명문을 추가하지 않는다.
마스킹 영역 밖은 변경하지 않는다.
원본 픽셀 크기를 유지한다.

공통 네거티브:
no watermark, no prompt text, no placeholder text, no pseudo-Korean,
no misspelled Korean, no duplicate labels, no invented formula,
no tiny text, no decorative arrows, no gradient background,
no photorealistic style, no file name, no version string
```

## [C] P4-F42 · PKI 구성요소와 역할 · 부분 수정

```text
[C] P4-F42 · PKI 구성요소와 역할 · 부분 수정

input_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\02_부분수정\Part4\P4-F42.png
output_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\03_수정완료\Part4\P4-F42.png
canvas: 1600 x 893 px
output_filename: P4-F42.png
title_policy: 내부 전체 제목·그림 코드 금지

문제:
그림 내부 코드·중복 제목·지시문 또는 국소 오탈자가 남아 있다.

필수 수정:
상단 코드·전체 제목 삭제.

통합 가이드 세부 지침: CSV required_correction을 따른다.

기본 프롬프트:
마스킹하지 않은 픽셀, 구도, 아이콘, 선, 화살표, 색상, 여백, 정확한 문구를 그대로 유지한다.
마스킹 영역의 코드·중복 제목·오탈자·잘못된 짧은 라벨만 삭제하거나 지정 문자열로 교체한다.
삭제 영역은 원래 흰 배경과 기존 테두리를 자연스럽게 복원한다.
새 제목, 새 코드, 워터마크, 생성 지시문, 설명문을 추가하지 않는다.
마스킹 영역 밖은 변경하지 않는다.
원본 픽셀 크기를 유지한다.

공통 네거티브:
no watermark, no prompt text, no placeholder text, no pseudo-Korean,
no misspelled Korean, no duplicate labels, no invented formula,
no tiny text, no decorative arrows, no gradient background,
no photorealistic style, no file name, no version string
```

## [C] P4-F44 · 인증서 발급·갱신·폐기 생명주기 · 부분 수정

```text
[C] P4-F44 · 인증서 발급·갱신·폐기 생명주기 · 부분 수정

input_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\02_부분수정\Part4\P4-F44.png
output_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\03_수정완료\Part4\P4-F44.png
canvas: 1600 x 893 px
output_filename: P4-F44.png
title_policy: 내부 전체 제목·그림 코드 금지

문제:
그림 내부 코드·중복 제목·지시문 또는 국소 오탈자가 남아 있다.

필수 수정:
상단 코드·전체 제목 삭제.

통합 가이드 세부 지침: CSV required_correction을 따른다.

기본 프롬프트:
마스킹하지 않은 픽셀, 구도, 아이콘, 선, 화살표, 색상, 여백, 정확한 문구를 그대로 유지한다.
마스킹 영역의 코드·중복 제목·오탈자·잘못된 짧은 라벨만 삭제하거나 지정 문자열로 교체한다.
삭제 영역은 원래 흰 배경과 기존 테두리를 자연스럽게 복원한다.
새 제목, 새 코드, 워터마크, 생성 지시문, 설명문을 추가하지 않는다.
마스킹 영역 밖은 변경하지 않는다.
원본 픽셀 크기를 유지한다.

공통 네거티브:
no watermark, no prompt text, no placeholder text, no pseudo-Korean,
no misspelled Korean, no duplicate labels, no invented formula,
no tiny text, no decorative arrows, no gradient background,
no photorealistic style, no file name, no version string
```

## [C] P4-F47 · 타임스탬프와 장기검증 · 부분 수정

```text
[C] P4-F47 · 타임스탬프와 장기검증 · 부분 수정

input_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\02_부분수정\Part4\P4-F47.png
output_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\03_수정완료\Part4\P4-F47.png
canvas: 1600 x 893 px
output_filename: P4-F47.png
title_policy: 내부 전체 제목·그림 코드 금지

문제:
그림 내부 코드·중복 제목·지시문 또는 국소 오탈자가 남아 있다.

필수 수정:
상단 코드·전체 제목 삭제.

통합 가이드 세부 지침: CSV required_correction을 따른다.

기본 프롬프트:
마스킹하지 않은 픽셀, 구도, 아이콘, 선, 화살표, 색상, 여백, 정확한 문구를 그대로 유지한다.
마스킹 영역의 코드·중복 제목·오탈자·잘못된 짧은 라벨만 삭제하거나 지정 문자열로 교체한다.
삭제 영역은 원래 흰 배경과 기존 테두리를 자연스럽게 복원한다.
새 제목, 새 코드, 워터마크, 생성 지시문, 설명문을 추가하지 않는다.
마스킹 영역 밖은 변경하지 않는다.
원본 픽셀 크기를 유지한다.

공통 네거티브:
no watermark, no prompt text, no placeholder text, no pseudo-Korean,
no misspelled Korean, no duplicate labels, no invented formula,
no tiny text, no decorative arrows, no gradient background,
no photorealistic style, no file name, no version string
```

## [C] P4-F52 · 혼돈·확산·쇄도효과 · 부분 수정

```text
[C] P4-F52 · 혼돈·확산·쇄도효과 · 부분 수정

input_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\02_부분수정\Part4\P4-F52.png
output_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\03_수정완료\Part4\P4-F52.png
canvas: 1600 x 893 px
output_filename: P4-F52.png
title_policy: 내부 전체 제목·그림 코드 금지

문제:
그림 내부 코드·중복 제목·지시문 또는 국소 오탈자가 남아 있다.

필수 수정:
상단 코드·전체 제목 삭제. 세 패널의 `혼돈`, `확산`, `쇄도효과`는 유지.

통합 가이드 세부 지침: CSV required_correction을 따른다.

기본 프롬프트:
마스킹하지 않은 픽셀, 구도, 아이콘, 선, 화살표, 색상, 여백, 정확한 문구를 그대로 유지한다.
마스킹 영역의 코드·중복 제목·오탈자·잘못된 짧은 라벨만 삭제하거나 지정 문자열로 교체한다.
삭제 영역은 원래 흰 배경과 기존 테두리를 자연스럽게 복원한다.
새 제목, 새 코드, 워터마크, 생성 지시문, 설명문을 추가하지 않는다.
마스킹 영역 밖은 변경하지 않는다.
원본 픽셀 크기를 유지한다.

공통 네거티브:
no watermark, no prompt text, no placeholder text, no pseudo-Korean,
no misspelled Korean, no duplicate labels, no invented formula,
no tiny text, no decorative arrows, no gradient background,
no photorealistic style, no file name, no version string
```

## [C] P5-F03 · 사업전략과 정보보호 전략 정렬 · 부분 수정

```text
[C] P5-F03 · 사업전략과 정보보호 전략 정렬 · 부분 수정

input_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\02_부분수정\Part5\P5-F03.png
output_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\03_수정완료\Part5\P5-F03.png
canvas: 1600 x 893 px
output_filename: P5-F03.png
title_policy: 내부 전체 제목·그림 코드 금지

문제:
그림 내부 코드·중복 제목·지시문 또는 국소 오탈자가 남아 있다.

필수 수정:
깨진 전체 제목 배너 삭제. 내부 흐름 유지.

통합 가이드 세부 지침: CSV required_correction을 따른다.

기본 프롬프트:
마스킹하지 않은 픽셀, 구도, 아이콘, 선, 화살표, 색상, 여백, 정확한 문구를 그대로 유지한다.
마스킹 영역의 코드·중복 제목·오탈자·잘못된 짧은 라벨만 삭제하거나 지정 문자열로 교체한다.
삭제 영역은 원래 흰 배경과 기존 테두리를 자연스럽게 복원한다.
새 제목, 새 코드, 워터마크, 생성 지시문, 설명문을 추가하지 않는다.
마스킹 영역 밖은 변경하지 않는다.
원본 픽셀 크기를 유지한다.

공통 네거티브:
no watermark, no prompt text, no placeholder text, no pseudo-Korean,
no misspelled Korean, no duplicate labels, no invented formula,
no tiny text, no decorative arrows, no gradient background,
no photorealistic style, no file name, no version string
```

## [C] P5-F07 · 정보보호 관리 생명주기 · 부분 수정

```text
[C] P5-F07 · 정보보호 관리 생명주기 · 부분 수정

input_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\02_부분수정\Part5\P5-F07.png
output_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\03_수정완료\Part5\P5-F07.png
canvas: 1600 x 893 px
output_filename: P5-F07.png
title_policy: 내부 전체 제목·그림 코드 금지

문제:
그림 내부 코드·중복 제목·지시문 또는 국소 오탈자가 남아 있다.

필수 수정:
상단 코드·전체 제목 삭제.

통합 가이드 세부 지침: CSV required_correction을 따른다.

기본 프롬프트:
마스킹하지 않은 픽셀, 구도, 아이콘, 선, 화살표, 색상, 여백, 정확한 문구를 그대로 유지한다.
마스킹 영역의 코드·중복 제목·오탈자·잘못된 짧은 라벨만 삭제하거나 지정 문자열로 교체한다.
삭제 영역은 원래 흰 배경과 기존 테두리를 자연스럽게 복원한다.
새 제목, 새 코드, 워터마크, 생성 지시문, 설명문을 추가하지 않는다.
마스킹 영역 밖은 변경하지 않는다.
원본 픽셀 크기를 유지한다.

공통 네거티브:
no watermark, no prompt text, no placeholder text, no pseudo-Korean,
no misspelled Korean, no duplicate labels, no invented formula,
no tiny text, no decorative arrows, no gradient background,
no photorealistic style, no file name, no version string
```

## [C] P5-F08 · 위험관리 전체 순환 · 부분 수정

```text
[C] P5-F08 · 위험관리 전체 순환 · 부분 수정

input_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\02_부분수정\Part5\P5-F08.png
output_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\03_수정완료\Part5\P5-F08.png
canvas: 1600 x 893 px
output_filename: P5-F08.png
title_policy: 내부 전체 제목·그림 코드 금지

문제:
그림 내부 코드·중복 제목·지시문 또는 국소 오탈자가 남아 있다.

필수 수정:
상단 코드·전체 제목 삭제.

통합 가이드 세부 지침: CSV required_correction을 따른다.

기본 프롬프트:
마스킹하지 않은 픽셀, 구도, 아이콘, 선, 화살표, 색상, 여백, 정확한 문구를 그대로 유지한다.
마스킹 영역의 코드·중복 제목·오탈자·잘못된 짧은 라벨만 삭제하거나 지정 문자열로 교체한다.
삭제 영역은 원래 흰 배경과 기존 테두리를 자연스럽게 복원한다.
새 제목, 새 코드, 워터마크, 생성 지시문, 설명문을 추가하지 않는다.
마스킹 영역 밖은 변경하지 않는다.
원본 픽셀 크기를 유지한다.

공통 네거티브:
no watermark, no prompt text, no placeholder text, no pseudo-Korean,
no misspelled Korean, no duplicate labels, no invented formula,
no tiny text, no decorative arrows, no gradient background,
no photorealistic style, no file name, no version string
```

## [C] P5-F09 · 정보자산 식별과 분류 · 부분 수정

```text
[C] P5-F09 · 정보자산 식별과 분류 · 부분 수정

input_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\02_부분수정\Part5\P5-F09.png
output_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\03_수정완료\Part5\P5-F09.png
canvas: 1600 x 893 px
output_filename: P5-F09.png
title_policy: 내부 전체 제목·그림 코드 금지

문제:
그림 내부 코드·중복 제목·지시문 또는 국소 오탈자가 남아 있다.

필수 수정:
상단 코드·전체 제목 삭제.

통합 가이드 세부 지침: CSV required_correction을 따른다.

기본 프롬프트:
마스킹하지 않은 픽셀, 구도, 아이콘, 선, 화살표, 색상, 여백, 정확한 문구를 그대로 유지한다.
마스킹 영역의 코드·중복 제목·오탈자·잘못된 짧은 라벨만 삭제하거나 지정 문자열로 교체한다.
삭제 영역은 원래 흰 배경과 기존 테두리를 자연스럽게 복원한다.
새 제목, 새 코드, 워터마크, 생성 지시문, 설명문을 추가하지 않는다.
마스킹 영역 밖은 변경하지 않는다.
원본 픽셀 크기를 유지한다.

공통 네거티브:
no watermark, no prompt text, no placeholder text, no pseudo-Korean,
no misspelled Korean, no duplicate labels, no invented formula,
no tiny text, no decorative arrows, no gradient background,
no photorealistic style, no file name, no version string
```

## [C] P5-F12 · ISO 27005 위험평가 흐름 · 부분 수정

```text
[C] P5-F12 · ISO 27005 위험평가 흐름 · 부분 수정

input_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\02_부분수정\Part5\P5-F12.png
output_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\03_수정완료\Part5\P5-F12.png
canvas: 1600 x 893 px
output_filename: P5-F12.png
title_policy: 내부 전체 제목·그림 코드 금지

문제:
그림 내부 코드·중복 제목·지시문 또는 국소 오탈자가 남아 있다.

필수 수정:
상단 전체 제목 삭제.

통합 가이드 세부 지침: CSV required_correction을 따른다.

기본 프롬프트:
마스킹하지 않은 픽셀, 구도, 아이콘, 선, 화살표, 색상, 여백, 정확한 문구를 그대로 유지한다.
마스킹 영역의 코드·중복 제목·오탈자·잘못된 짧은 라벨만 삭제하거나 지정 문자열로 교체한다.
삭제 영역은 원래 흰 배경과 기존 테두리를 자연스럽게 복원한다.
새 제목, 새 코드, 워터마크, 생성 지시문, 설명문을 추가하지 않는다.
마스킹 영역 밖은 변경하지 않는다.
원본 픽셀 크기를 유지한다.

공통 네거티브:
no watermark, no prompt text, no placeholder text, no pseudo-Korean,
no misspelled Korean, no duplicate labels, no invented formula,
no tiny text, no decorative arrows, no gradient background,
no photorealistic style, no file name, no version string
```

## [C] P5-F13 · 위험분석 접근방법 비교 · 부분 수정

```text
[C] P5-F13 · 위험분석 접근방법 비교 · 부분 수정

input_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\02_부분수정\Part5\P5-F13.png
output_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\03_수정완료\Part5\P5-F13.png
canvas: 1600 x 893 px
output_filename: P5-F13.png
title_policy: 내부 전체 제목·그림 코드 금지

문제:
그림 내부 코드·중복 제목·지시문 또는 국소 오탈자가 남아 있다.

필수 수정:
깨진 전체 제목 삭제. 네 접근법 패널은 유지.

통합 가이드 세부 지침: CSV required_correction을 따른다.

기본 프롬프트:
마스킹하지 않은 픽셀, 구도, 아이콘, 선, 화살표, 색상, 여백, 정확한 문구를 그대로 유지한다.
마스킹 영역의 코드·중복 제목·오탈자·잘못된 짧은 라벨만 삭제하거나 지정 문자열로 교체한다.
삭제 영역은 원래 흰 배경과 기존 테두리를 자연스럽게 복원한다.
새 제목, 새 코드, 워터마크, 생성 지시문, 설명문을 추가하지 않는다.
마스킹 영역 밖은 변경하지 않는다.
원본 픽셀 크기를 유지한다.

공통 네거티브:
no watermark, no prompt text, no placeholder text, no pseudo-Korean,
no misspelled Korean, no duplicate labels, no invented formula,
no tiny text, no decorative arrows, no gradient background,
no photorealistic style, no file name, no version string
```

## [C] P5-F17 · 위험 매트릭스 · 부분 수정

```text
[C] P5-F17 · 위험 매트릭스 · 부분 수정

input_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\02_부분수정\Part5\P5-F17.png
output_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\03_수정완료\Part5\P5-F17.png
canvas: 1600 x 893 px
output_filename: P5-F17.png
title_policy: 내부 전체 제목·그림 코드 금지

문제:
그림 내부 코드·중복 제목·지시문 또는 국소 오탈자가 남아 있다.

필수 수정:
상단 코드·전체 제목 삭제.

통합 가이드 세부 지침: CSV required_correction을 따른다.

기본 프롬프트:
마스킹하지 않은 픽셀, 구도, 아이콘, 선, 화살표, 색상, 여백, 정확한 문구를 그대로 유지한다.
마스킹 영역의 코드·중복 제목·오탈자·잘못된 짧은 라벨만 삭제하거나 지정 문자열로 교체한다.
삭제 영역은 원래 흰 배경과 기존 테두리를 자연스럽게 복원한다.
새 제목, 새 코드, 워터마크, 생성 지시문, 설명문을 추가하지 않는다.
마스킹 영역 밖은 변경하지 않는다.
원본 픽셀 크기를 유지한다.

공통 네거티브:
no watermark, no prompt text, no placeholder text, no pseudo-Korean,
no misspelled Korean, no duplicate labels, no invented formula,
no tiny text, no decorative arrows, no gradient background,
no photorealistic style, no file name, no version string
```

## [C] P5-F19 · 잔여위험과 위험수용 · 부분 수정

```text
[C] P5-F19 · 잔여위험과 위험수용 · 부분 수정

input_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\02_부분수정\Part5\P5-F19.png
output_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\03_수정완료\Part5\P5-F19.png
canvas: 1600 x 893 px
output_filename: P5-F19.png
title_policy: 내부 전체 제목·그림 코드 금지

문제:
그림 내부 코드·중복 제목·지시문 또는 국소 오탈자가 남아 있다.

필수 수정:
상단 코드·전체 제목 삭제.

통합 가이드 세부 지침: CSV required_correction을 따른다.

기본 프롬프트:
마스킹하지 않은 픽셀, 구도, 아이콘, 선, 화살표, 색상, 여백, 정확한 문구를 그대로 유지한다.
마스킹 영역의 코드·중복 제목·오탈자·잘못된 짧은 라벨만 삭제하거나 지정 문자열로 교체한다.
삭제 영역은 원래 흰 배경과 기존 테두리를 자연스럽게 복원한다.
새 제목, 새 코드, 워터마크, 생성 지시문, 설명문을 추가하지 않는다.
마스킹 영역 밖은 변경하지 않는다.
원본 픽셀 크기를 유지한다.

공통 네거티브:
no watermark, no prompt text, no placeholder text, no pseudo-Korean,
no misspelled Korean, no duplicate labels, no invented formula,
no tiny text, no decorative arrows, no gradient background,
no photorealistic style, no file name, no version string
```

## [C] P5-F20 · 위험등록부와 처리계획 · 부분 수정

```text
[C] P5-F20 · 위험등록부와 처리계획 · 부분 수정

input_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\02_부분수정\Part5\P5-F20.png
output_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\03_수정완료\Part5\P5-F20.png
canvas: 1600 x 893 px
output_filename: P5-F20.png
title_policy: 내부 전체 제목·그림 코드 금지

문제:
그림 내부 코드·중복 제목·지시문 또는 국소 오탈자가 남아 있다.

필수 수정:
상단 코드·전체 제목 삭제.

통합 가이드 세부 지침: CSV required_correction을 따른다.

기본 프롬프트:
마스킹하지 않은 픽셀, 구도, 아이콘, 선, 화살표, 색상, 여백, 정확한 문구를 그대로 유지한다.
마스킹 영역의 코드·중복 제목·오탈자·잘못된 짧은 라벨만 삭제하거나 지정 문자열로 교체한다.
삭제 영역은 원래 흰 배경과 기존 테두리를 자연스럽게 복원한다.
새 제목, 새 코드, 워터마크, 생성 지시문, 설명문을 추가하지 않는다.
마스킹 영역 밖은 변경하지 않는다.
원본 픽셀 크기를 유지한다.

공통 네거티브:
no watermark, no prompt text, no placeholder text, no pseudo-Korean,
no misspelled Korean, no duplicate labels, no invented formula,
no tiny text, no decorative arrows, no gradient background,
no photorealistic style, no file name, no version string
```

## [C] P5-F24 · 인적 보안 생명주기 · 부분 수정

```text
[C] P5-F24 · 인적 보안 생명주기 · 부분 수정

input_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\02_부분수정\Part5\P5-F24.png
output_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\03_수정완료\Part5\P5-F24.png
canvas: 1600 x 893 px
output_filename: P5-F24.png
title_policy: 내부 전체 제목·그림 코드 금지

문제:
그림 내부 코드·중복 제목·지시문 또는 국소 오탈자가 남아 있다.

필수 수정:
깨진 전체 제목 삭제. 채용 전·재직·직무변경·퇴직 단계는 유지.

통합 가이드 세부 지침: CSV required_correction을 따른다.

기본 프롬프트:
마스킹하지 않은 픽셀, 구도, 아이콘, 선, 화살표, 색상, 여백, 정확한 문구를 그대로 유지한다.
마스킹 영역의 코드·중복 제목·오탈자·잘못된 짧은 라벨만 삭제하거나 지정 문자열로 교체한다.
삭제 영역은 원래 흰 배경과 기존 테두리를 자연스럽게 복원한다.
새 제목, 새 코드, 워터마크, 생성 지시문, 설명문을 추가하지 않는다.
마스킹 영역 밖은 변경하지 않는다.
원본 픽셀 크기를 유지한다.

공통 네거티브:
no watermark, no prompt text, no placeholder text, no pseudo-Korean,
no misspelled Korean, no duplicate labels, no invented formula,
no tiny text, no decorative arrows, no gradient background,
no photorealistic style, no file name, no version string
```

## [C] P5-F25 · 외부자·공급망 보안 생명주기 · 부분 수정

```text
[C] P5-F25 · 외부자·공급망 보안 생명주기 · 부분 수정

input_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\02_부분수정\Part5\P5-F25.png
output_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\03_수정완료\Part5\P5-F25.png
canvas: 1600 x 893 px
output_filename: P5-F25.png
title_policy: 내부 전체 제목·그림 코드 금지

문제:
그림 내부 코드·중복 제목·지시문 또는 국소 오탈자가 남아 있다.

필수 수정:
상단 전체 제목 삭제.

통합 가이드 세부 지침: CSV required_correction을 따른다.

기본 프롬프트:
마스킹하지 않은 픽셀, 구도, 아이콘, 선, 화살표, 색상, 여백, 정확한 문구를 그대로 유지한다.
마스킹 영역의 코드·중복 제목·오탈자·잘못된 짧은 라벨만 삭제하거나 지정 문자열로 교체한다.
삭제 영역은 원래 흰 배경과 기존 테두리를 자연스럽게 복원한다.
새 제목, 새 코드, 워터마크, 생성 지시문, 설명문을 추가하지 않는다.
마스킹 영역 밖은 변경하지 않는다.
원본 픽셀 크기를 유지한다.

공통 네거티브:
no watermark, no prompt text, no placeholder text, no pseudo-Korean,
no misspelled Korean, no duplicate labels, no invented formula,
no tiny text, no decorative arrows, no gradient background,
no photorealistic style, no file name, no version string
```

## [C] P5-F27 · 형상·변경관리 흐름 · 부분 수정

```text
[C] P5-F27 · 형상·변경관리 흐름 · 부분 수정

input_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\02_부분수정\Part5\P5-F27.png
output_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\03_수정완료\Part5\P5-F27.png
canvas: 1600 x 893 px
output_filename: P5-F27.png
title_policy: 내부 전체 제목·그림 코드 금지

문제:
그림 내부 코드·중복 제목·지시문 또는 국소 오탈자가 남아 있다.

필수 수정:
깨진 전체 제목 삭제. 변경관리 단계는 유지.

통합 가이드 세부 지침: CSV required_correction을 따른다.

기본 프롬프트:
마스킹하지 않은 픽셀, 구도, 아이콘, 선, 화살표, 색상, 여백, 정확한 문구를 그대로 유지한다.
마스킹 영역의 코드·중복 제목·오탈자·잘못된 짧은 라벨만 삭제하거나 지정 문자열로 교체한다.
삭제 영역은 원래 흰 배경과 기존 테두리를 자연스럽게 복원한다.
새 제목, 새 코드, 워터마크, 생성 지시문, 설명문을 추가하지 않는다.
마스킹 영역 밖은 변경하지 않는다.
원본 픽셀 크기를 유지한다.

공통 네거티브:
no watermark, no prompt text, no placeholder text, no pseudo-Korean,
no misspelled Korean, no duplicate labels, no invented formula,
no tiny text, no decorative arrows, no gradient background,
no photorealistic style, no file name, no version string
```

## [C] P5-F32 · BIA 업무영향분석 흐름 · 부분 수정

```text
[C] P5-F32 · BIA 업무영향분석 흐름 · 부분 수정

input_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\02_부분수정\Part5\P5-F32.png
output_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\03_수정완료\Part5\P5-F32.png
canvas: 1600 x 893 px
output_filename: P5-F32.png
title_policy: 내부 전체 제목·그림 코드 금지

문제:
그림 내부 코드·중복 제목·지시문 또는 국소 오탈자가 남아 있다.

필수 수정:
상단 코드·전체 제목 삭제.

통합 가이드 세부 지침: CSV required_correction을 따른다.

기본 프롬프트:
마스킹하지 않은 픽셀, 구도, 아이콘, 선, 화살표, 색상, 여백, 정확한 문구를 그대로 유지한다.
마스킹 영역의 코드·중복 제목·오탈자·잘못된 짧은 라벨만 삭제하거나 지정 문자열로 교체한다.
삭제 영역은 원래 흰 배경과 기존 테두리를 자연스럽게 복원한다.
새 제목, 새 코드, 워터마크, 생성 지시문, 설명문을 추가하지 않는다.
마스킹 영역 밖은 변경하지 않는다.
원본 픽셀 크기를 유지한다.

공통 네거티브:
no watermark, no prompt text, no placeholder text, no pseudo-Korean,
no misspelled Korean, no duplicate labels, no invented formula,
no tiny text, no decorative arrows, no gradient background,
no photorealistic style, no file name, no version string
```

## [C] P5-F36 · 업무연속성 훈련 유형 · 부분 수정

```text
[C] P5-F36 · 업무연속성 훈련 유형 · 부분 수정

input_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\02_부분수정\Part5\P5-F36.png
output_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\03_수정완료\Part5\P5-F36.png
canvas: 1600 x 893 px
output_filename: P5-F36.png
title_policy: 내부 전체 제목·그림 코드 금지

문제:
그림 내부 코드·중복 제목·지시문 또는 국소 오탈자가 남아 있다.

필수 수정:
상단 코드·전체 제목 삭제.

통합 가이드 세부 지침: CSV required_correction을 따른다.

기본 프롬프트:
마스킹하지 않은 픽셀, 구도, 아이콘, 선, 화살표, 색상, 여백, 정확한 문구를 그대로 유지한다.
마스킹 영역의 코드·중복 제목·오탈자·잘못된 짧은 라벨만 삭제하거나 지정 문자열로 교체한다.
삭제 영역은 원래 흰 배경과 기존 테두리를 자연스럽게 복원한다.
새 제목, 새 코드, 워터마크, 생성 지시문, 설명문을 추가하지 않는다.
마스킹 영역 밖은 변경하지 않는다.
원본 픽셀 크기를 유지한다.

공통 네거티브:
no watermark, no prompt text, no placeholder text, no pseudo-Korean,
no misspelled Korean, no duplicate labels, no invented formula,
no tiny text, no decorative arrows, no gradient background,
no photorealistic style, no file name, no version string
```

## [C] P5-F38 · 사고 심각도와 트리아지 · 부분 수정

```text
[C] P5-F38 · 사고 심각도와 트리아지 · 부분 수정

input_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\02_부분수정\Part5\P5-F38.png
output_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\03_수정완료\Part5\P5-F38.png
canvas: 1600 x 893 px
output_filename: P5-F38.png
title_policy: 내부 전체 제목·그림 코드 금지

문제:
그림 내부 코드·중복 제목·지시문 또는 국소 오탈자가 남아 있다.

필수 수정:
상단 코드·전체 제목 삭제.

통합 가이드 세부 지침: CSV required_correction을 따른다.

기본 프롬프트:
마스킹하지 않은 픽셀, 구도, 아이콘, 선, 화살표, 색상, 여백, 정확한 문구를 그대로 유지한다.
마스킹 영역의 코드·중복 제목·오탈자·잘못된 짧은 라벨만 삭제하거나 지정 문자열로 교체한다.
삭제 영역은 원래 흰 배경과 기존 테두리를 자연스럽게 복원한다.
새 제목, 새 코드, 워터마크, 생성 지시문, 설명문을 추가하지 않는다.
마스킹 영역 밖은 변경하지 않는다.
원본 픽셀 크기를 유지한다.

공통 네거티브:
no watermark, no prompt text, no placeholder text, no pseudo-Korean,
no misspelled Korean, no duplicate labels, no invented formula,
no tiny text, no decorative arrows, no gradient background,
no photorealistic style, no file name, no version string
```

## [C] P5-F45 · ISMS와 ISMS-P 구조 비교 · 부분 수정

```text
[C] P5-F45 · ISMS와 ISMS-P 구조 비교 · 부분 수정

input_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\02_부분수정\Part5\P5-F45.png
output_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\03_수정완료\Part5\P5-F45.png
canvas: 1600 x 893 px
output_filename: P5-F45.png
title_policy: 내부 전체 제목·그림 코드 금지

문제:
그림 내부 코드·중복 제목·지시문 또는 국소 오탈자가 남아 있다.

필수 수정:
상단 코드·전체 제목 삭제.

통합 가이드 세부 지침: CSV required_correction을 따른다.

기본 프롬프트:
마스킹하지 않은 픽셀, 구도, 아이콘, 선, 화살표, 색상, 여백, 정확한 문구를 그대로 유지한다.
마스킹 영역의 코드·중복 제목·오탈자·잘못된 짧은 라벨만 삭제하거나 지정 문자열로 교체한다.
삭제 영역은 원래 흰 배경과 기존 테두리를 자연스럽게 복원한다.
새 제목, 새 코드, 워터마크, 생성 지시문, 설명문을 추가하지 않는다.
마스킹 영역 밖은 변경하지 않는다.
원본 픽셀 크기를 유지한다.

공통 네거티브:
no watermark, no prompt text, no placeholder text, no pseudo-Korean,
no misspelled Korean, no duplicate labels, no invented formula,
no tiny text, no decorative arrows, no gradient background,
no photorealistic style, no file name, no version string
```

## [C] P5-F48 · ISMS-P 인증 절차 · 부분 수정

```text
[C] P5-F48 · ISMS-P 인증 절차 · 부분 수정

input_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\02_부분수정\Part5\P5-F48.png
output_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\03_수정완료\Part5\P5-F48.png
canvas: 1600 x 893 px
output_filename: P5-F48.png
title_policy: 내부 전체 제목·그림 코드 금지

문제:
그림 내부 코드·중복 제목·지시문 또는 국소 오탈자가 남아 있다.

필수 수정:
상단 코드·전체 제목 삭제.

통합 가이드 세부 지침: CSV required_correction을 따른다.

기본 프롬프트:
마스킹하지 않은 픽셀, 구도, 아이콘, 선, 화살표, 색상, 여백, 정확한 문구를 그대로 유지한다.
마스킹 영역의 코드·중복 제목·오탈자·잘못된 짧은 라벨만 삭제하거나 지정 문자열로 교체한다.
삭제 영역은 원래 흰 배경과 기존 테두리를 자연스럽게 복원한다.
새 제목, 새 코드, 워터마크, 생성 지시문, 설명문을 추가하지 않는다.
마스킹 영역 밖은 변경하지 않는다.
원본 픽셀 크기를 유지한다.

공통 네거티브:
no watermark, no prompt text, no placeholder text, no pseudo-Korean,
no misspelled Korean, no duplicate labels, no invented formula,
no tiny text, no decorative arrows, no gradient background,
no photorealistic style, no file name, no version string
```

## [C] P5-F52 · CCRA 국제상호인정 · 부분 수정

```text
[C] P5-F52 · CCRA 국제상호인정 · 부분 수정

input_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\02_부분수정\Part5\P5-F52.png
output_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\03_수정완료\Part5\P5-F52.png
canvas: 1600 x 893 px
output_filename: P5-F52.png
title_policy: 내부 전체 제목·그림 코드 금지

문제:
그림 내부 코드·중복 제목·지시문 또는 국소 오탈자가 남아 있다.

필수 수정:
깨진 전체 제목 삭제. CCRA 상호인정 구조는 유지.

통합 가이드 세부 지침: CSV required_correction을 따른다.

기본 프롬프트:
마스킹하지 않은 픽셀, 구도, 아이콘, 선, 화살표, 색상, 여백, 정확한 문구를 그대로 유지한다.
마스킹 영역의 코드·중복 제목·오탈자·잘못된 짧은 라벨만 삭제하거나 지정 문자열로 교체한다.
삭제 영역은 원래 흰 배경과 기존 테두리를 자연스럽게 복원한다.
새 제목, 새 코드, 워터마크, 생성 지시문, 설명문을 추가하지 않는다.
마스킹 영역 밖은 변경하지 않는다.
원본 픽셀 크기를 유지한다.

공통 네거티브:
no watermark, no prompt text, no placeholder text, no pseudo-Korean,
no misspelled Korean, no duplicate labels, no invented formula,
no tiny text, no decorative arrows, no gradient background,
no photorealistic style, no file name, no version string
```

## [C] P5-F59 · 디지털 저작권 권리 구조 · 부분 수정

```text
[C] P5-F59 · 디지털 저작권 권리 구조 · 부분 수정

input_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\02_부분수정\Part5\P5-F59.png
output_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\03_수정완료\Part5\P5-F59.png
canvas: 1600 x 893 px
output_filename: P5-F59.png
title_policy: 내부 전체 제목·그림 코드 금지

문제:
그림 내부 코드·중복 제목·지시문 또는 국소 오탈자가 남아 있다.

필수 수정:
상단 코드·전체 제목 삭제.

통합 가이드 세부 지침: CSV required_correction을 따른다.

기본 프롬프트:
마스킹하지 않은 픽셀, 구도, 아이콘, 선, 화살표, 색상, 여백, 정확한 문구를 그대로 유지한다.
마스킹 영역의 코드·중복 제목·오탈자·잘못된 짧은 라벨만 삭제하거나 지정 문자열로 교체한다.
삭제 영역은 원래 흰 배경과 기존 테두리를 자연스럽게 복원한다.
새 제목, 새 코드, 워터마크, 생성 지시문, 설명문을 추가하지 않는다.
마스킹 영역 밖은 변경하지 않는다.
원본 픽셀 크기를 유지한다.

공통 네거티브:
no watermark, no prompt text, no placeholder text, no pseudo-Korean,
no misspelled Korean, no duplicate labels, no invented formula,
no tiny text, no decorative arrows, no gradient background,
no photorealistic style, no file name, no version string
```

## [C] P5-F61 · 책임 있는 취약점 공개 · 부분 수정

```text
[C] P5-F61 · 책임 있는 취약점 공개 · 부분 수정

input_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\02_부분수정\Part5\P5-F61.png
output_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\03_수정완료\Part5\P5-F61.png
canvas: 1600 x 893 px
output_filename: P5-F61.png
title_policy: 내부 전체 제목·그림 코드 금지

문제:
그림 내부 코드·중복 제목·지시문 또는 국소 오탈자가 남아 있다.

필수 수정:
상단 코드·깨진 전체 제목 삭제. 절차 흐름은 유지.

통합 가이드 세부 지침: CSV required_correction을 따른다.

기본 프롬프트:
마스킹하지 않은 픽셀, 구도, 아이콘, 선, 화살표, 색상, 여백, 정확한 문구를 그대로 유지한다.
마스킹 영역의 코드·중복 제목·오탈자·잘못된 짧은 라벨만 삭제하거나 지정 문자열로 교체한다.
삭제 영역은 원래 흰 배경과 기존 테두리를 자연스럽게 복원한다.
새 제목, 새 코드, 워터마크, 생성 지시문, 설명문을 추가하지 않는다.
마스킹 영역 밖은 변경하지 않는다.
원본 픽셀 크기를 유지한다.

공통 네거티브:
no watermark, no prompt text, no placeholder text, no pseudo-Korean,
no misspelled Korean, no duplicate labels, no invented formula,
no tiny text, no decorative arrows, no gradient background,
no photorealistic style, no file name, no version string
```

## [C] P5-F62 · 이용자·개인정보취급자 금지행위 · 부분 수정

```text
[C] P5-F62 · 이용자·개인정보취급자 금지행위 · 부분 수정

input_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\02_부분수정\Part5\P5-F62.png
output_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\03_수정완료\Part5\P5-F62.png
canvas: 1600 x 893 px
output_filename: P5-F62.png
title_policy: 내부 전체 제목·그림 코드 금지

문제:
그림 내부 코드·중복 제목·지시문 또는 국소 오탈자가 남아 있다.

필수 수정:
상단 전체 제목 삭제.

통합 가이드 세부 지침: CSV required_correction을 따른다.

기본 프롬프트:
마스킹하지 않은 픽셀, 구도, 아이콘, 선, 화살표, 색상, 여백, 정확한 문구를 그대로 유지한다.
마스킹 영역의 코드·중복 제목·오탈자·잘못된 짧은 라벨만 삭제하거나 지정 문자열로 교체한다.
삭제 영역은 원래 흰 배경과 기존 테두리를 자연스럽게 복원한다.
새 제목, 새 코드, 워터마크, 생성 지시문, 설명문을 추가하지 않는다.
마스킹 영역 밖은 변경하지 않는다.
원본 픽셀 크기를 유지한다.

공통 네거티브:
no watermark, no prompt text, no placeholder text, no pseudo-Korean,
no misspelled Korean, no duplicate labels, no invented formula,
no tiny text, no decorative arrows, no gradient background,
no photorealistic style, no file name, no version string
```

## [C] P5-F67 · 불법정보·스팸·망 안정성 · 부분 수정

```text
[C] P5-F67 · 불법정보·스팸·망 안정성 · 부분 수정

input_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\02_부분수정\Part5\P5-F67.png
output_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\03_수정완료\Part5\P5-F67.png
canvas: 1600 x 893 px
output_filename: P5-F67.png
title_policy: 내부 전체 제목·그림 코드 금지

문제:
그림 내부 코드·중복 제목·지시문 또는 국소 오탈자가 남아 있다.

필수 수정:
좌상단 그림 코드 삭제.

통합 가이드 세부 지침: CSV required_correction을 따른다.

기본 프롬프트:
마스킹하지 않은 픽셀, 구도, 아이콘, 선, 화살표, 색상, 여백, 정확한 문구를 그대로 유지한다.
마스킹 영역의 코드·중복 제목·오탈자·잘못된 짧은 라벨만 삭제하거나 지정 문자열로 교체한다.
삭제 영역은 원래 흰 배경과 기존 테두리를 자연스럽게 복원한다.
새 제목, 새 코드, 워터마크, 생성 지시문, 설명문을 추가하지 않는다.
마스킹 영역 밖은 변경하지 않는다.
원본 픽셀 크기를 유지한다.

공통 네거티브:
no watermark, no prompt text, no placeholder text, no pseudo-Korean,
no misspelled Korean, no duplicate labels, no invented formula,
no tiny text, no decorative arrows, no gradient background,
no photorealistic style, no file name, no version string
```

## [C] P5-F69 · 주요정보통신기반시설 지정 기준 · 부분 수정

```text
[C] P5-F69 · 주요정보통신기반시설 지정 기준 · 부분 수정

input_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\02_부분수정\Part5\P5-F69.png
output_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\03_수정완료\Part5\P5-F69.png
canvas: 1600 x 893 px
output_filename: P5-F69.png
title_policy: 내부 전체 제목·그림 코드 금지

문제:
그림 내부 코드·중복 제목·지시문 또는 국소 오탈자가 남아 있다.

필수 수정:
깨진 전체 제목 삭제. 지정 기준 패널은 유지.

통합 가이드 세부 지침: CSV required_correction을 따른다.

기본 프롬프트:
마스킹하지 않은 픽셀, 구도, 아이콘, 선, 화살표, 색상, 여백, 정확한 문구를 그대로 유지한다.
마스킹 영역의 코드·중복 제목·오탈자·잘못된 짧은 라벨만 삭제하거나 지정 문자열로 교체한다.
삭제 영역은 원래 흰 배경과 기존 테두리를 자연스럽게 복원한다.
새 제목, 새 코드, 워터마크, 생성 지시문, 설명문을 추가하지 않는다.
마스킹 영역 밖은 변경하지 않는다.
원본 픽셀 크기를 유지한다.

공통 네거티브:
no watermark, no prompt text, no placeholder text, no pseudo-Korean,
no misspelled Korean, no duplicate labels, no invented formula,
no tiny text, no decorative arrows, no gradient background,
no photorealistic style, no file name, no version string
```

## [C] P5-F70 · 보호계획과 취약점 분석·평가 · 부분 수정

```text
[C] P5-F70 · 보호계획과 취약점 분석·평가 · 부분 수정

input_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\02_부분수정\Part5\P5-F70.png
output_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\03_수정완료\Part5\P5-F70.png
canvas: 1600 x 893 px
output_filename: P5-F70.png
title_policy: 내부 전체 제목·그림 코드 금지

문제:
그림 내부 코드·중복 제목·지시문 또는 국소 오탈자가 남아 있다.

필수 수정:
그림 내부 코드 삭제.

통합 가이드 세부 지침: CSV required_correction을 따른다.

기본 프롬프트:
마스킹하지 않은 픽셀, 구도, 아이콘, 선, 화살표, 색상, 여백, 정확한 문구를 그대로 유지한다.
마스킹 영역의 코드·중복 제목·오탈자·잘못된 짧은 라벨만 삭제하거나 지정 문자열로 교체한다.
삭제 영역은 원래 흰 배경과 기존 테두리를 자연스럽게 복원한다.
새 제목, 새 코드, 워터마크, 생성 지시문, 설명문을 추가하지 않는다.
마스킹 영역 밖은 변경하지 않는다.
원본 픽셀 크기를 유지한다.

공통 네거티브:
no watermark, no prompt text, no placeholder text, no pseudo-Korean,
no misspelled Korean, no duplicate labels, no invented formula,
no tiny text, no decorative arrows, no gradient background,
no photorealistic style, no file name, no version string
```

## [C] P5-F75 · 개인정보·가명정보·익명정보 · 부분 수정

```text
[C] P5-F75 · 개인정보·가명정보·익명정보 · 부분 수정

input_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\02_부분수정\Part5\P5-F75.png
output_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\03_수정완료\Part5\P5-F75.png
canvas: 1600 x 893 px
output_filename: P5-F75.png
title_policy: 내부 전체 제목·그림 코드 금지

문제:
그림 내부 코드·중복 제목·지시문 또는 국소 오탈자가 남아 있다.

필수 수정:
상단 전체 제목 삭제. 개인정보·가명정보·익명정보 구분은 유지.

통합 가이드 세부 지침: CSV required_correction을 따른다.

기본 프롬프트:
마스킹하지 않은 픽셀, 구도, 아이콘, 선, 화살표, 색상, 여백, 정확한 문구를 그대로 유지한다.
마스킹 영역의 코드·중복 제목·오탈자·잘못된 짧은 라벨만 삭제하거나 지정 문자열로 교체한다.
삭제 영역은 원래 흰 배경과 기존 테두리를 자연스럽게 복원한다.
새 제목, 새 코드, 워터마크, 생성 지시문, 설명문을 추가하지 않는다.
마스킹 영역 밖은 변경하지 않는다.
원본 픽셀 크기를 유지한다.

공통 네거티브:
no watermark, no prompt text, no placeholder text, no pseudo-Korean,
no misspelled Korean, no duplicate labels, no invented formula,
no tiny text, no decorative arrows, no gradient background,
no photorealistic style, no file name, no version string
```

## [C] P5-F78 · 동의와 고지 항목 · 부분 수정

```text
[C] P5-F78 · 동의와 고지 항목 · 부분 수정

input_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\02_부분수정\Part5\P5-F78.png
output_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\03_수정완료\Part5\P5-F78.png
canvas: 1600 x 893 px
output_filename: P5-F78.png
title_policy: 내부 전체 제목·그림 코드 금지

문제:
그림 내부 코드·중복 제목·지시문 또는 국소 오탈자가 남아 있다.

필수 수정:
상단 코드·전체 제목 삭제.

통합 가이드 세부 지침: CSV required_correction을 따른다.

기본 프롬프트:
마스킹하지 않은 픽셀, 구도, 아이콘, 선, 화살표, 색상, 여백, 정확한 문구를 그대로 유지한다.
마스킹 영역의 코드·중복 제목·오탈자·잘못된 짧은 라벨만 삭제하거나 지정 문자열로 교체한다.
삭제 영역은 원래 흰 배경과 기존 테두리를 자연스럽게 복원한다.
새 제목, 새 코드, 워터마크, 생성 지시문, 설명문을 추가하지 않는다.
마스킹 영역 밖은 변경하지 않는다.
원본 픽셀 크기를 유지한다.

공통 네거티브:
no watermark, no prompt text, no placeholder text, no pseudo-Korean,
no misspelled Korean, no duplicate labels, no invented formula,
no tiny text, no decorative arrows, no gradient background,
no photorealistic style, no file name, no version string
```

## [C] P5-F81 · 정보주체 권리 · 부분 수정

```text
[C] P5-F81 · 정보주체 권리 · 부분 수정

input_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\02_부분수정\Part5\P5-F81.png
output_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\03_수정완료\Part5\P5-F81.png
canvas: 1600 x 893 px
output_filename: P5-F81.png
title_policy: 내부 전체 제목·그림 코드 금지

문제:
그림 내부 코드·중복 제목·지시문 또는 국소 오탈자가 남아 있다.

필수 수정:
중복된 코드·전체 제목을 모두 삭제. 권리행사 흐름은 유지.

통합 가이드 세부 지침: CSV required_correction을 따른다.

기본 프롬프트:
마스킹하지 않은 픽셀, 구도, 아이콘, 선, 화살표, 색상, 여백, 정확한 문구를 그대로 유지한다.
마스킹 영역의 코드·중복 제목·오탈자·잘못된 짧은 라벨만 삭제하거나 지정 문자열로 교체한다.
삭제 영역은 원래 흰 배경과 기존 테두리를 자연스럽게 복원한다.
새 제목, 새 코드, 워터마크, 생성 지시문, 설명문을 추가하지 않는다.
마스킹 영역 밖은 변경하지 않는다.
원본 픽셀 크기를 유지한다.

공통 네거티브:
no watermark, no prompt text, no placeholder text, no pseudo-Korean,
no misspelled Korean, no duplicate labels, no invented formula,
no tiny text, no decorative arrows, no gradient background,
no photorealistic style, no file name, no version string
```

## [C] P5-F82 · 개인정보 보호책임자와 거버넌스 · 부분 수정

```text
[C] P5-F82 · 개인정보 보호책임자와 거버넌스 · 부분 수정

input_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\02_부분수정\Part5\P5-F82.png
output_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\03_수정완료\Part5\P5-F82.png
canvas: 1600 x 893 px
output_filename: P5-F82.png
title_policy: 내부 전체 제목·그림 코드 금지

문제:
그림 내부 코드·중복 제목·지시문 또는 국소 오탈자가 남아 있다.

필수 수정:
상단 코드·전체 제목 삭제.

통합 가이드 세부 지침: CSV required_correction을 따른다.

기본 프롬프트:
마스킹하지 않은 픽셀, 구도, 아이콘, 선, 화살표, 색상, 여백, 정확한 문구를 그대로 유지한다.
마스킹 영역의 코드·중복 제목·오탈자·잘못된 짧은 라벨만 삭제하거나 지정 문자열로 교체한다.
삭제 영역은 원래 흰 배경과 기존 테두리를 자연스럽게 복원한다.
새 제목, 새 코드, 워터마크, 생성 지시문, 설명문을 추가하지 않는다.
마스킹 영역 밖은 변경하지 않는다.
원본 픽셀 크기를 유지한다.

공통 네거티브:
no watermark, no prompt text, no placeholder text, no pseudo-Korean,
no misspelled Korean, no duplicate labels, no invented formula,
no tiny text, no decorative arrows, no gradient background,
no photorealistic style, no file name, no version string
```

## [C] P5-F86 · 개인정보 영향평가 PIA와 CCTV · 부분 수정

```text
[C] P5-F86 · 개인정보 영향평가 PIA와 CCTV · 부분 수정

input_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\02_부분수정\Part5\P5-F86.png
output_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\03_수정완료\Part5\P5-F86.png
canvas: 1600 x 893 px
output_filename: P5-F86.png
title_policy: 내부 전체 제목·그림 코드 금지

문제:
그림 내부 코드·중복 제목·지시문 또는 국소 오탈자가 남아 있다.

필수 수정:
상단 전체 제목 삭제. PIA와 CCTV 두 패널은 유지.

통합 가이드 세부 지침: CSV required_correction을 따른다.

기본 프롬프트:
마스킹하지 않은 픽셀, 구도, 아이콘, 선, 화살표, 색상, 여백, 정확한 문구를 그대로 유지한다.
마스킹 영역의 코드·중복 제목·오탈자·잘못된 짧은 라벨만 삭제하거나 지정 문자열로 교체한다.
삭제 영역은 원래 흰 배경과 기존 테두리를 자연스럽게 복원한다.
새 제목, 새 코드, 워터마크, 생성 지시문, 설명문을 추가하지 않는다.
마스킹 영역 밖은 변경하지 않는다.
원본 픽셀 크기를 유지한다.

공통 네거티브:
no watermark, no prompt text, no placeholder text, no pseudo-Korean,
no misspelled Korean, no duplicate labels, no invented formula,
no tiny text, no decorative arrows, no gradient background,
no photorealistic style, no file name, no version string
```

## [C] P5-F87 · 보유기간·파기·분리보관 · 부분 수정

```text
[C] P5-F87 · 보유기간·파기·분리보관 · 부분 수정

input_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\02_부분수정\Part5\P5-F87.png
output_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\03_수정완료\Part5\P5-F87.png
canvas: 1600 x 893 px
output_filename: P5-F87.png
title_policy: 내부 전체 제목·그림 코드 금지

문제:
그림 내부 코드·중복 제목·지시문 또는 국소 오탈자가 남아 있다.

필수 수정:
상단 코드·전체 제목 삭제.

통합 가이드 세부 지침: CSV required_correction을 따른다.

기본 프롬프트:
마스킹하지 않은 픽셀, 구도, 아이콘, 선, 화살표, 색상, 여백, 정확한 문구를 그대로 유지한다.
마스킹 영역의 코드·중복 제목·오탈자·잘못된 짧은 라벨만 삭제하거나 지정 문자열로 교체한다.
삭제 영역은 원래 흰 배경과 기존 테두리를 자연스럽게 복원한다.
새 제목, 새 코드, 워터마크, 생성 지시문, 설명문을 추가하지 않는다.
마스킹 영역 밖은 변경하지 않는다.
원본 픽셀 크기를 유지한다.

공통 네거티브:
no watermark, no prompt text, no placeholder text, no pseudo-Korean,
no misspelled Korean, no duplicate labels, no invented formula,
no tiny text, no decorative arrows, no gradient background,
no photorealistic style, no file name, no version string
```

## [C] P5-F88 · 현행법과 역사적 기출 함정 · 부분 수정

```text
[C] P5-F88 · 현행법과 역사적 기출 함정 · 부분 수정

input_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\02_부분수정\Part5\P5-F88.png
output_abs: C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2\03_수정완료\Part5\P5-F88.png
canvas: 1600 x 893 px
output_filename: P5-F88.png
title_policy: 내부 전체 제목·그림 코드 금지

문제:
그림 내부 코드·중복 제목·지시문 또는 국소 오탈자가 남아 있다.

필수 수정:
상단 전체 제목 삭제. 현행·역사 비교 본체는 유지.

통합 가이드 세부 지침: CSV required_correction을 따른다.

기본 프롬프트:
마스킹하지 않은 픽셀, 구도, 아이콘, 선, 화살표, 색상, 여백, 정확한 문구를 그대로 유지한다.
마스킹 영역의 코드·중복 제목·오탈자·잘못된 짧은 라벨만 삭제하거나 지정 문자열로 교체한다.
삭제 영역은 원래 흰 배경과 기존 테두리를 자연스럽게 복원한다.
새 제목, 새 코드, 워터마크, 생성 지시문, 설명문을 추가하지 않는다.
마스킹 영역 밖은 변경하지 않는다.
원본 픽셀 크기를 유지한다.

공통 네거티브:
no watermark, no prompt text, no placeholder text, no pseudo-Korean,
no misspelled Korean, no duplicate labels, no invented formula,
no tiny text, no decorative arrows, no gradient background,
no photorealistic style, no file name, no version string
```


