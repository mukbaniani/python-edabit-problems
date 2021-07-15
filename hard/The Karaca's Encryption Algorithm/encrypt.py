def encrypt(word):
	translate = {'a': '0', 'e': '1', 'i': '2', 'o': '2', 'u': '3'}
	reverse_word = word[::-1]
	mt = reverse_word.maketrans(translate)
	result = reverse_word.translate(mt) + 'aca'
	return result