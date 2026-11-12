import json

s = {"a": 1, "b": 0, "right": 1, "left": 0}   # Python 사전
text = json.dumps(s)                            # 사전 -> 글자
print(type(s), s)
print(type(text), text)

back = json.loads(text)                         # 글자 -> 사전
print(back["right"] + 10)
print(json.dumps({"mode": "자동"}))
print(json.dumps({"mode": "자동"}, ensure_ascii=False))
