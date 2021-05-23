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