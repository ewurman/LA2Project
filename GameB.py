'''
M = money I have (integer)
if M is div by 3 we toss coin 1;
else we toss coin 2

Coin1: I win 9/10 + e
Coin2: I win 1/4 + e

Winner wins 1 dollar from loser
'''
import random

class GameB:

	def __init__(self):
		self.epsilon = 0.05
		self.chance_one = 0.9
		self.chance_two = .25
		self.coin1_chance = 3

	def __init__(self, epsilon):
		self.epsilon = epsilon
		self.chance_one = 0.9
		self.chance_two = .25
		self.coin1_chance = 3

	def __init__(self, epsilon, chance1, chance2):
		self.epsilon = epsilon
		self.chance_one = chance1
		self.chance_two = chance2
		self.coin1_chance = 3

	def play_once(self, money):
		'''return True if I win'''
		x = random.random()
		if (money % self.coin1_chance == 0):
			#we flip coin 1
			if (self.chance_one + self.epsilon > x):
				return True
			else:
				return False
		else:
			#we flip #2
			if (self.chance_two + self.epsilon > x):
				return True
			else:
				return False


