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

	def __init__(self, epsilon = 0.05, chance1 = 0.9, chance2 = 0.25):
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

	def play(self, turns, money):
		'''returns money after playing turns turns'''
		i = 0
		while(i < turns):
			if self.play_once(money):
				money += 1
			else:
				money -= 1
			i += 1
		return money


