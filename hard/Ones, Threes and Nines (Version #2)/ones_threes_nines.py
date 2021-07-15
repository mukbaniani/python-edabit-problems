class ones_threes_nines:
	def __init__(self, num):
		self.answer = "nines:{}, threes:{}, ones:{}".format(num // 9, num % 9 // 3, num % 9 % 3)