# b05_list_dict.py — 리스트와 딕셔너리: 여러 값을 한꺼번에
pins = [17, 27, 23, 24]                    # 리스트: 순서가 있는 값 묶음
print(pins[0], len(pins))                  # 17 4

io = {"SEN1": 17, "SEN2": 27, "IN1": 23, "IN2": 24}   # 딕셔너리: 이름 -> 값
print(io["IN1"])                           # 23
for key, pin in io.items():
    print(f"{key:5s} -> GPIO{pin}")
