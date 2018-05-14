'''
M = money I have (integer)
if M is div by 3 we toss coin 1;
else we toss coin 2

Coin1: I win 9/10 + e
Coin2: I win 1/4 + e

Winner wins 1 dollar from loser
'''
import random
import numpy as np
import matplotlib.pyplot as plt

class GameB:

	def __init__(self, epsilon = 0.005, chance1 = 0.9, chance2 = 0.25):
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
		money_list = []
		counts = [0,0,0]

		while(i < turns):
			counts[money%3] += 1
			if self.play_once(money):
				money += 1
			else:
				money -= 1

			money_list.append(money)

			i += 1

		P_0 = counts[0]/turns
		P_1 = counts[1]/turns
		P_2 = counts[2]/turns


		print('P(0) =', P_0)
		print('P(1) =', P_1)
		print('P(2) =', P_2)
		print(P_0 + P_1 + P_2)


		return money, money_list


	def plot(self, turns, money, trials):
		'''plots the average return for the given number
		of turns and trials'''

		i = 0
		turns_list = np.linspace(0, turns, turns)
		list_sum = np.zeros(turns)
		while i < trials:
			money = money
			money2, money_list = self.play(turns, money)
			list_sum = np.add(list_sum, money_list)
			i += 1


		#print('Winning sums:', list_sum)
		ave_list = np.multiply((1/trials), list_sum)


		#print('Flips:', turns_list)
		#print('Average winnings:', ave_list)

		plt.plot(turns_list, ave_list)
		plt.xlabel('Coin Flips')
		plt.ylabel('Money')
		plt.title('Game B Average Winnings Over 1000 Trials')
		plt.show()




