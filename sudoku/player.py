from sudoku import *

class Player:
	"""
	>>> s = Sudoku('filled_puzzle_1.txt')
	>>> p = Player('player', s)
	>>> p.puzzle.is_done()
	True
	>>> p.puzzle.completed
	False
	>>> p.puzzle.check_puzzle()
	Congratulations! Your answers check out!
	>>> p.puzzle.completed
	True
	"""
	def __init__(self, name, puzzle):
		self.name = name
		self.puzzle = puzzle

	def get_pick(self):
		print(self.puzzle)
		print('Please enter the row then the column of the spot you would like to fill:\n')
		row = int(input()) - 1
		col = int(input()) - 1
		print('\n')

		print('Please enter your guess:\n')
		guess = int(input())
		print('\n')

		self.puzzle.fill_spot(row, col, guess)

		if self.puzzle.is_done():
			self.puzzle.check_puzzle()
			if self.puzzle.completed:
				print('Congrats! You completed the puzzle correcly!')
		else:
			self.get_pick()



















if __name__ == '__main__':
	import doctest
	doctest.testmod()