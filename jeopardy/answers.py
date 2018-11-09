from questions import *
from categories imort *

class Answer:
	"""
	>>>
	"""
	def __init__(self, file):
		f = open(file)
		f = f.read()
		f = f.split('\n')
		
		self.anwers = []

		for _ in range(6):
			self.answers += [f[0:5]]
			del f[0:5]	












if __name__ == "__main__":
    import doctest
    doctest.testmod()