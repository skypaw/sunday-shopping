from datetime import datetime
import csv


def remove_past_sundays(date):
    sunday = datetime.fromisoformat(date)
    now = datetime.now()
    if sunday > now:
        return True
    else:
        return False


filtered_dates = []
with open('./_data/shopping-sundays.csv', 'r') as file:
    for dates in csv.reader(file):
        filtered_dates = filter(remove_past_sundays, dates)

with open('./_data/filtered-shopping-sundays.csv', 'w') as file:
    csv.writer(file).writerow(filtered_dates)
