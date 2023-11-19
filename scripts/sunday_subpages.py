import datetime
import xmltodict

TODAY_TIMESTAMP = datetime.datetime.now().timestamp()


def calculate_day(x: int) -> datetime.datetime:
    return datetime.datetime.fromtimestamp(TODAY_TIMESTAMP) + datetime.timedelta(days=x)


def sunday_url(date: datetime.datetime) -> str:
    return f'czy-{date.strftime("%d-%m-%Y")}-jest-niedziela-handlowa'


def check_if_shopping_allowed(list_index: int) -> None:
    if date_list[list_index] <= datetime.datetime.today() + datetime.timedelta(7):
        closest_sunday(date_list[list_index], is_shopping_allowed=True)
    else:
        closest_sunday(date_list[list_index])


def closest_sunday(date, is_shopping_allowed=False) -> None:
    format_date = date.strftime("%d.%m.%Y")
    with open(f'jekyll/czy-najblizsza-niedziela-jest-handlowa.md', 'w', encoding='utf-8') as file:
        closest = f'''---
title: Czy najbliższa niedziela ({format_date}) jest handlowa?
---

<div class="row pt-5">
    <h2 class="pb-3">Czy najbliższa niedziela ({format_date}) jest handlowa?</h2>
    <p class="lead">{"Tak! 🥳" if is_shopping_allowed else "Nie 😔"}</p>
</div>
'''
        file.writelines(closest)


def generate_md(date) -> str:
    format_date = date.strftime("%d.%m.%Y")
    return f'''---
title: Czy {format_date} jest handlowa?
---

<div class="row pt-5">
    <h2 class="pb-3">Czy {format_date} jest niedziela handlowa?</h2>
    <p class="lead">{"Tak! 🥳" if date.strftime("%Y-%m-%d") in config_string else "Nie 😔"}</p>
</div>
'''


with open('shopping-sundays.csv') as file:
    config_string = file.readline()
    last_confing_sunday = config_string[config_string.rfind(',') + 1:]

last_confing_sunday_timestamp = datetime.datetime.fromisoformat(last_confing_sunday).timestamp()
delta_days = datetime.timedelta(seconds=last_confing_sunday_timestamp - TODAY_TIMESTAMP).days

date_list = [calculate_day(i) for i in range(delta_days) if calculate_day(i).weekday() == 6]

# create closest sunday subpage

if date_list[0].date() == datetime.datetime.today().date():
    check_if_shopping_allowed(1)
else:
    check_if_shopping_allowed(0)

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
