def majority_vote(lst):
	if not lst:
		return None
	count_vote = sorted([(lst.count(i),i) for i in sorted(set(lst), key=lst.index)], reverse=True)
	if len(count_vote) <= 1:
		return count_vote[0][1]
	elif count_vote[0][0] != count_vote[1][0]:
		return count_vote[0][1]
	else:
		return None