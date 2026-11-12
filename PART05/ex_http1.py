from http.server import BaseHTTPRequestHandler, HTTPServer
import json
st = {"mode": "STOP", "count": 0}

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/status":            # 상태 → JSON
            body, code = json.dumps(st).encode(), 200
        elif self.path == "/start":           # 명령
            st["mode"] = "RIGHT"
            body, code = b"OK", 200
        else:                                 # 없는 경로
            body, code = b"Not Found", 404
        self.send_response(code)              # 상태 줄
        self.send_header("Content-Type", "application/json")
        self.end_headers()                    # 헤더 끝
        self.wfile.write(body)                # 본문

HTTPServer(("", 8000), Handler).serve_forever()
