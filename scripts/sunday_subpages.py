import json
from datetime import datetime, timedelta

import aiofiles
import xmltodict

from scripts.templates import any_sunday_template, closest_sunday_template


class AnySunday:
    def __init__(self, sunday):
        self.date = sunday
        self.jekyll_date = self.date.strftime("%d.%m.%Y")

    def sunday_url(self) -> str:
        return f'czy-{self.date.strftime("%d-%m-%Y")}-jest-niedziela-handlowa.md'

    def sitemap(self):
        return {'loc': f'https://czyjesthandlowa.pl/{self.sunday_url()}/',
                'changefreq': 'monthly'}

    def template(self, shops_open) -> str:
        return any_sunday_template(self.jekyll_date, shops_open)

    async def generate(self, shops_open):
        async with aiofiles.open(self.sunday_url(), mode='w') as md:
            await md.writelines(self.template(shops_open))
        await self.build_sitemap()

    async def build_sitemap(self):
        async with aiofiles.open('jekyll/sitemap.xml', 'r') as sitemap:
            parsed_sitemap = xmltodict.parse(await sitemap.read())
        with aiofiles.open('jekyll/sitemap.xml', 'w') as sitemap:
            parsed_sitemap['urlset']['url'].append(self.sitemap())
            xmltodict.unparse(parsed_sitemap, sitemap)


class ClosestSunday(AnySunday):
    def sunday_url(self) -> str:
        return f'czy-najblizsza-niedziela-jest-handlowa.md'

    def template(self, shops_open) -> str:
        return closest_sunday_template(self.date, self.jekyll_date)


class Config:
    def __init__(self):
        self.config = self.load_config()

    def dates(self):
        today = datetime.now().timestamp()
        calendar = timedelta(seconds=self.last_sunday - today).days
        return [self.days(i) for i in range(calendar) if self.days(i).weekday() == 6]

    def shops_open(self, sunday):
        return True if sunday in self.config else False

    @property
    def first_sunday(self):
        return self.config[1]

    @property
    def last_sunday(self):
        return self.config[-1]

    @staticmethod
    def days(i):
        return datetime.today() + timedelta(i)

    @staticmethod
    def load_config():
        with open('jekyll/_data/filtered-shopping-sundays.json') as config:
            return json.load(config)['dates']


if __name__ == '__main__':
    config = Config()

    for date in config.dates():
        if date == config.first_sunday:
            closest_sunday = ClosestSunday(config.first_sunday)
            closest_sunday.generate(config.shops_open(config.first_sunday))
        any_sunday = AnySunday(date)
        any_sunday.generate(config.shops_open(date))
