# rule_run.py — 규칙 기반 프로그램으로 디지털 트윈 운전
import time
import twin

twin.reset()
act, old = 2, None
try:
    while True:
        a, b, lost = twin.read()              # (1) 읽기
        if a:                                 # (2) 판단 = 사람이 쓴 규칙
            act = 2
        elif b:
            act = 1
        twin.write(act)                       # (3) 쓰기
        if (a, b, lost) != old:               # 센서가 바뀔 때만 출력
            t = time.strftime("%H:%M:%S")
            print(t, f"A={a} B={b} 사라짐={lost} -> 행동 {act}")
            old = (a, b, lost)
        time.sleep(0.05)
except KeyboardInterrupt:                     # Ctrl+C -> 벨트 정지
    twin.write(0)
