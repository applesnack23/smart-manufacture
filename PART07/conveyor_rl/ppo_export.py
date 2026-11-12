# ppo_export.py — 학습한 PPO 를 12 가지 상태 표(JSON)로 바꾸기
import sys
import numpy as np
from stable_baselines3 import PPO
sys.path.append(".")
import ai_table

# [1] 학습한 모델 읽기
model = PPO.load("conveyor_rl/ppo_conveyor_20k", device="cpu")

# [2] 상태 하나에 행동 하나 (가장 좋은 것)
def predict(a, b, last):
    obs = np.array([a, b, last])
    action, _ = model.predict(obs, deterministic=True)
    return action

ai_table.save(predict, "conveyor_rl/ppo_table.json")   # [3] 저장
