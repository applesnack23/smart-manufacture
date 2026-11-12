# b07_file.py — 파일에 기록하기 (나중에 설비 데이터를 CSV 로 남길 때 사용)
import time

with open("log.csv", "w", encoding="utf-8") as f:   # with: 끝나면 파일이 자동으로 닫힘
    f.write("time,sensor_a,sensor_b\n")
    for i in range(3):
        f.write(f"{time.strftime('%H:%M:%S')},{i % 2},0\n")

with open("log.csv", encoding="utf-8") as f:
    print(f.read())
