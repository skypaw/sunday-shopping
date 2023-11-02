import datetime

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


with open('../shopping-sundays.csv') as file:
    config_string = file.readline()
    last_confing_sunday = config_string[config_string.rfind(',') + 1:]

last_confing_sunday_timestamp = datetime.datetime.fromisoformat(last_confing_sunday).timestamp()
delta_days = datetime.timedelta(seconds=last_confing_sunday_timestamp - TODAY_TIMESTAMP).days

date_list = [calculate_day(i) for i in range(delta_days) if calculate_day(i).weekday() == 6]

for date in date_list:
    with open(f'../jekyll/czy-{date.strftime("%d-%m-%Y")}-jest-niedziela-handlowa.md', 'w', encoding='utf-16') as file:
        file.writelines(generate_md(date))
