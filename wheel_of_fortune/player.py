from board import *
from wheel import *
from utils import *

class Player:
	"""
	>>> w = Wheel()
	"""
	def __init__(self, name, wheel):
		self.name = name
		self.wheel = wheel

		self.score = 0

	def spin(self):
		return self.wheel.spin()

	















if __name__ == '__main__':
	import doctest
	doctest.testmod()