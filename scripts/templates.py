def any_sunday_template(date, format_date, config_string):
    return f"""---
title: Czy {format_date} jest handlowa?
---

<div class="row pt-5 pb-5 text-center">
    <h1 class="pb-3">Czy {format_date} jest niedziela handlowa?</h1>
    <p class="lead">{"Tak! 🥳" if date.strftime("%Y-%m-%d") in config_string else "Nie 😔"}</p>
</div>
"""


def closest_sunday_template(format_date, is_shopping_allowed):
    return f"""---
title: Czy najbliższa niedziela ({format_date}) jest handlowa?
---

<div class="row pt-5 pb-5 text-center">
    <h1 class="pb-3">Czy najbliższa niedziela ({format_date}) jest handlowa?</h1>
    <p class="lead">{"Tak! 🥳" if is_shopping_allowed else "Nie 😔"}</p>
</div>
"""
