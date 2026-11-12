# b01_hello.py — 출력과 변수
name = "컨베이어"          # 문자열(str)
speed = 45                 # 정수(int), 모터 rpm
length = 0.13              # 실수(float), 롤러 중심거리 m
running = False            # 참/거짓(bool)

print("안녕하세요,", name)
print(f"모터 {speed} rpm, 길이 {length} m, 운전 중: {running}")
print(type(speed), type(length))
