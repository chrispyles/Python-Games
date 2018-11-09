from categories import *

class Questions:
	"""
	>>> c = Categories('categories_6123.txt')
	>>> q = Questions('qs_6123.txt', 'an_6123.txt', c)
	>>> label = c.cat_list[0]
	>>> q.qs[label][400]
	'1 of the 2 females who solve mysteries with Scooby Doo; they got their own prequel movie in 2018'
	>>> q.answer(label, 200, 'a saxophone')
	True
	>>> q.answer(label, 200, 'test')
	False
	"""
	def __init__(self, q_file, a_file, cats, dj=False):
		self.cats = cats.items()

		f = open(q_file)
		f = f.read()
		f = f.split('\n')

		self.qs = {}

		for c in self.cats:
			d = {}
			if not dj:
				vals = [200, 400, 600, 800, 1000]
			else:
				vals = [400, 800, 1200, 1600, 2000]
			for i in range(5):
				d[vals[i]] = f[i]
			self.qs[c] = d
			del f[0:5]
		

		f = open(a_file)
		f = f.read()
		f = f.split('\n')

		self.answers = {}

		for c in cats.items():
			d = {}
			if not dj:
				vals = [200, 400, 600, 800, 1000]
			else:
				vals = [400, 800, 1200, 1600, 2000]
			for i in range(5):
				d[vals[i]] = f[i]
			self.answers[c] = d
			del f[0:5]


	def answer(self, cat, val, ans):
		if ans == self.answers[cat][val]:
			del self.qs[cat][val]
			return True
		else:
			del self.qs[cat][val]
			return False







if __name__ == "__main__":
    import doctest
    doctest.testmod()