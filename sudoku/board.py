from position import *
from player import *

class Board:
	"""
	>>> s = Sudoku(rows=[[1, 2, 3], [4, 5, 6], [7, 8, 9]])
	>>> print(s)
	<BLANKLINE>
	[1, 2, 3]
	[4, 5, 6]
	[7, 8, 9]
	<BLANKLINE>
	>>> s1 = Sudoku('test_puzzle.txt')
	>>> print(s1)
	<BLANKLINE>
	[1, 2, 3]
	[4, 5, 6]
	[7, 8, 9]
	<BLANKLINE>
	"""
	def __init__(self, file='', rows=[]):
		"""
		>>> s = Sudoku(rows=[[1,2,3], [4,5,6]])
		Traceback (most recent call last):
		  File "<stdin>", line 1, in <module>
		Exception: You need an equal number of rows and columns!
		"""
		self.completed = False
		if len(file) == 0:
			self.rows = rows
		elif len(rows) == 0 and len(file) != 0:
			f = open(file)
			f = f.read()
			f = f.split('\n')
			f = [i.split(',') for i in f]

			not_underscore = lambda x: x != '_'

			f = [filtered_map(int, not_underscore, i) for i in f]
			self.rows = f
		else:
			raise Exception('Must enter list of rows or a filepath')


		min_row_len = min([len(self.rows[i]) for i in range(len(self.rows))])
		max_row_len = max([len(self.rows[i]) for i in range(len(self.rows))])

		if len(self.rows) != min_row_len or min_row_len != max_row_len:
			raise Exception('You need an equal number of rows and columns!')


	def __repr__(self):
		result = '\n'
		for row in self.rows:
			result += str(row) + '\n'
		return result

	def __contains__(self, item):
		# finish this

	def check_puzzle(self):
		"""
		>>> s = Sudoku('filled_puzzle_1.txt')
		>>> s.check_puzzle()
		Congratulations! Your answers check out!
		"""
		collection = []
		for i in range(1, 10):
			for j in range(9):
				num_occurances = sum([i == k[j] for k in self.rows])
				if num_occurances == 1:
					collection += [1]
				else:
					print('Sorry, but your answers do not work.')
		for i in range(1, 10):
			for j in self.rows:
				num_occurances = sum([i == j[k] for k in range(9)])
				if num_occurances == 1:
					collection += [1]
				else:
					print('Sorry, but your answers do not work.')
		if sum(collection) == 162:
			print('Congratulations! Your answers check out!')
			self.completed = True
		else:
			print('Sorry, but your answers do not work.')

	def is_done(self):
		# return '_' not in self

	def fill_spot(self, row, col, guess):
		self.rows[row][col] = guess


# open unfilled puzzle
s = Sudoku('puzzle_2.txt')



















if __name__ == '__main__':
	import doctest
	doctest.testmod()