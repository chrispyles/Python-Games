from random import choice
from board import *
from player import *
from wheel import *
import string

def generate_secret_phrase():
	phrases = open('phrases.txt').read()
	phrases = phrases.split('\n')

	d = {}
	while len(phrases) > 0:
		d[phrases[1]] = phrases[0]
		del phrases[0:2]

	selected_phrase = choice(list(d.keys()))

	return selected_phrase, d[selected_phrase]


class SecretPhrase:
	def __init__(self, phrase, category):
		"""
		>>> p = SecretPhrase('testing this out', 'test')
		>>> w = Wheel()
		>>> p1 = Player('P1', w)
		>>> p.phrase
		'testing this out'
		>>> p.indices[2]
		's'
		>>> p.blanks
		['_', '_', '_', '_', '_', '_', '_', ' ', '_', '_', '_', '_', ' ', '_', '_', '_']
		>>> p.guess_letter('z', p1)
		0
		>>> p.guess_letter('e', p1)
		1
		>>> p.blanks
		['_', 'e', '_', '_', '_', '_', '_', ' ', '_', '_', '_', '_', ' ', '_', '_', '_']
		>>> p.guess_letter('e', p1)
		Traceback (most recent call last):
		  File "<stdin>", line 1, in <module>
		AssertionError: You need to guess a letter not already guessed.
		>>> p.show_status()
		'test: _ e _ _ _ _ _   _ _ _ _   _ _ _'
		"""
		self.phrase = phrase
		self.category = category
		
		self.indices = {i : j for i, j in zip(range(len(phrase)), phrase)}

		self.ascii_dict = {low : up for low, up in zip(string.ascii_lowercase, string.ascii_uppercase)}

		self.blanks = []
		for letter in self.phrase:
			if letter == ' ':
				self.blanks += [' ']
			else:
				self.blanks += ['_']

		self.guesses = []

	def __repr__(self):
		return f'{self.category}: <secret phrase>'

	def assign_board(self, board):
		"""
		>>> s = SecretPhrase('test', 'test')
		>>> b = Board(s)
		>>> s.assign_board(b)
		>>> s.board.players
		[]
		"""
		self.board = board

	def guess_letter(self, letter, player):
		try:
			assert letter not in self.guesses, 'You need to guess a letter not already guessed.'
		except AssertionError as e:
			print(e)
			self.board.get_letter(player)

		try:
			assert letter in string.ascii_lowercase, 'Please enter a lowercase letter.'	
		except AssertionError as e:
			print(e)
			self.board.get_letter(player)
	
		self.guesses += [letter]
		if letter not in self.phrase:
			if self.ascii_dict[letter] not in self.phrase:
				return 0
			else:
				count = 0
				for i in self.indices:
					if self.indices[i] == self.ascii_dict[letter]:
						self.blanks[i] = self.ascii_dict[letter]
						count += 1
			return count
		else:
			count = 0
			for i in self.indices:
				if self.indices[i] == letter:
					self.blanks[i] = letter
					count += 1
			return count

	def complete_puzzle(self, answer):
		return answer == self.phrase

	def is_done(self):
		return '_' not in self.blanks

	def show_status(self):
		return self.category + ': ' + ' '.join(self.blanks)


















if __name__ == '__main__':
	import doctest
	doctest.testmod()