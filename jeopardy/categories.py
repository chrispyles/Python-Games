class Categories:
	"""
	>>> c = Categories('categories_6123.txt')
	>>> print(c)
	<BLANKLINE>
	<BLANKLINE>
	1. CARTOON FEMALES
	2. STOCK SYMBOLS
	3. A RIVER RUNS THROUGH IT: WORLD CAPITAL EDITION
	4. I NEED A HOBBY!
	5. METEROLOGICAL RHYME TIME
	6. EDISON LABS
	<BLANKLINE>
	<BLANKLINE>
	"""
	def __init__(self, file):

		f = open(file)
		f = f.read()

		f = f.split('\n')

		self.cat_list = f

		self.cats = {i:j for i,j in zip(range(6), f)}

	def __repr__(self):
		result = '\n\n'
		for i in self.cats:
			result += f'{i+1}. {self.cats[i]}\n'
		result += '\n'
		return result

	def items(self):
		return self.cat_list







if __name__ == "__main__":
    import doctest
    doctest.testmod()