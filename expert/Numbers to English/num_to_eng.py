def num_to_eng(n):
    if n == 0:
        return 'zero'
    num_dct = {
	    1: 'one', 2: 'two', 3: 'three', 4: 'four',
		5: 'five', 6: "six", 7: 'seven', 8: 'eight',
		9: 'nine', 10: 'teen', 11: 'eleven',
		12: 'twelve', 13: 'thirteen', 20: 'twenty', 30: 'thirty',
        40: 'forty', 50: 'fifty', 60: 'sixty', 70: 'seventy',
        80: 'eighty', 90: 'ninety', 100: 'hundred'
	}
    result = ''
    hundreds = n // 100
    if hundreds:
        result += f'{num_dct.get(hundreds)} hundred '
    dozens = n % 100
    if dozens > 9:
        get_dozens = num_dct.get(dozens)
        if get_dozens:
            result += f'{get_dozens} '
            n = 0
        elif dozens > 13 and dozens < 20:
            result += f"{num_dct.get(int(str(dozens)[1]))}{num_dct.get(int(str(dozens)[0] + '0'))}"
            n = 0
        else:
            result += f"{num_dct.get(int(str(dozens)[0] + '0'))} "
    unit = n % 10
    if unit:
        result += num_dct.get(unit)
    return result
