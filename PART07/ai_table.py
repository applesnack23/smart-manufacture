# ai_table.py — 모델을 "12 가지 상태 -> 행동" 표(JSON)로 저장
import json
NAME = {0: "STOP", 1: "LEFT", 2: "RIGHT"}
STATES = [(a, b, last) for a in (0, 1) for b in (0, 1) for last in (0, 1, 2)]

def save(predict, path):
    table = {}
    for a, b, last in STATES:                       # 12 가지를 차례로 묻기
        table[f"{a},{b},{last}"] = int(predict(a, b, last))
    with open(path, "w") as f:
        json.dump(table, f, indent=1)
    for k, v in table.items():
        print(f"A,B,LAST = {k} -> {NAME[v]}")
    print("저장:", path)
