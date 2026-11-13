# smart-manufacture — 컨베이어 한 대로 배우는 Physical AI 실습 자료

「스마트제조 · 산업자동화 — 컨베이어 한 대로 배우는 Physical AI」 교재의 예제 · 데이터 · 완성 소스 코드입니다.
폴더는 교재의 PART 별로 나뉘어 있고, 각 PART 안의 `라즈베리파이` 폴더는 라즈베리파이에서 실행하는 파일입니다.

| 폴더 | PC 에 복사할 곳 | 라즈베리파이 폴더 → 복사할 곳 |
|---|---|---|
| `PART02` 3D 모델 | `STL` 출력용 · `F3D` Fusion 원본 (부품별 .f3d + 조립품 `02-00_컨베이어_조립품.f3z`) · `STEP` 구매 부품 단순화 모델 · `부품목록.csv` — 파일 이름 앞 번호 `02-n` = 교재 PART02 5 장 5) 「n. ○○ 모델링」 | — |
| `PART03` 전기 도면 | `ConveyorRaspberryPi.qet` (QElectroTech 에서 열기), `ConveyorRaspberryPi.pdf` (바로 보기), `전선목록.csv` (전선 15 가닥), `전기부품목록.csv`, `부품그림` (도면에 넣은 부품 그림) | — |
| `PART04` | `requirements.txt` — AI 패키지 목록 (`C:\PART07` 가상환경에 설치) | — |
| `PART05` Python | `C:\PART05` (`ex_*.py`, `web\panel.html`, `연습\`) | `\\192.168.7.1\projects\PART05` (`p01 ~ p04`, `cycle_*`, `RaspberryPi_cycle.py`, `panel.html`) |
| `PART06` OpenPLC | `C:\PART06` (`.st` 는 OpenPLC Editor 에서 열기, `ex_*.py`, `web\panel.html`) | `\\192.168.7.1\projects\PART06` (`web_server.py`, `hmi_view`, `hmi_plc`) |
| `PART07` Physical AI | `C:\PART07` (디지털 트윈 · 지도 · 모방 · 강화학습), `예시표` (학습 결과 예시 JSON) | `\\192.168.7.1\projects\PART07` (`ai_run_gpio.py 표파일.json`) |
| `APPENDIX` 배포 이미지 | 라즈베리파이 OS 이미지 링크 (https://vo.la/ZUvFmAM) · 굽는 법 · 접속 방법 (로그인 이름 `twiniex`) | — |

## 받기
- 초록색 **Code** 단추 → **Download ZIP** → 압축 풀기
- 또는 `git clone https://github.com/applesnack23/smart-manufacture.git`

## PC 준비 (PART 04)
```
cd C:\PART07
py -3.13 -m venv .venv
.venv\Scripts\activate
python -m pip install -r requirements.txt
```

## 라즈베리파이에서 실행
```
ssh username@192.168.7.1
cd projects/PART05
python3 p01_sensor_read.py
```

## 표로 실물 운전 (PART 07)
```
cd ~/projects/PART07
python3 ai_run_gpio.py sl_table.json
```
표 파일은 PC 에서 학습해 만든 것을 씁니다. 먼저 시험해 보려면 `PART07/예시표` 의 JSON 을 같은 폴더에 복사합니다.

## 실습 환경
- 라즈베리파이 제로 v1.3 · Python 3.13.5 · USB 가젯(192.168.7.1)
- 배선: 전선 번호 · 단자는 `PART03/전선목록.csv` 와 도면을 따름 (공통 GND N-3 = 라즈베리파이 9 번 핀 → L298N GND)
- 센서 A = GPIO17, 센서 B = GPIO27, 모터 IN1 = GPIO23, IN2 = GPIO24
- OpenPLC Runtime v3 (웹 `http://192.168.7.1:8080`, openplc / openplc)

라즈베리파이 배포 이미지(SD 카드 이미지)는 크기가 커서 이 저장소에 넣지 않고, 선생님이 따로 알려 주는 링크에서 받습니다.

## 그림 · 모델 출처
이 저장소의 부품 그림(`PART03/부품그림`)과 구매 부품 STEP(`PART02/STEP`)은 저자가 직접 그리고 만든 것입니다. 인터넷 사진이나 외부 CAD 모델은 넣지 않았습니다.
