import json
from datetime import datetime, timedelta, date

import xmltodict

from templates import any_sunday_template, closest_sunday_template


class AnySunday:
    def __init__(self, sunday):
        self.date = sunday
        self.jekyll_date = self.date.strftime("%d.%m.%Y")

    def sunday_url(self) -> str:
        return f"czy-{self.jekyll_date}-jest-niedziela-handlowa"

    def sitemap(self):
        return {
            "loc": f"https://czyjesthandlowa.pl/{self.sunday_url()}/",
            "changefreq": "monthly",
        }

    def template(self, shops_open) -> str:
        return any_sunday_template(self.jekyll_date, shops_open)

    def generate(self, shops_open):
        with open(f"{self.sunday_url()}.md", mode="w", encoding="utf-8") as md:
            md.writelines(self.template(shops_open))
        self.build_sitemap()

    def build_sitemap(self):
        with open("jekyll/sitemap.xml", "r") as sitemap:
            parsed_sitemap = xmltodict.parse(sitemap.read())
        with open("jekyll/sitemap.xml", "w") as sitemap:
            parsed_sitemap["urlset"]["url"].append(self.sitemap())
            xmltodict.unparse(parsed_sitemap, sitemap)


class ClosestSunday(AnySunday):
    def sunday_url(self) -> str:
        return "czy-najblizsza-niedziela-jest-handlowa"

    def template(self, shops_open) -> str:
        return closest_sunday_template(self.date, self.jekyll_date)


class Config:
    def __init__(self):
        self.config = []

    def dates(self):
        today = date.today()
        calendar = (self.last_sunday - today).days + 7  # days
        return [self.days(i) for i in range(calendar) if self.days(i).weekday() == 6]

    def shops_open(self, sunday):
        return True if sunday in self.config else False

    def load_config(self):
        with open("jekyll/_data/filtered-shopping-sundays.json") as json_config:
            jekyll_format = json.load(json_config)["dates"]
            self.config = [datetime.strptime(i, "%B %d, %Y").date() for i in jekyll_format]

    @property
    def first_sunday(self):
        return self.config[0]

    @property
    def last_sunday(self):
        return self.config[-1]

    @staticmethod
    def days(i):
        return date.today() + timedelta(i)


if __name__ == "__main__":
    config = Config()
    config.load_config()

    for date in config.dates():
        any_sunday = AnySunday(date)
        any_sunday.generate(config.shops_open(date))

    closest_sunday = ClosestSunday(config.first_sunday)
    closest_sunday.generate(config.shops_open(config.first_sunday))
