'''
I Lose with 1/2 + e chance,
I win with 1/2 - e chance
Winner wins $1
'''
import random

class GameA:

	def __init__(self):
		self.epsilon = 0.05
		self.chance = 0.05

	def __init__(self, epsilon):
		self.epsilon = epsilon
		self.chance = 0.05

	def __init__(self, epsilon, chance):
		self.epsilon = epsilon
		self.chance = chance


	def play_once(self):
		'''return True if I win'''
		x = random.random()
		if (self.chance + self.epsilon > x):
			#we are in the 0-not us winning range
			return False
		else:
			return True

