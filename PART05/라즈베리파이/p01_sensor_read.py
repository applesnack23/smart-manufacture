# p01_sensor_read.py — 센서 A · B 값 읽기 (Ctrl+C 로 끝)
from gpiozero import DigitalInputDevice
from time import sleep

# pull_up=True: 핀이 LOW(0 V)일 때 value = 1 -> TCRT5000 은 감지하면 D0 = LOW 이므로 1 = 감지
sensor_a = DigitalInputDevice(17, pull_up=True)   # 물리 11번 (SEN1)
sensor_b = DigitalInputDevice(27, pull_up=True)   # 물리 13번 (SEN2)

try:
    while True:
        print(f"센서A={sensor_a.value}  센서B={sensor_b.value}   (1 = 감지)")
        sleep(0.2)
except KeyboardInterrupt:
    print("끝")
