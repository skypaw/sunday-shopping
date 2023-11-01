---
title: Najbliższa niedziela handlowa
---

<div class="row pt-5">
    <p class="lead">Najbliższa niedziela handlowa przypada w dniu:</p>
    <div class="container">
        <ul>
            {% for sunday in site.data.filtered-shopping-sundays.dates limit:1 %}
                <li class="list-group-item">{{ sunday | date: "%d.%m.%Y"}}</li>
            {% endfor %}
        </ul>
    </div>
</div>



