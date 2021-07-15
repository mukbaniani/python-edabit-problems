from datetime import datetime

def weekday_dutch(date):
	day, month, year = date.split()
	english_dutch = {0: 'maandag', 1: 'dinsdag', 2:
	'woensdag', 3: 'donderdag', 4: 'vrijdag',
	5: "zaterdag", 6: 'zondag'}
	week_day = datetime(int(year), int(month), int(day)).weekday()
	return english_dutch.get(week_day)