from math import gcd
# import numpy as np

#https://edabit.com/challenge/uPAmqwiHmvwpwoBom
def convert_to_roman(num):
	nums = [1,4,5,9,10,40,50,90,100,400,500,900,1000]
	roman = ['I', 'IV', 'V', 'IX', 'X', 'XL', 'L', 'XC', 'C', 'CD', 'D', 'CM', 'M']
	d = dict(zip(nums, roman))
	result = ''
	while num > 0:
		for i in range(len(nums)):
			if num <= 0:
				break
			elif num == nums[i]:
				result += d.get(nums[i])
				num -= nums[i]
				break
			elif num < nums[i]:
				result += d.get(nums[i-1])
				num -= nums[i-1]
				break
			elif num >= 1000:
				result += 'M'
				num -= 1000
				break
	return result


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

#https://edabit.com/challenge/Fpymv2HieqEd7ptAq
def split(txt):
	word = ''
	num_9 = 0
	num_0 = 0
	res_list = []
	for i in txt:
		if i == "(":
			num_9 += 1
			word += "("
		elif i == ")":
			num_0 += 1
			word += ")"
			if num_0 == num_9:
				num_0 = 0
				num_9 = 0
				res_list.append(word)
				word = ''
	return res_list

#https://edabit.com/challenge/9YfCbQpRPqRLzPCcg
def will_hit(equation, position):
	result = eval(equation.replace('y ', str(position[1]) + ' =').replace('x', '*' + str(position[0])))
	return result

#https://edabit.com/challenge/6vSZmN66xhMRDX8YT
def advanced_sort(lst):
	result = [[i for _ in range(lst.count(i))] for i in list(dict.fromkeys(lst))]
	return result

#https://edabit.com/challenge/vQgmyjcjMoMu9YGGW
def simplify(txt):
	num1, num2 = txt.split('/')
	gcd_num1_num2 = gcd(int(num1), int(num2))
	if gcd_num1_num2 == int(num1) and num1 < num2:
		return int(num2) // int(num2)
	elif gcd_num1_num2 == int(num2) and num2 < num1:
		return int(num1) // int(num2)
	elif gcd_num1_num2 == 1:
		return txt	
	else:
		return f'{int(num1) // gcd_num1_num2}/{int(num2) // gcd_num1_num2}'


#https://edabit.com/challenge/A8gEGRXqMwRWQJvBf
# def tic_tac_toe(board):
# 	array_board = np.array(board)
# 	array_board_T = array_board.T
# 	for i, j in zip(array_board, array_board_T):
# 		if len(set(i)) == 1:
# 			return i[0]
# 		elif len(set(array_board.diagonal())) == 1:
# 			return array_board.diagonal()[0]
# 		elif len(set(j)) == 1:
# 			return j[0]
# 	return 'Draw'

#https://edabit.com/challenge/S7rdJsn6vkfC9BzcR
class Employee:
	def __init__(self, fullname, **kwargs):
		self.name, self.last_name = fullname.split()
		self.salary = kwargs.get('salary')
		self.height = kwargs.get('height')
		self.nationality = kwargs.get('nationality')
		self.subordinates = kwargs.get('subordinates')

#https://edabit.com/challenge/sg7j2sT8yBbY7eFYG
class Magic:

	def trim(self, txt):
		return txt.strip()

	def str_length(self, txt):
		return len(txt)

	def list_slice(self, lst, slice):
		return lst[slice[0] -1 : slice[1]]

	def replace(self, txt, char, to):
		return txt.replace(char, to)

#https://edabit.com/challenge/uwFHSRewNpmBNvbME
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