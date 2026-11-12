# ai_run.py — 표(JSON)로 디지털 트윈 운전
#   python ai_run.py conveyor_sl/sl_table.json
import json, sys, time
import twin

NAME = {0: "STOP", 1: "LEFT", 2: "RIGHT"}
table = json.load(open(sys.argv[1]))          # [1] 표 읽기
twin.reset()
last, old = 0, None
try:
    while True:
        a, b, lost = twin.read()              # [2] (1) 읽기
        if lost:                              #     박스가 떨어지면 리셋
            print("박스 사라짐 -> 리셋")
            twin.reset(); last = 0
            continue
        if a: last = 1                        #     마지막으로 본 센서
        elif b: last = 2
        act = table[f"{a},{b},{last}"]        # [3] (2) 판단 = 표 보기
        twin.write(act)                       # [4] (3) 쓰기
        if act != old:
            msg = f"A={a} B={b} LAST={last} -> {NAME[act]}"
            print(time.strftime("%H:%M:%S"), msg)
            old = act
        time.sleep(0.05)
except KeyboardInterrupt:
    twin.write(0)
