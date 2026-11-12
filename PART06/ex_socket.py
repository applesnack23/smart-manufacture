import socket

# web_server.py 가 켜져 있어야 합니다 (다른 터미널에서 실행)
with socket.create_connection(("127.0.0.1", 8000), timeout=1) as s:
    s.sendall(b"GET /status HTTP/1.0\r\n\r\n")   # 브라우저가 보내는 글자
    answer = b""
    while True:
        part = s.recv(1000)                       # 최대 1000 바이트 받기
        if not part:                              # 빈 바이트 = 상대가 끊음
            break
        answer = answer + part
print(answer.decode())
