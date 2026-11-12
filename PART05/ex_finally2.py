class Motor:                      # PC 연습용 가짜 모터 (글자만 찍음)
    def forward(self): print("모터: 정방향")
    def stop(self): print("모터: 정지")
motor = Motor()

try:
    motor.forward()
    speed = int("빠르게")         # 같은 오류
    print("여기는 실행되지 않음")
finally:
    motor.stop()                 # 오류가 나도 반드시 실행
