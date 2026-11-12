# hmi_view.py — OpenPLC 의 센서 · 모터 상태를 웹으로 보기
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import json, socket, struct

PLC = ("127.0.0.1", 502)            # 같은 라즈베리파이의 OpenPLC (Modbus TCP)

def bits(fc, addr, n):
    """비트 n 개 읽기: fc 1 = 코일(%QX), 2 = 입력(%IX) -> [0, 1, ...]"""
    with socket.create_connection(PLC, timeout=1) as s:
        s.sendall(struct.pack(">HHHBBHH", 1, 0, 6, 1, fc, addr, n))
        data = s.recv(260)[9:]               # 앞 9 바이트(머리말) 뒤가 데이터
    return [(data[k // 8] >> (k % 8)) & 1 for k in range(n)]

def status():
    a, b = bits(1, 11, 2)                    # SENSOR_A · B = %QX1.3 · 1.4 = 코일 11 · 12
    right, left = bits(1, 2, 2)              # %QX0.2 · %QX0.3 = 코일 2 · 3
    return {"a": a, "b": b, "right": right, "left": left}

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            body = open("hmi_view.html", "rb").read()
        else:
            body = json.dumps(status()).encode()
        self.send_response(200)
        self.end_headers()
        self.wfile.write(body)
    def log_message(self, *args):
        pass

print("HMI: http://192.168.7.1:8000")
ThreadingHTTPServer(("", 8000), Handler).serve_forever()
