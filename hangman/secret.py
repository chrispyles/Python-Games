###############################
##### Hangman Secret Word #####
#####   by Chris Pyles    #####
###############################

from utils import *
from player import *
from board import *

class SecretWord:
	"""
	Secret word class for Hangman, to hold the secret word created by
	Player 1.
	"""
	def __init__(self, word):
		self._secret = word
		self._len = len(self._secret)
		self._guessed = repeat(False, self._len)

	
	def __repr__(self):
		result = ""
		for idx in range(self._len):
			if self._guessed[idx]:
				result += self._secret[idx]
			else:
				result += "_"
		return result

	def __len__(self):
		return self._len

	def guess(self, letter):
		occurances, idx = 0, 0
		for l in self._secret:
			if l == letter:
				occurances += 1
				self._guessed[idx] = True
			idx += 1
		if occurances > 0:
			return True, occurances
		else:
			return False, 0

	def num_guessed(self):
		return sum(self._guessed)

	def is_finished(self):
		return self.num_guessed() == len(self)