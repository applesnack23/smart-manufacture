# conveyor_env.py — 디지털 트윈을 강화학습 환경으로 감싸기
import sys, time
import numpy as np
import gymnasium as gym
sys.path.append(".")
import twin

TRIPS = 3                       # 왕복 몇 번이면 성공 (0 = 끝없이 왕복)

class ConveyorEnv(gym.Env):
    # [1] 행동 0 STOP · 1 LEFT · 2 RIGHT, 상태 [A, B, LAST]
    action_space = gym.spaces.Discrete(3)
    observation_space = gym.spaces.MultiDiscrete([2, 2, 3])

    def reset(self, seed=None, options=None):          # [2] 판 시작
        twin.reset()
        a, b, _ = twin.read()
        self.last, self.steps, self.trips = 1, 0, 0
        return np.array([a, b, self.last]), {}

    def step(self, action):                            # [3] 한 걸음
        twin.write(int(action))
        time.sleep(0.1)
        a, b, lost = twin.read()
        self.steps += 1
        r = -0.06 if action == 0 else -0.01            # [4] 보상
        if (b and self.last == 1) or (a and self.last == 2):
            r = 1.0                                    # 반대편 도착
            if a: self.trips += 1                      # A 도착 = 왕복 1 번
        self.last = 1 if a else (2 if b else self.last)
        done = bool(lost) or (TRIPS > 0 and self.trips >= TRIPS)   # [5] 끝
        if done: r = -10.0 if lost else 10.0           # 떨어뜨림 · 성공
        cut = self.steps >= 500 and not done           # 시간 초과
        if cut and TRIPS > 0: r = -5.0
        if done or cut: twin.write(0)
        return np.array([a, b, self.last]), r, done, cut, {}
