from categories import *
from questions import *
from board import *

class Player:
	"""
	>>> c = Categories('categories_6123.txt')
	>>> q = Questions('qs_6123.txt', 'an_6123.txt', c)
	>>> b = Board(c, q)
	>>> p = Player('Player 1', b)
	>>> p.score
	0
	>>> cat = p.board.categories.items()[0]
	>>> print(f'Available amounts: {", ".join([str(i) for i in p.board.questions.qs[cat]])}')
	Available amounts: 200, 400, 600, 800, 1000
	>>> print(f'{p.board.question(cat, 200)}')
	Lisa Simpson takes moral stands on many an issue & also plays a mean one of these instruments
	"""
	def __init__(self, name, board):
		self.name = name
		self.score = 0
		self.board = board

	def choose_question(self):
		print('~~~~~~~~~~')
		print(self.board.display())
		print('Please enter the number of the category you would like.')
		cat = int(input()) - 1
		try:
			cat = self.board.categories.items()[cat]
		except IndexError:
			print('Sorry, but that is not an available catory.\n\n')
			self.choose_question()
		print('\n\nPlease enter the amount.')
		print(f'Available amounts: {", ".join([str(i) for i in self.board.questions.qs[cat]])}\n\n')
		val = int(input())

		print(f'\n\n{self.board.question(cat, val)}')

		if self.board.question(cat, val) != 'Sorry, but that value as already been selected.':

			print('\n\nPlease enter your answer below (you can omit the question form):\n\n')
			answer = input()
			if self.board.questions.answer(cat, val, answer):
				self.score += val
				print(f'\n\nCorrect!\n\nCurrent Score: ${self.score}')
			else:
				self.score -= val
				print('\n\nSorry, incorrect...\n\n')

		else:
			print('\n\n')
			self.choose_question()















if __name__ == "__main__":
    import doctest
    doctest.testmod()