from datetime import datetime
import csv


def remove_past_sundays(date):
    sunday = datetime.fromisoformat(date)
    now = datetime.now()
    if sunday > now:
        return sunday
    else:
        return None


def not_none(element):
    if element is None:
        return False
    return True


mapped_dates = []
with open('jekyll/_data/shopping-sundays.csv', 'r') as file:
    for dates in csv.reader(file):
        mapped_dates = map(remove_past_sundays, dates)

with open('jekyll/_data/filtered-shopping-sundays.csv', 'w') as file:
    filtered_dates = filter(not_none, mapped_dates)
    csv.writer(file).writerow(filtered_dates)
