from datetime import datetime

def sort_dates(lst, mode):
	return sorted(lst, key=lambda x: datetime.strptime(x, '%d-%m-%Y_%H:%M'), reverse=False if mode == 'ASC' else True)
   