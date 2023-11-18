import datetime
import xmltodict

TODAY_TIMESTAMP = datetime.datetime.now().timestamp()


def calculate_day(x):
    return datetime.datetime.fromtimestamp(TODAY_TIMESTAMP) + datetime.timedelta(days=x)


def generate_md(date):
    format_date = date.strftime("%d.%m.%Y")
    return f'''---
title: Czy {format_date} jest handlowa?
---

<div class="row pt-5">
    <h2 class="pb-3">Czy {format_date} jest niedziela handlowa?</h2>
    <p class="lead">{"Tak! 🥳" if date.strftime("%Y-%m-%d") in config_string else "Nie 😔"}</p>
</div>
'''


def sunday_url(date):
    return f'czy-{date.strftime("%d-%m-%Y")}-jest-niedziela-handlowa'


with open('shopping-sundays.csv') as file:
    config_string = file.readline()
    last_confing_sunday = config_string[config_string.rfind(',') + 1:]

last_confing_sunday_timestamp = datetime.datetime.fromisoformat(last_confing_sunday).timestamp()
delta_days = datetime.timedelta(seconds=last_confing_sunday_timestamp - TODAY_TIMESTAMP).days

date_list = [calculate_day(i) for i in range(delta_days) if calculate_day(i).weekday() == 6]

with open('jekyll/sitemap.xml', 'r') as sitemap_read:
    default_sitemap = xmltodict.parse(sitemap_read.read())
    for date in date_list:
        with open(f'jekyll/{sunday_url(date)}.md', 'w', encoding='utf-8') as file:
            file.writelines(generate_md(date))
        default_sitemap['urlset']['url'].append({'loc': f'https://czyjesthandlowa.pl/{sunday_url(date)}/'

with open('jekyll/sitemap.xml', 'w') as sitemap_write:
    xmltodict.unparse(default_sitemap, sitemap_write)
