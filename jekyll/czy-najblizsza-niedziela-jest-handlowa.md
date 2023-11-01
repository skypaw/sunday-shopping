---
title: Czy najbliższa niedziela jest handlowa?
---

<div class="row pt-5">
    <p class="lead">Czy najbliższa niedziela ( ) jest handlowa:</p>
    <div class="container">
        <ul>
            {% assign date_to_sec = site.data.filtered-shopping-sundays.dates[0] %}
            {% date_to_sec | date: "%s" %}
            {% date_to_sec | minus: 604800 %}

            {% assign today_to_sec = "now" %}
            {% today_to_sec | date : "%s" %}

            {% if date_to_sec <= today_to_sec %}
                <li class="list-group-item">Tak! 😄</li>
            {% else %}
              <li class="list-group-item">Nie 😔</li>
            {% endif %}
        </ul>
    </div>
</div>


