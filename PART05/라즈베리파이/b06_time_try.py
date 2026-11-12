# b06_time_try.py — 모듈 가져오기, 기다리기, 안전하게 끝내기
import time                      # 표준 모듈 time 가져오기

try:
    for sec in range(1, 11):
        print(sec, "초")
        time.sleep(1)            # 1초 기다림
except KeyboardInterrupt:        # Ctrl+C 를 누르면 여기로
    print("사용자가 멈춤")
finally:                         # 어떻게 끝나든 마지막에 반드시 실행
    print("정리: 모터 정지")
