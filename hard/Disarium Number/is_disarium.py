def is_disarium(n):
	str_n = str(n)
	result = 0
	for i in range(1, len(str_n) + 1):
		result += int(str_n[i - 1]) ** i
	return result == n