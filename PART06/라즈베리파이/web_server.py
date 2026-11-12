# web_server.py — 가장 간단한 웹 서버
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import json, time

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):                        # 브라우저가 주소를 열면 실행
        print("요청 주소:", self.path)
        if self.path == "/":
            text = "메인 화면"
        elif self.path == "/status":
            d = {"time": time.strftime("%H:%M:%S"), "a": 1, "b": 0}
            text = json.dumps(d)             # 사전 -> JSON 글자
        else:
            text = "없는 주소: " + self.path
        body = text.encode()
        self.send_response(200)              # 상태 코드 200 = 잘 됐음
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.end_headers()                   # 머리말 끝
        self.wfile.write(body)               # 본문 보내기
    def log_message(self, *args):            # 접속 기록 줄 끄기
        pass

print("http://192.168.7.1:8000")
ThreadingHTTPServer(("", 8000), Handler).serve_forever()
