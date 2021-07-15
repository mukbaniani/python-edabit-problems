def pentagonal(num):
	result = 1
	step = 0
	for item in range(1,num):
		step += 5
		result += step
	return result