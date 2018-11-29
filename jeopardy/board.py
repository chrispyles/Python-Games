from categories import *
from questions import *
from player import *

class Board:
	"""
	>>> c = Categories('categories_6123.txt')
	>>> q = Questions('qs_6123.txt', 'an_6123.txt', c)
	>>> b = Board(c, q)
	>>> print(b.display())
	<BLANKLINE>
	<BLANKLINE>
	1. CARTOON FEMALES: 200, 400, 600, 800, 1000
	2. STOCK SYMBOLS: 200, 400, 600, 800, 1000
	3. A RIVER RUNS THROUGH IT: WORLD CAPITAL EDITION: 200, 400, 600, 800, 1000
	4. I NEED A HOBBY!: 200, 400, 600, 800, 1000
	5. METEROLOGICAL RHYME TIME: 200, 400, 600, 800, 1000
	6. EDISON LABS: 200, 400, 600, 800, 1000
	<BLANKLINE>
	<BLANKLINE>
	>>> b.is_done()
	False
	>>> b.questions.qs = {c:{}}
	>>> b.is_done()
	True
	"""
	def __init__(self, cats=[], qs=[], dj=False):
		self.categories = cats
		self.questions = qs

		if not dj:
			self.values = [200, 400, 600, 800, 1000]
		else:
			self.values = [400, 800, 1200, 1600, 2000]


	def display(self):
		result = '\n\n'
		for i in self.categories.cats:
			result += f'{i+1}. {self.categories.cats[i]}: {", ".join([str(i) for i in self.questions.qs[self.categories.cats[i]]])}\n'
		result += '\n'
		return result


	def question(self, cat, value):
		if value not in self.values:
			raise Exception('The value entered is not in the list')
		try:
			return self.questions.qs[cat][value]
		except KeyError as e:
			return 'Sorry, but that value as already been selected.'

	def answer_question(self, cat, value):
		q = self.question(cat, value)
		#answer = input()
		if q.check_answer(answer):
			#print(f'Correct! Your score is now ${player.score}') # DEFINE PLAYER!!!!!!!!!!!
			del self.questions.qs[cat][val]
			return True
		else:
			del self.questions.qs[cat][val]
			return False

	def is_done(self):
		qs_left = [len(self.questions.qs[cat]) for cat in self.questions.qs]
		if sum(qs_left) == 0:
			return True
		return False



















if __name__ == "__main__":
    import doctest
    doctest.testmod()