import json
from abc import ABC, abstractmethod
from datetime import datetime, timedelta

import xmltodict

from templates import any_sunday_template, closest_sunday_template


class Subpage(ABC):
    @abstractmethod
    def sunday_url(self):
        pass

    @abstractmethod
    def template(self):
        pass


class AnySunday(Subpage):
    def __init__(self, sunday):
        self.date = sunday
        self.jekyll_date = self.date.strftime("%d.%m.%Y")

    def sunday_url(self) -> str:
        return f'czy-{self.date.strftime("%d-%m-%Y")}-jest-niedziela-handlowa'

    def template(self) -> str:
        return any_sunday_template(self.date, self.jekyll_date)


class ClosestSunday(Subpage):
    def __init__(self, sunday):
        self.date = sunday
        self.jekyll_date = self.date.strftime("%d.%m.%Y")

    def sunday_url(self) -> str:
        return f'czy-najblizsza-niedziela-jest-handlowa'

    def template(self) -> str:
        return closest_sunday_template(self.date, self.jekyll_date)


TODAY_TIMESTAMP = datetime.now().timestamp()


def calculate_day(x: int) -> datetime:
    return datetime.fromtimestamp(TODAY_TIMESTAMP) + timedelta(days=x)


def sunday_url(date: datetime) -> str:
    return f'czy-{date.strftime("%d-%m-%Y")}-jest-niedziela-handlowa'


def check_if_shopping_allowed(list_index: int, list_of_sundays: list) -> None:
    if datetime.fromisoformat(list_of_sundays[list_index]).date() <= (
            datetime.today() + timedelta(7)).date():
        closest_sunday_A(date_list[list_index], is_shopping_allowed=True)
    else:
        closest_sunday_A(date_list[list_index])


def closest_sunday_A(date, is_shopping_allowed=False) -> None:
    format_date = date.strftime("%d.%m.%Y")
    with open(f'jekyll/czy-najblizsza-niedziela-jest-handlowa.md', 'w', encoding='utf-8') as file:
        closest = closest_sunday_template(format_date, is_shopping_allowed)
        file.writelines(closest)


def generate_md(date) -> str:
    format_date = date.strftime("%d.%m.%Y")
    return any_sunday_template(date, format_date, config_string)


with open('shopping-sundays.csv') as file:
    config_string = file.readline()
    last_confing_sunday = config_string[config_string.rfind(',') + 1:]

last_confing_sunday_timestamp = datetime.fromisoformat(last_confing_sunday).timestamp()
delta_days = timedelta(seconds=last_confing_sunday_timestamp - TODAY_TIMESTAMP).days

date_list = [calculate_day(i) for i in range(delta_days) if calculate_day(i).weekday() == 6]

# create closest sunday subpage

with open('jekyll/_data/filtered-shopping-sundays.json') as file:
    shopping_sundays = json.load(file)['dates']

if datetime.fromisoformat(shopping_sundays[0]).date() == datetime.today().date():
    check_if_shopping_allowed(1, shopping_sundays)
else:
    check_if_shopping_allowed(0, shopping_sundays)

# create sitemap and subpages

with open('jekyll/sitemap.xml', 'r') as sitemap_read:
    default_sitemap = xmltodict.parse(sitemap_read.read())
    for date in date_list:
        with open(f'jekyll/{sunday_url(date)}.md', 'w', encoding='utf-8') as file:
            file.writelines(generate_md(date))
        default_sitemap['urlset']['url'].append({'loc': f'https://czyjesthandlowa.pl/{sunday_url(date)}/',
                                                 'changefreq': 'monthly'})

with open('jekyll/sitemap.xml', 'w') as sitemap_write:
    xmltodict.unparse(default_sitemap, sitemap_write)

if __name__ == '__main__':
    # asyncio.run()

    #
    # create subpages
    # create sitemap
    pass
