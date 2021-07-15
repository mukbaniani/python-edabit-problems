import string

def to_boolean_list(word):
	English_alphabet_list = list(string.ascii_lowercase)
	result = [True if (English_alphabet_list.index(i) + 1) % 2 != 0 else False for i in word]
	return result