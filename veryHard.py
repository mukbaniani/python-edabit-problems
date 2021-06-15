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