from wheel import *
from secret import *
from player import *
from utils import *
from override import *
import string

vowels = ['a', 'e', 'i', 'o', 'u']

class Board:
	"""
	>>> w = Wheel()
	>>> p = Player('Player 1', w)
	>>> s = SecretPhrase('testing this out', 'test')
	>>> b = Board(s, p)
	"""
	def __init__(self, secret, players=[]):
		self.secret = secret
		self.category = self.secret.category
		self.players = players

	def get_letter(self, player):
		print(f'\n\n{self.secret.show_status()}')
		print(f"\n\n{player.name}'s Score: {player.score}\nDo you want to buy a vowel?")
		buy_vowel = input()

		if buy_vowel == 'OVERRIDE':
			try:
				Override(self, player)
			except AssertionError as e:
				print(e)
				self.get_letter(player)
		else:
			try:
				assert buy_vowel in yes or buy_vowel in no, 'Please enter yes or no.'
			except AssertionError as e:
				print(e)
				self.get_letter(player)
		
		if buy_vowel in yes:
			try:
				assert player.score >= 200, 'Your score is too low to buy a vowel.'
			except AssertionError as e:
				print(e)
				self.get_letter(player)
			print('\n\nPlease enter your vowel.\n')
			letter = input()
			
			try:
				assert letter in string.ascii_lowercase, 'Please enter a lowercase letter.'
			except AssertionError as e:
				print(e)
				self.get_letter(player)
			
			player.score -= 200
			self.secret.guess_letter(letter, player)
		else:
			#print('\n\nPress Enter to spin!\n')
			#input()
			value = player.spin()
			print(f'\n\nYou spun: {value}\nPlease enter a letter.')
			letter = input()

			try:
				assert letter in string.ascii_lowercase, 'Please enter a lowercase letter.'
			except AssertionError as e:
				print(e)
				self.get_letter(player)

			try:
				assert letter not in vowels, "You didn't buy a vowel!"
			except AssertionError as e:
				print(e)
				self.get_letter(player)

			num_correct = self.secret.guess_letter(letter, player)
			player.score += num_correct * value
	















if __name__ == '__main__':
	import doctest
	doctest.testmod()