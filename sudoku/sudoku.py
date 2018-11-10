from utils import *

class Sudoku:
	"""
	>>> s = Sudoku([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
	>>> print(s)
	<BLANKLINE>
	[1, 2, 3]
	[4, 5, 6]
	[7, 8, 9]
	<BLANKLINE>
	>>> s1 = Sudoku(file='test_puzzle.txt')
	>>> print(s1)
	<BLANKLINE>
	[1, 2, 3]
	[4, 5, 6]
	[7, 8, 9]
	<BLANKLINE>
	"""

	def __init__(self, rows=[], file=''):
		if len(file) == 0:
			self.rows = rows
		elif len(rows) == 0 and len(file) != 0:
			f = open(file)
			f = f.read()
			f = f.split('\n')
			f = [i.split(',') for i in f]
			f = [map(int, i) for i in f]
			self.rows = f
		else:
			raise Exception('Must enter list of rows or a filepath')

	def __repr__(self):
		result = '\n'
		for row in self.rows:
			result += str(row) + '\n' 
		return result

	def check_puzzle(self):
		"""
		>>> s = Sudoku(file = 'puzzle_1.txt')
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
		else:
			print('Sorry, but your answers do not work.')



















if __name__ == '__main__':
	import doctest
	doctest.testmod()