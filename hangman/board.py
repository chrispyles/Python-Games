##########################
##### Hangman Board  #####
##### by Chris Pyles #####
##########################

# WHICH LETTERS HAVE BEEN GUESSED????????????????

from secret import *
from player import *
from utils import *

class Board:
	"""
	Board class for Hangman
	"""
	def __init__(self, secret, players):
		self._secret = secret
		self._players = players
		self._board = 0
		self._guessed_letters = []

	def __repr__(self):
		return "<Board: {} length secret, {} guessed>".format(
				len(self._secret),
				self._secret.num_guessed()
			)

	def guess(self, player, letter):
		if letter not in self._guessed_letters:
			self._guessed_letters += [letter]
			if not player.guess(self._secret, letter):
				self._board += 1
		else:
			self._guessed_letters += [letter]
			print("'{}' has already been guessed".format(letter))
			
	def board(self):
		bd = boards[self._board] + "\nWord: "
		bd += (self._secret.__repr__() + "\nGuessed: ")
		bd += " ".join(self._guessed_letters)
		return bd

	def board_number(self):
		return self._board

	def is_completed(self):
		return self.board_number() == 6 or self._secret.is_finished()

	def ending(self):
		if self.board_number() == 6:
			print("\n\nHanged.\nFinal Scores:")
		else:
			print("\n\nCongratulations! You guessed the secret word:\n{}\nFinal Scores:".format(
					self._secret.__repr__()
				))
		for p in self._players:
			print("{} (Player {}): {}".format(
					p._name,
					p._id,
					p._score
				))






















if __name__ == "__main__":
	import doctest
	doctest.testmod()