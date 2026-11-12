# ppo_train.py — 강화학습: PPO 로 20000 걸음 연습 (약 35 분)
from stable_baselines3 import PPO
from conveyor_env import ConveyorEnv

env = ConveyorEnv()                               # [1] 환경
model = PPO("MlpPolicy", env,                     # [2] 에이전트
            n_steps=256, batch_size=64, gamma=0.99,
            learning_rate=0.0003, verbose=1,
            tensorboard_log="conveyor_rl/logs")
model.learn(total_timesteps=20000)                # [3] 연습
model.save("conveyor_rl/ppo_conveyor_20k")        # [4] 저장 (.zip)
env.close()
