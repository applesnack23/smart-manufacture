import time
class Motor:                      # PC 연습용 가짜 모터 (글자만 찍음)
    def forward(self): print("모터: 정방향")
    def stop(self): print("모터: 정지")
motor = Motor()

try:
    motor.forward()
    for i in range(3):
        print("도는 중", i)
        time.sleep(0.1)
    raise KeyboardInterrupt      # 사람이 Ctrl + C 를 누른 것처럼
except KeyboardInterrupt:
    print("Ctrl + C — 사용자가 멈춤")
finally:
    motor.stop()
