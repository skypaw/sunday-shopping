from datetime import datetime
import csv
import json


def remove_past(date):
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
with open('shopping-sundays.csv', 'r') as file:
    for dates in csv.reader(file):
        mapped_dates = map(remove_past, dates)

with open('jekyll/_data/filtered-shopping-sundays.json', 'w', newline='') as file:
    filtered_dates = filter(not_none, list(mapped_dates))
    file.writelines(json.dumps({'dates': list(filtered_dates)}))
