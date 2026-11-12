# ai_run_gpio.py — PC 에서 만든 표(JSON)로 실제 컨베이어 운전
#   python3 ai_run_gpio.py sl_table.json
from gpiozero import DigitalInputDevice, Motor
import json, sys, time

# [1] 핀 준비 (PART 05 와 같음)
sensor_a = DigitalInputDevice(17, pull_up=True)      # 1 = 감지
sensor_b = DigitalInputDevice(27, pull_up=True)
motor = Motor(forward=23, backward=24, pwm=False)    # RIGHT = forward
NAME = {0: "STOP", 1: "LEFT", 2: "RIGHT"}
if len(sys.argv) < 2:                                # 표 파일을 안 적었을 때
    print("사용법: python3 ai_run_gpio.py 표파일.json  (예: sl_table.json)")
    sys.exit()
table = json.load(open(sys.argv[1]))
last, old, seen = 0, None, time.time()
try:
    while True:
        # [2] (1) 읽기 · 8 초 동안 못 보면 정지
        a, b = sensor_a.value, sensor_b.value
        if a: last = 1
        elif b: last = 2
        if a or b: seen = time.time()
        if time.time() - seen > 8:
            print("박스가 사라졌습니다 -> 정지")
            break
        # [3] (2) 판단 = 표 보기
        act = table[f"{a},{b},{last}"]
        # [4] (3) 쓰기
        if act == 2: motor.forward()
        elif act == 1: motor.backward()
        else: motor.stop()
        if act != old:
            msg = f"A={a} B={b} LAST={last} -> {NAME[act]}"
            print(time.strftime("%H:%M:%S"), msg)
            old = act
        time.sleep(0.05)
except KeyboardInterrupt:
    pass
finally:
    motor.stop()
