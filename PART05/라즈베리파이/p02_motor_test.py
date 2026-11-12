# p02_motor_test.py — 모터 출력 테스트: 정방향 2초 -> 정지 1초 -> 역방향 2초 -> 정지
from gpiozero import Motor
from time import sleep

# IN1 = GPIO23(물리 16번), IN2 = GPIO24(물리 18번), ENA 는 점퍼(최고 속도) -> pwm=False
motor = Motor(forward=23, backward=24, pwm=False)

try:
    print("정방향 2초")
    motor.forward()
    sleep(2)
    print("정지 1초")
    motor.stop()
    sleep(1)
    print("역방향 2초")
    motor.backward()
    sleep(2)
finally:
    motor.stop()        # 어떤 경우에도 정지하고 끝냄
    print("끝")
