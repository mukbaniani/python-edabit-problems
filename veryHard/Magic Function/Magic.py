class Magic:

	def trim(self, txt):
		return txt.strip()

	def str_length(self, txt):
		return len(txt)

	def list_slice(self, lst, slice):
		return lst[slice[0] -1 : slice[1]]

	def replace(self, txt, char, to):
		return txt.replace(char, to)