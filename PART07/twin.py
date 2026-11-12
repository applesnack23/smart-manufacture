# twin.py — 디지털 트윈(twin_sim.py)과 Modbus 로 주고받기
import asyncio, threading, time
import modbus_server as mb

# [1] Modbus 서버를 뒤에서 따로 돌리기
loop = asyncio.new_event_loop()

def _serve():
    asyncio.set_event_loop(loop)
    loop.run_until_complete(mb.start_server())

threading.Thread(target=_serve, daemon=True).start()
time.sleep(1)
print("Modbus 서버 127.0.0.1:1502 — twin_sim.py 를 실행하세요")

def _do(job):                          # 서버 쪽에 일을 맡기고 결과 받기
    return asyncio.run_coroutine_threadsafe(job, loop).result(timeout=5)

# [2] 읽기: HR0 -> (센서 A, 센서 B, 사라짐)
def read():
    v = _do(mb.read_hr(0))
    return v & 1, (v >> 1) & 1, (v >> 2) & 1

# [3] 쓰기: HR10 <- 0 STOP · 1 LEFT · 2 RIGHT · 4 RESET
def write(cmd):
    _do(mb.write_hr(10, cmd))

# [4] 리셋: 박스를 센서 A 자리로
def reset():
    write(0); time.sleep(0.05)
    write(4); time.sleep(0.1)
    write(0); time.sleep(0.3)

# [5] 혼자 실행하면: 서버만 켜 두기 (twin_sim.py 화면 시험용)
if __name__ == "__main__":
    try:
        while True: time.sleep(1)
    except KeyboardInterrupt:
        print("끝")
