def super_digit(n, k):
	def sum_digits(num):
		result = 0
		while num:
			result += num % 10
			num //= 10
		return result
	res = int(n * k)
	while res > 9:
		res = sum_digits(res)
	return res