def convert_to_hex(txt):
	result = ''
	for word in txt:
		result += hex(ord(word))[2:] + ' '
	return result.rstrip()