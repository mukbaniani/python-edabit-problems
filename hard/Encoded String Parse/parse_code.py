def parse_code(txt):
	keys = ['first_name', 'last_name', 'id']
	values = list(filter(None, txt.split('0')))
	dct = dict(zip(keys, values))
	return dct