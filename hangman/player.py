###########################
##### Hangman Players #####
##### by Chris Pyles  #####
###########################

from utils import *
from secret import *
from player import *

class Player:
	def __init__(self, name, number):
		self._score = 0
		self._name = name
		self._id = number

	def guess(self, secret, letter):
		in_word, occurances = secret.guess(letter)
		if in_word:
			self._score += 100 * occurances
			print("'{}' occurred {} times! Your score is now {}.".format(
					letter,
					occurances,
					self._score
				))
			return True
		else:
			print("'{}' did not occur :(. Your score is now {}.".format(
					letter,
					self._score
				))
			return False




























if __name__ == "__main__":
	import doctest
	doctest.testmod()