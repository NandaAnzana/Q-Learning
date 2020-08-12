import gym
import numpy as np
import random

class Agent:

	def __init__(self, env):
		self.is_discrete = type(env.action_space) == gym.spaces.discrete.Discrete
		if self.is_discrete:
			self.action_size = env.action_space.n
		else:
			self.action_low = env.action_space.low
			self.action_high = env.action_space.high
			self.actino_shape = env.action_space.shape
			print("Action range: {} - {}".format(self.action_low,self.action_high))

	def get_action(self, state):
		if self.is_discrete:
			action = random.choice(range(self.action_size))
		else:
			action = np.random.uniform(self.action_low, self.action_high, self.action_size)
		return action


class QLearn(Agent):

	def __init__(self,env):
		super().__init__(env)
		self.state_size = env.observation_space.n
		self.epsilon = 0.1
		self.learning_rate = 0.1
		self.discount_rate = 0.97

	def model(self):
		self.q_table = np.zeros([self.state_size, self.action_size])

	def get_action(self, state):
		random_value = random.uniform(0, 1)
		if random_value < self.epsilon:
			return random.choice(range(self.action_size))
		else:
			q_state = self.q_table[state]
			return np.argmax(q_state)

	def get_action1(self, state):
		q_state = self.q_table[state]
		action_greedy = np.argmax(q_state)
		return action_greedy

	def train(self, observation):
		state, next_state, reward, action, done = observation
		q_value = self.q_table[state, action]
		q_next = self.q_table[next_state]
		target = reward + self.discount_rate * max(q_next)
		new_q = q_value + self.learning_rate * (target - q_value)
		self.q_table[state, action] = new_q