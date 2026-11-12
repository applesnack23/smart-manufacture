# RaspberryPi_cycle.py — 왕복 사이클 + 웹 운전 화면 (브라우저 http://192.168.7.1:8000)
from gpiozero import DigitalInputDevice, Motor
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import json, threading, time

sensor_a = DigitalInputDevice(17, pull_up=True)    # 1 = 감지
sensor_b = DigitalInputDevice(27, pull_up=True)
motor = Motor(forward=23, backward=24, pwm=False)
st = {"mode": "STOP", "a": 0, "b": 0, "count": 0}  # 설비 상태 (웹 화면으로 보냄)

def step():                                        # (2) 판단
    if st["mode"] == "RIGHT" and st["b"]:
        st["mode"] = "LEFT"
    elif st["mode"] == "LEFT" and st["a"]:
        st["mode"] = "RIGHT"
        st["count"] += 1                           # A 로 돌아오면 왕복 1 회

class Handler(BaseHTTPRequestHandler):             # 브라우저의 요청에 답함
    def do_GET(self):
        if self.path == "/start" and st["mode"] == "STOP":
            st["mode"] = "RIGHT" if st["a"] else "LEFT"
        elif self.path == "/stop":
            st["mode"] = "STOP"
        if self.path == "/":                       # 화면 파일
            body = open("cycle_ui.html", "rb").read()
        else:                                      # 그 밖에는 상태(JSON)
            body = json.dumps(st).encode()
        self.send_response(200)
        self.end_headers()
        self.wfile.write(body)
    def log_message(self, *args):                  # 접속 기록은 화면에 찍지 않음
        pass

server = ThreadingHTTPServer(("", 8000), Handler)
threading.Thread(target=server.serve_forever, daemon=True).start()
print("웹 운전 화면: http://192.168.7.1:8000")
try:
    while True:
        st["a"], st["b"] = sensor_a.value, sensor_b.value   # (1) 읽기
        step()
        if st["mode"] == "RIGHT":                           # (3) 쓰기
            motor.forward()
        elif st["mode"] == "LEFT":
            motor.backward()
        else:
            motor.stop()
        time.sleep(0.05)
except KeyboardInterrupt:
    print("끝")
finally:
    motor.stop()
