data = bytes([0b00001010])          # PLC 가 보낸 1 바이트 = 10
print(data[0], bin(data[0]))
for k in range(4):
    print(k, "번 비트:", (data[0] >> k) & 1)
