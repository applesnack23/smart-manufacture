# il_collect.py — 모방학습 1단계: 키보드 운전 기록을 그대로 모으기
# D = RIGHT · A = LEFT · S = STOP · R = 리셋 · Q = 저장하고 끝
import msvcrt, sys, time
import pandas as pd
sys.path.append(".")
import twin

KEY = {"d": 2, "a": 1, "s": 0}
rows, act, last = [], 0, 0                  # 처음 행동은 STOP
twin.reset()
print("D = RIGHT · A = LEFT · S = STOP · R = 리셋 · Q = 저장")
while True:
    # [1] 키 읽기 (Enter 없이)
    if msvcrt.kbhit():
        k = msvcrt.getwch().lower()
        if k == "q":
            break
        if k == "r":                        # 박스를 처음 자리로
            twin.reset(); act, last = 0, 0
        act = KEY.get(k, act)
    # [2] 센서 읽고 명령 보내기
    a, b, lost = twin.read()
    if a: last = 1
    elif b: last = 2
    twin.write(act)
    # [3] 한 줄 기록 (모두)
    rows.append([a, b, last, lost, act])
    time.sleep(0.05)

# [4] CSV 로 저장
twin.write(0)
cols = ["Sensor01", "Sensor02", "LastSensor", "Lost", "Action"]
df = pd.DataFrame(rows, columns=cols)
df.to_csv("conveyor_il/il_dataset.csv", index=False)
print(len(df), "줄 저장 -> conveyor_il/il_dataset.csv")
