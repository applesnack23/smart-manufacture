# b02_if.py — 조건문: 센서 값에 따라 할 일 고르기
sensor_a = 1   # 1 = 감지, 0 = 없음 (나중에 실제 센서 값으로 바뀜)
sensor_b = 0

if sensor_a == 1 and sensor_b == 1:
    print("둘 다 감지 -> 정지")
elif sensor_a == 1:
    print("센서 A 감지 -> 정방향")
elif sensor_b == 1:
    print("센서 B 감지 -> 역방향")
else:
    print("감지 없음 -> 정지")
