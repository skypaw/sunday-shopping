from datetime import datetime
import csv
import json


class FilterDates:
    def __init__(self, dates):
        self.dates = dates
        self.future_sundays = self.remove_past_sundays()

    def remove_past_sundays(self):
        return map(self.remove_past, self.dates)

    def filter_dates(self):
        return filter(self.not_none, list(self.future_sundays))

    @staticmethod
    def remove_past(date):
        sunday = datetime.fromisoformat(date)
        now = datetime.now()
        if sunday.date() >= now.date():
            return sunday

    @staticmethod
    def not_none(date):
        if not date:
            return False
        else:
            return True

    @staticmethod
    def load_dates():
        dates = []
        with open("shopping-sundays.csv", "r") as file:
            for row in csv.reader(file):
                dates = row
        return dates

    @staticmethod
    def save_dates(filtered_dates):
        with open(
            "jekyll/_data/filtered-shopping-sundays.json", "w", newline=""
        ) as file:
            file.writelines(json.dumps({"dates": [datetime.strftime(i, "%B %d, %Y") for i in filtered_dates]}))


if __name__ == "__main__":
    raw_dates = FilterDates.load_dates()
    filter_data = FilterDates(raw_dates)
    filter_data.save_dates(filter_data.filter_dates())
