import re

def negative_sum(chars):
	negative_num_list = re.findall(r'-\d+', chars)
	abs_negative_num_list = [abs(int(num)) for num in negative_num_list]
	result = sum(abs_negative_num_list) * -1
	return result