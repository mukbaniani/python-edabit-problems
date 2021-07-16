def will_hit(equation, position):
	result = eval(equation.replace('y ', str(position[1]) + ' =').replace('x', '*' + str(position[0])))
	return result