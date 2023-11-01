---
title: Czy najbliższa niedziela jest handlowa?
---

<div class="row pt-5">
    <p class="lead">Czy najbliższa niedziela jest handlowa:</p>
    <div class="container">
        <ul>
            {% if  site.data.filtered-shopping-sundays.dates[0] != "now" %}
                <li class="list-group-item">Tak! 😄</li>
            {% else %}
              <li class="list-group-item">Nie 😔</li>
            {% endif %}
        </ul>
    </div>
</div>


