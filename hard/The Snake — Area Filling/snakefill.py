def snakefill(n):
	size = n * n
	snake_size = 1
	result = 0
	for i in range(size):
		snake_size *= 2
		if snake_size > size:
			break
		else:
			result += 1
	return result