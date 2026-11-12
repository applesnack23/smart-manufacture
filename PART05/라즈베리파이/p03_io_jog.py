# p03_io_jog.py — 입력으로 출력 바꾸기: 센서 A -> 정방향, 센서 B -> 역방향, 그 밖에는 정지
from gpiozero import DigitalInputDevice, Motor
from time import sleep

sensor_a = DigitalInputDevice(17, pull_up=True)
sensor_b = DigitalInputDevice(27, pull_up=True)
motor = Motor(forward=23, backward=24, pwm=False)

def decide(a, b):                 # 2) 의 예제 34 와 같은 함수
    if a and b:
        return "정지"
    if a:
        return "정방향"
    if b:
        return "역방향"
    return "정지"

last = ""
try:
    while True:
        act = decide(sensor_a.value, sensor_b.value)   # (1) 읽기 -> (2) 판단
        if act == "정방향":                            # (3) 쓰기
            motor.forward()
        elif act == "역방향":
            motor.backward()
        else:
            motor.stop()
        if act != last:                                # 바뀔 때만 화면에 표시
            print(act)
            last = act
        sleep(0.05)
except KeyboardInterrupt:
    pass
finally:
    motor.stop()
    print("끝")
