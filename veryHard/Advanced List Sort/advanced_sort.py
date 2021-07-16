def advanced_sort(lst):
	result = [[i for _ in range(lst.count(i))] for i in list(dict.fromkeys(lst))]
	return result