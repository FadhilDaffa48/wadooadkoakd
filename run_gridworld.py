import gymnasium as gym
import gymnasium_env

env = gym.make("gymnasium_env/GridWorld-v0", render_mode="human")

observation, info = env.reset(seed=42)

terminated = False
truncated = False

while not (terminated or truncated):
    action = env.action_space.sample()
    observation, reward, terminated, truncated, info = env.step(action)

env.close()