import json
st = {"mode": "RIGHT", "a": 1, "b": 0, "run": True, "err": None}
text = json.dumps(st)                    # 사전 → JSON 글자
print(text)
print(type(text))
back = json.loads('{"mode": "STOP", "count": 3}')   # 글자 → 사전
print(back["mode"], back["count"] + 1)
