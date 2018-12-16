def repeat(x, n):
	return [x for _ in range(n)]

def key_of_max(d):
	"""
	>>> key_of_max({1:2, 3:4, 5:6})
	5
	"""
	max_key = list(d.keys())[0]
	max_val = d[max_key]
	for key in d:
		if d[key] > max_val:
			max_key = key
			max_val =d[key]
	return max_key

yes = ['Yes', 'yes', 'y', 'Y', 'yeah', 'ye']
no = ['No', 'no', 'N', 'n']


















if __name__ == '__main__':
	import doctest
	doctest.testmod()