###############################
##### Hangman Game Runner #####
#####   by Chris Pyles    #####
###############################

from board import *
from secret import *
from player import *
from utils import *
import re

class Game:
	"""
	Runs a game of hangman.
	"""
	def __init__(self):
		print("\n\nWelcome to Hangman.\nSecret Keeper, step up to the computer.")
		print("\nAre you the Secret Keeper?")
		secret_keeper = input()
		if re.match(r"[Yy][Ee]?[Ss]?", secret_keeper):
			self.enter_secret()
		else:
			print("\nSorry, you're not the Secret Keeper. Go away.")
			Game()

	def enter_secret(self):
		print("\n\nSecret Keeper, enter your secret word.")
		word = input()
		self._secret = SecretWord(word)
		self.create_players()

	def create_players(self):
		self._players = []
		more_players, i = True, 0
		while more_players:
			print("\n\nEnter Player {}'s Name:".format(i))
			name = input()
			self._players += [Player(name, i)]
			i += 1
			print("\nMore players?")
			more_players_question = input()
			if re.match(r"[Yy][Ee]?[Ss]?", more_players_question):
				continue
			else:
				break
		self.init_board()

	def init_board(self):
		self._board = Board(self._secret, self._players)
		self.run_game()

	def run_game(self):
		i = 0
		while not self._board.is_completed():
			print("\n\nHere is the current state of the board:")
			print(self._board.board())

			print("\nIt is {}'s turn.".format(self._players[i]._name))
			print("Enter your guess below.")
			guess = input()

			try:
				assert len(guess) == 1, "Guess must be length 1"
			except AssertionError:
				print("\nYour guess must have length 1.")
				continue

			self._board.guess(self._players[i], guess)

			i += 1
			if i == len(self._players):
				i = 0

		self._board.ending()