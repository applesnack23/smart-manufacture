class Motor:                      # PC 연습용 가짜 모터 (글자만 찍음)
    def forward(self): print("모터: 정방향")
    def stop(self): print("모터: 정지")
motor = Motor()

motor.forward()
speed = int("빠르게")             # 일부러 낸 오류 (ValueError)
motor.stop()                     # 이 줄까지 오지 못함
