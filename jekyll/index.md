---
title: Czy dziś jest niedziela handlowa
---

<h2 class="display-4 lh-1  text-center">Czy dziś jest niedziela handlowa?</h2>
<h1 id="is-shopping-allowed" class="display-4 fw-bold lh-1 pt-4 text-center">Nie</h1>
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
