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

def filtered_map(fn, pred, l):
	"""Returns a list with fn mapped to each element of l that satisfies
	pred; if pred not satisfied, original value inserted intstead

	>>> square = lambda x: x**2
	>>> is_odd = lambda x: x % 2 == 1
	>>> filtered_map(square, is_odd, [1, 2, 3, 4])
	[1, 2, 9, 4]
	"""
	result = []
	for i in l:
		if pred(i):
			result += [fn(i)]
		else:
			result += [i]
	return result













if __name__ == '__main__':
	import doctest
	doctest.testmod()