# smart-manufacture — 컨베이어 한 대로 배우는 Physical AI 실습 자료

「스마트제조 · 산업자동화 — 컨베이어 한 대로 배우는 Physical AI」 교재의 예제 · 데이터 · 완성 소스 코드입니다.
폴더는 교재의 PART 별로 나뉘어 있고, 각 폴더 안의 `라즈베리파이` 폴더는 라즈베리파이에서 실행하는 파일입니다.

| 폴더 | 교재 | 내용 |
|---|---|---|
| `PART04` | PART 04 실습 환경 | AI 패키지 목록 `requirements.txt` (가상환경에 설치) |
| `PART05` | PART 05 Python | PC 연습(`ex_*.py`, `web/panel.html`, `연습/`) |
| `PART05/라즈베리파이` | PART 05 | 센서 · 모터 · 사이클 제어(`p01 ~ p04`, `cycle_step*`, `RaspberryPi_cycle.py`, `cycle_ui.html`) |
| `PART06` | PART 06 OpenPLC | 래더 · ST 프로그램(`.st`, OpenPLC Editor 에서 열기), HMI 준비 연습(`ex_*.py`) |
| `PART06/라즈베리파이` | PART 06 | 웹 · HMI(`web_server.py`, `hmi_view`, `hmi_plc`) |
| `PART07` | PART 07 Physical AI | 디지털 트윈 · 지도 · 모방 · 강화학습(`twin_sim.py`, `conveyor_sl · il · rl`) |
| `PART07/라즈베리파이` | PART 07 | 학습한 표로 실물 운전(`ai_run_gpio.py 표파일.json`) |

## 어디로 복사하나
- **라즈베리파이:** `PART05` · `PART06` · `PART07` 의 `라즈베리파이` 폴더 안 파일을 모두 `\\192.168.7.1\projects\p3` 에 복사합니다(라즈베리파이의 `~/projects/p3`).
- **PC — PART 05 · 06 연습:** `PART05`, `PART06` 의 PC 파일을 `C:\py_practice` 에 복사합니다.
- **PC — PART 07:** `PART07` 의 PC 파일(라즈베리파이 폴더 빼고)을 `C:\AI_Training` 에 복사합니다.

## 받기
- 초록색 **Code** 단추 → **Download ZIP** → 압축 풀기
- 또는 `git clone https://github.com/applesnack23/smart-manufacture.git`

## PC 준비 (PART 04)
```
cd C:\AI_Training
py -3.13 -m venv .venv
.venv\Scripts\activate
python -m pip install -r requirements.txt
```

## 실습 환경
- 라즈베리파이 제로 v1.3 · Python 3.13.5 · USB 가젯(192.168.7.1)
- 센서 A = GPIO17, 센서 B = GPIO27, 모터 IN1 = GPIO23, IN2 = GPIO24
- OpenPLC Runtime v3 (웹 `http://192.168.7.1:8080`, openplc / openplc)

라즈베리파이 배포 이미지(SD 카드 이미지)는 크기가 커서 이 저장소에 넣지 않고, 선생님이 따로 알려 주는 링크에서 받습니다.
