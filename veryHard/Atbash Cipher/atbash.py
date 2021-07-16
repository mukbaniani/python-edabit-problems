def atbash(txt):
	ord_a = ord('a')
	ord_z = ord('z')
	ord_A = ord('A')
	ord_Z = ord('Z')
	result = ''
	for word in txt:
		if ord(word) < 65:
			result += word
		elif word.islower():
			to_chr = ord_a + ord_z - ord(word)
			result += chr(to_chr)
		elif word.isupper():
			to_chr = ord_A + ord_Z - ord(word)
			result += chr(to_chr)
		elif word.isspace():
			result += ' '
	return result