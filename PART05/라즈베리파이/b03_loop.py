# b03_loop.py — 반복문: for 와 while
for i in range(3):              # 0, 1, 2
    print("왕복", i + 1, "회")

count = 0
while True:                     # 끝없이 반복 -> break 로 빠져나감
    count = count + 1
    print("검사", count)
    if count >= 5:
        break
print("끝")
