import struct

b = struct.pack(">H", 502)          # 숫자 502 -> 2 바이트
print(b, list(b), b.hex(" "))

q = struct.pack(">HHHBBHH", 1, 0, 6, 1, 2, 3, 2)
print(len(q), "바이트:", q.hex(" "))
print(struct.unpack(">HHHBBHH", q))  # 바이트 -> 숫자들
