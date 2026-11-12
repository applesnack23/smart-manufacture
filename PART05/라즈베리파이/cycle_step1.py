# cycle_step1.py — 단계 1: 센서 값이 바뀔 때만 출력
from gpiozero import DigitalInputDevice
import time

sensor_a = DigitalInputDevice(17, pull_up=True)   # 물리 11번, 1 = 감지
sensor_b = DigitalInputDevice(27, pull_up=True)   # 물리 13번

last = None                                       # 직전 값 (처음에는 없음)
try:
    while True:
        now = (sensor_a.value, sensor_b.value)    # 두 값을 튜플로 묶음
        if now != last:                           # 바뀌었을 때만 출력
            print(time.strftime("%H:%M:%S"), "A =", now[0], " B =", now[1])
            last = now
        time.sleep(0.05)
except KeyboardInterrupt:
    print("끝")
