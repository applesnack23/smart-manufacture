# hmi_plc.py — 상태 보기 + AUTO / MANUAL · 수동 운전 · 알람 리셋
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import json, socket, struct, time

PLC = ("127.0.0.1", 502)            # 같은 라즈베리파이의 OpenPLC (Modbus TCP)

def modbus(fc, addr, value):
    """Modbus 요청 하나: fc 1 = 코일 읽기, 2 = 입력 읽기, 5 = 코일 쓰기"""
    with socket.create_connection(PLC, timeout=1) as s:
        s.sendall(struct.pack(">HHHBBHH", 1, 0, 6, 1, fc, addr, value))
        return s.recv(260)[9:]

def bits(fc, addr, n):
    data = modbus(fc, addr, n)
    return [(data[k // 8] >> (k % 8)) & 1 for k in range(n)]

def status():
    a, b = bits(1, 11, 2)                    # SENSOR_A · B = %QX1.3 · 1.4 = 코일 11 · 12
    right, left = bits(1, 2, 2)              # %QX0.2 · %QX0.3 = 코일 2 · 3
    auto, alarm = bits(1, 24, 2)             # %QX3.0 · %QX3.1 = 코일 24 · 25
    return {"a": a, "b": b, "right": right, "left": left,
            "auto": auto, "alarm": alarm}

BUTTON = {"/auto": 16, "/manual": 17,        # %QX2.0 ~ %QX2.5 = 코일 16 ~ 21
          "/fwd": 18, "/rev": 19, "/stop": 20, "/arst": 21}

def press(coil):                             # 누름 버튼 = 0.3 초 동안만 1
    try:
        modbus(5, coil, 0xFF00)              # 0xFF00 = 1 쓰기
        time.sleep(0.3)
    finally:
        modbus(5, coil, 0)                   # 무슨 일이 있어도 0 으로 되돌림

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path in BUTTON:              # 버튼 주소면 먼저 누르고
            press(BUTTON[self.path])
        if self.path == "/":
            body = open("hmi_plc.html", "rb").read()
        else:
            body = json.dumps(status()).encode()
        self.send_response(200)
        self.end_headers()
        self.wfile.write(body)
    def log_message(self, *args):
        pass

print("HMI: http://192.168.7.1:8000")
ThreadingHTTPServer(("", 8000), Handler).serve_forever()
