from datetime import datetime

def has_friday_13(month, year):
	week_day = datetime(year, month, 13).weekday()
	return week_day == 4