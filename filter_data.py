from datetime import datetime
import csv


def remove_past_sundays(date):
    sunday = datetime.fromisoformat(date)
    now = datetime.now()
    if sunday > now:
        return str(sunday)


def not_none(element):
    if not element:
        return False
    else:
        return True


mapped_dates = []
with open('jekyll/_data/shopping-sundays.csv', 'r') as file:
    for dates in csv.reader(file):
        mapped_dates = map(remove_past_sundays, dates)

with open('jekyll/_data/filtered-shopping-sundays.csv', 'w', newline='') as file:
    filtered_dates = filter(not_none, list(mapped_dates))
    writer = csv.DictWriter(file, fieldnames=['dates'])

    writer.writeheader()
    writer.writerows([{'dates': date} for date in filtered_dates])
