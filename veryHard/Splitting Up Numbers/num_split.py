def num_split(num):
    n = -num if num < 0 else num
    result = [
        -int(index + str(number * "0")) if num < 0
	    else int(index + str(number * "0"))
	    for number, index in enumerate(str(n)[::-1])
    ]
    result.reverse()
    return result
