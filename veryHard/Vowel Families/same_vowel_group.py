def same_vowel_group(w):
	vowles_in_first_word = ''
	vowles = ['a', 'e', 'i', 'o', 'u']
	for i in w[0]:
		if i in vowles and  i not in vowles_in_first_word:
			vowles_in_first_word += i
	not_in = [i for i in vowles if i not in vowles_in_first_word]
	result = [i for i in w[1:] if all(True if j in i and j not in not_in else False for j in i)]
	result.insert(0, w[0])
	return result