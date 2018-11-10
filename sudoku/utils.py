def repeat(x, n):
	"""Returns x n times

	>>> repeat('a', 4)
	['a', 'a', 'a', 'a']
	"""
	return [x for _ in range(n)]

def map(fn, l):
	"""Returns a list with fn mapped to each item in l

	>>> square = lambda x: x**2
	>>> map(square, [1, 2, 3, 4])
	[1, 4, 9, 16]
	"""
	return [fn(i) for i in l]













if __name__ == '__main__':
	import doctest
	doctest.testmod()