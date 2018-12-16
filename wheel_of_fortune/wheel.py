from utils import *
from random import choice

class Wheel:
	"""
	>>> w = Wheel()
	>>> w.numbers
	[200, 200, 200, 200, 200, 400, 400, 400, 400, 600, 600, 600, 800, 800, 1000]
	>>> w.spin() in [200, 400, 600, 800, 1000]
	True
	"""
	def __init__(self):
		self.numbers = repeat(200, 5) + repeat(400, 4) + repeat(600, 3) + repeat(800, 2) + repeat(1000, 1)

	def spin(self):
		return choice(self.numbers)















if __name__ == '__main__':
	import doctest
	doctest.testmod()