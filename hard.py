from datetime import datetime
import re
import string

#https://edabit.com/challenge/G9QRtAGXb9Cu368Pw
def combinations(*items):
	result = 1
	for i in items:
		if i == 0:
			continue
		result *= i
	return result

#https://edabit.com/challenge/5bYXQfpyoithnQisa
def encode_morse(message):
	char_to_dots = {
	  'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
	  'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
	  'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
	  'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
	  'Y': '-.--', 'Z': '--..', ' ': ' ', '0': '-----',
	  '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
	  '6': '-....', '7': '--...', '8': '---..', '9': '----.',
	  '&': '.-...', "'": '.----.', '@': '.--.-.', ')': '-.--.-', '(': '-.--.',
	  ':': '---...', ',': '--..--', '=': '-...-', '!': '-.-.--', '.': '.-.-.-',
	  '-': '-....-', '+': '.-.-.', '"': '.-..-.', '?': '..--..', '/': '-..-.'
	}
	result = ""
	upper_message = message.upper()
	for word in upper_message:
		result += char_to_dots.get(word) + " "
	return result.rstrip()

#https://edabit.com/challenge/Y5Ji2HDnQTX7MxeHt
def snakefill(n):
	size = n * n
	snake_size = 1
	result = 0
	for i in range(size):
		snake_size *= 2
		if snake_size > size:
			break
		else:
			result += 1
	return result

#https://edabit.com/challenge/st8mDxreMcuWxuz8c
def pentagonal(num):
	result = 1
	step = 0
	for item in range(1,num):
		step += 5
		result += step
	return result

#https://edabit.com/challenge/7vN8ZRw43yuWNoy3Y
def parse_code(txt):
	keys = ['first_name', 'last_name', 'id']
	values = list(filter(None, txt.split('0')))
	dct = dict(zip(keys, values))
	return dct

#https://edabit.com/challenge/JzBLDzrcGCzDjkk5n
def encrypt(word):
	translate = {'a': '0', 'e': '1', 'i': '2', 'o': '2', 'u': '3'}
	reverse_word = word[::-1]
	mt = reverse_word.maketrans(translate)
	result = reverse_word.translate(mt) + 'aca'
	return result

#https://edabit.com/challenge/Xkc2iAjwCap2z9N5D
def has_friday_13(month, year):
	week_day = datetime(year, month, 13).weekday()
	return week_day == 4

#https://edabit.com/challenge/mHLAmj4vmRuXrT8Nb
def consecutive_combo(lst1, lst2):
	lst3 = lst1 + lst2
	max_lst3 = max(lst3)
	min_lst3 = min(lst3)
	sorted_lst3 = sorted(lst3)
	min_max_range = [num for num in range(min_lst3, max_lst3 + 1)]
	return sorted_lst3 == min_max_range

#https://edabit.com/challenge/yvJbdkmKHvCNtcZy9
def is_disarium(n):
	str_n = str(n)
	result = 0
	for i in range(1, len(str_n) + 1):
		result += int(str_n[i - 1]) ** i
	return result == n

#https://edabit.com/challenge/q3zrcjja7uWHejxf6
def negative_sum(chars):
	negative_num_list = re.findall(r'-\d+', chars)
	abs_negative_num_list = [abs(int(num)) for num in negative_num_list]
	result = sum(abs_negative_num_list) * -1
	return result

#https://edabit.com/challenge/temD7SmTyhdmME75i
def to_boolean_list(word):
	English_alphabet_list = list(string.ascii_lowercase)
	result = [True if (English_alphabet_list.index(i) + 1) % 2 != 0 else False for i in word]
	return result

#https://edabit.com/challenge/ehyZvt6AJF4rKFfXT
def uncensor(txt, vowels):
	r = txt.replace('*', '{}')
	return r.format(*vowels)