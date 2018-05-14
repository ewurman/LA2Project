'''
I Lose with 1/2 - e chance,
I win with 1/2 + e chance
Winner wins $1
'''
import random
import numpy as np
import matplotlib.pyplot as plt

class GameA:

	def __init__(self, epsilon = 0.005, chance = 0.5):
		self.epsilon = epsilon
		self.chance = chance


	def play_once(self):
		'''return True if I win'''
		x = random.random()
		if (self.chance + self.epsilon > x):
			#we are in the 0-not us winning range
			return True
		else:
			return False

                

	def play(self, turns, money):
		'''returns money after playing turns turns'''
		i = 0
		money_list = []
		while(i < turns):
			if self.play_once():
				money += 1
			else:
				money -= 1
			money_list.append(money)

			
			i += 1
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
		plt.title('Game A Average Winnings Over 1000 Trials')
		plt.show()
                
                

        

        
                        
                

                



