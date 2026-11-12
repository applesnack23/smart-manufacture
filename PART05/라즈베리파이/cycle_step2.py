# cycle_step2.py — 단계 2: 끝에 닿으면 방향을 바꿔 A <-> B 왕복
from gpiozero import DigitalInputDevice, Motor
import time

sensor_a = DigitalInputDevice(17, pull_up=True)    # 1 = 감지
sensor_b = DigitalInputDevice(27, pull_up=True)
motor = Motor(forward=23, backward=24, pwm=False)  # forward = A 에서 B 쪽

mode = "RIGHT" if sensor_a.value else "LEFT"       # 박스가 A 에 있으면 B 쪽으로 출발
print("출발:", mode)
try:
    while True:
        a, b = sensor_a.value, sensor_b.value      # (1) 읽기
        if mode == "RIGHT" and b:                  # (2) 판단
            mode = "LEFT"
            print(time.strftime("%H:%M:%S"), "B 도착 -> LEFT")
        elif mode == "LEFT" and a:
            mode = "RIGHT"
            print(time.strftime("%H:%M:%S"), "A 도착 -> RIGHT")
        if mode == "RIGHT":                        # (3) 쓰기
            motor.forward()
        else:
            motor.backward()
        time.sleep(0.05)
except KeyboardInterrupt:
    print("끝")
finally:
    motor.stop()                                   # 어떻게 끝나든 모터 정지
