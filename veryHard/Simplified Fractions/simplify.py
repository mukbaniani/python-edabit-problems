from math import gcd

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
		return f"{int(num1) // gcd_num1_num2}/{int(num2) // gcd_num1_num2}"