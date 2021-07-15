def meme_sum(a, b):
	x = str(a)
	y = str(b)
	z = len(x) - len(y)
	q = len(y) - len(x)
	if z < 0:
		for i in range(z * -1):
			x = "{}{}".format('0', x)
	elif q < 0:
		for i in range(q * -1):
			y = "{}{}".format('0', y)
	result = ''
	for i,j in zip(x, y):
		result += str(int(i) + int(j))
	return int(result)