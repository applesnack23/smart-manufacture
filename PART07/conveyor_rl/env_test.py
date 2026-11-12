# env_test.py — 환경 시험: 정해 둔 운전으로 한 판 해 보고 점수 보기
#   python conveyor_rl/env_test.py right     (right · stop · rule)
import sys
from conveyor_env import ConveyorEnv

mode = sys.argv[1]
env = ConveyorEnv()
obs, _ = env.reset()
total, n = 0, 0
while True:
    if mode == "right": act = 2                    # 늘 RIGHT
    elif mode == "stop": act = 0                   # 늘 STOP
    else: act = 1 if obs[2] == 2 else 2            # 규칙: 마지막이 B 면 LEFT
    obs, r, done, cut, _ = env.step(act)
    total, n = total + r, n + 1
    if r not in (0, -0.01, -0.06):                 # 특별한 보상만 출력
        print(n, "걸음", obs, "보상", r)
    if done or cut:
        break
print("걸음", n, "점수 합계", round(total, 2), "끝" if done else "시간 초과")
