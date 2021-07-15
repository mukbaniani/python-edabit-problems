def consecutive_combo(lst1, lst2):
	lst3 = lst1 + lst2
	max_lst3 = max(lst3)
	min_lst3 = min(lst3)
	sorted_lst3 = sorted(lst3)
	min_max_range = [num for num in range(min_lst3, max_lst3 + 1)]
	return sorted_lst3 == min_max_range