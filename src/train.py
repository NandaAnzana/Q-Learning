from .agent import QLearn
import gym
import numpy as np

def train_taxi():
    print("Your training begin...")
    env = gym.make('Taxi-v3')
    agent = QLearn(env)
    agent.model()
    for _ in range(100000):
        state = env.reset()
        done = False
        while not done:
            action = agent.get_action(state)
            next_state, reward, done, _ = env.step(action)
            agent.train((state, next_state, reward, action, done))
            state = next_state
    
    with open('model.npy', 'wb') as f:
        np.save(f, agent.q_table)
    print("Your training is done...")