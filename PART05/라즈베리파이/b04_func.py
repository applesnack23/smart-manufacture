# b04_func.py — 함수: 자주 쓰는 일을 이름 붙여 묶기
def decide(a, b):
    """센서 A, B 값(1 = 감지)을 받아 모터 동작을 돌려줌"""
    if a and b:
        return "정지"
    if a:
        return "정방향"
    if b:
        return "역방향"
    return "정지"

print(decide(1, 0))   # 정방향
print(decide(0, 1))   # 역방향
print(decide(1, 1))   # 정지
