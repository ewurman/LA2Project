'''
I Lose with 1/2 + e chance,
I win with 1/2 - e chance
Winner wins $1
'''
import random

class GameA:

	def __init__(self, epsilon = 0.05, chance = 0.5):
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

	def play(self, turns, money):
		'''returns money after playing turns turns'''
		i = 0
		while(i < turns):
			if self.play_once():
				money += 1
			else:
				money -= 1
			i += 1
		return money



