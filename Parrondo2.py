from GameA import *
from GameB import *
import numpy as np

def alternate_games(money, turns):
	'''returns the money after playing the game turns times each'''
	ga = GameA()
	gb = GameB()
	money_list = []
	i = 0
	turns_2 = turns
	while i < turns_2:
		if ga.play_once():
			money += 1
		else:
			money -= 1
		money_list.append(money)
		i += 1
		if ga.play_once():
			money += 1
		else:
			money -= 1
		money_list.append(money)
		i += 1
		if gb.play_once(money):
			money += 1
		else:
			money -= 1
		money_list.append(money)
		i += 1
		if gb.play_once(money):
			money += 1
		else:
			money -= 1
		money_list.append(money)
		i += 1
	return money, money_list

def alternate_many_trials(money, turns, trials):
	'''averages trial number of alternating games '''
	i = 0
	orig_money = money
	turns_list = np.linspace(0, turns, turns)
	list_sum = np.zeros(turns)
	while i < trials:
		money = orig_money
		money2, money_list = alternate_games(money, turns)
		list_sum = np.add(list_sum, money_list)
		i += 1

	ave_list = np.multiply((1/trials), list_sum)
	plt.plot(turns_list, ave_list)
	plt.xlabel('Coin Flips')
	plt.ylabel('Money')
	plt.title('Game C Average Winnings Over 1000 Trials')
	plt.show()




def __main__():
	money = 100
	print("Sanity Check, Starting with $100")
	turns = 1000
	trials = 1000

	ga = GameA() #higher episolon to test losing game
	gb = GameB()

	money, x = ga.play(turns, money)
	print("Played GameA {0} times, money at {1}. resetting money to $100".format(turns, money))
	money = 100
	money, x = gb.play(turns, money)
	print("Played GameB {0} times, money at {1}. resetting money to $100".format(turns, money))
	money = 100

	print("Alternating games for {0} turns each:".format(turns))
	money, x = alternate_games(money, turns)

	print("Final: ${0}".format(money))
	money = 100
	#gb.plot(turns, money, trials)

	alternate_many_trials(money, turns, trials)


__main__()
