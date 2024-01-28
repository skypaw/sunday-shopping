---
title: Czy dzisiaj jest niedziela handlowa
layout: default
---

<h1 class="display-4 lh-1  text-center">Czy dzisiaj jest niedziela handlowa?</h1>
<p id="is-shopping-allowed" class="display-4 fw-bold lh-1 pt-4 text-center">
{% capture today %}{{"now" | date: "%B %d, %Y"}}{% endcapture %}
{% if site.data.filtered-shopping-sundays.dates[0] == today %}
    Tak! 😄
{% else %}
    Nie 😔
{% endif %}

</p>
<div class="row pt-5">
    <p class="lead">Najbliższe niedziele handlowe:</p>
    <div class="container">
        <ul id="next-sunday" class="list-group">
            {% for sunday in site.data.filtered-shopping-sundays.dates limit:3 %}
                <li class="list-group-item">{{ sunday | date: "%d.%m.%Y"}}</li>
            {% endfor %}
        </ul>
    </div>
</div>
