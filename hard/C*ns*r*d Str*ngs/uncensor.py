def uncensor(txt, vowels):
	r = txt.replace('*', '{}')
	return r.format(*vowels)
