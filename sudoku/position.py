from sudoku import *
from player import *

class Position:
	"""

	"""
	def __init__(self, position, value):
		self.position = position
		self.value = value

	def blank(self):
		return self.value == '_'