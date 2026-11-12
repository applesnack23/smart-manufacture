# p04_io_check.py — 입출력 점검: 번호를 골라 하나씩 확인
from gpiozero import DigitalInputDevice, Motor
from time import sleep

sensor_a = DigitalInputDevice(17, pull_up=True)
sensor_b = DigitalInputDevice(27, pull_up=True)
motor = Motor(forward=23, backward=24, pwm=False)

try:
    while True:
        sel = input("1 센서 보기  2 정방향  3 역방향  q 끝 > ")
        if sel == "1":
            for i in range(20):                    # 0.2 초마다 20 번 = 4 초
                print("A =", sensor_a.value, " B =", sensor_b.value)
                sleep(0.2)
        elif sel == "2":
            motor.forward()
            sleep(2)
            motor.stop()
        elif sel == "3":
            motor.backward()
            sleep(2)
            motor.stop()
        elif sel == "q":
            break
finally:
    motor.stop()
