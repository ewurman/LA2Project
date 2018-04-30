from GameA import *
from GameB import *
import numpy as np

def alternate_games(money, turns):
	'''returns the money after playing the game turns times each'''
	ga = GameA()
	gb = GameB()

	i = 0
	while i < turns:
		i += 1
		if ga.play_once():
			money += 1
		else:
			money -= 1
		if gb.play_once(money):
			money += 1
		else: 
			money -= 1
	return money



def __main__():
	money = 100
	print("Sanity Check, Starting with $100")
	turns = 1000

	ga = GameA() #higher episolon to test losing game
	gb = GameB()

	money = ga.play(turns, money)
	print("Played GameA {0} times, money at {1}. resetting money to $100".format(turns, money))
	money = 100
	money = gb.play(turns, money)
	print("Played GameB {0} times, money at {1}. resetting money to $100".format(turns, money))
	money = 100

	print("Alternating games for {0} turns each:".format(turns))
	money = alternate_games(money, 100)

	print("Final: ${0}".format(money))



__main__()