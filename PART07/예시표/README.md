# 예시표 — PART 07 예시 학습 결과 (PC 에서 만든 표)

| 파일 | 만든 방법 |
|---|---|
| `sl_table.json` | 지도학습 (`sl_train.py`) |
| `il_clean_table.json` | 모방학습 (`il_train.py`, STOP · 사라짐 줄을 지운 뒤) |
| `ppo_table.json` | 강화학습 (`ppo_train.py` → `ppo_export.py`) |

표의 키는 `"A,B,LAST"` 이고, 값은 0 = STOP, 1 = LEFT, 2 = RIGHT 입니다.

## 라즈베리파이에서 바로 시험하기
1. 이 파일들을 `\\192.168.7.1\projects\PART07` 에 복사합니다 (`ai_run_gpio.py` 가 있는 폴더).
2. 라즈베리파이에서 실행합니다.
```
cd ~/projects/PART07
python3 ai_run_gpio.py sl_table.json
```

수업에서는 학생이 직접 학습해서 만든 표를 씁니다. 이 표는 결과를 비교하거나 실물 동작을 먼저 확인할 때 씁니다.
