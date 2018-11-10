def repeat(x, n):
	'''Returns x n times'''
	return [x for _ in range(n)]

def map(fn, l):
	'''Returns a list with fn mapped to each item in l'''
	return [fn(i) for i in l]