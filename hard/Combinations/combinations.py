def combinations(*items):
	result = 1
	for i in items:
		if i == 0:
			continue
		result *= i
	return result