---
title: Czy dziś jest niedziela handlowa
---

<h2 class="display-4 lh-1  text-center">Czy dziś jest niedziela handlowa?</h2>
<h1 id="is-shopping-allowed" class="display-4 fw-bold lh-1 pt-4 text-center">Nie</h1>
<div class="row pt-5">
    <p class="lead">Najbliższe niedziele handlowe:</p>
    <div class="container">
        <ul id="next-sunday" class="list-group">
            {% var = 0 %}
            {% for sunday in site.data.niedziele-handlowe %}
                {% if var == 3 %}
                    {% break %}
                {% else %}
                    {% var | plus: 1 %}
                    {{ sunday.date | date: "%d.%m.%Y"}}
                {% endif %}
            {% endfor %}
        </ul>
    </div>
</div>
<script type="text/javascript">
    const date = new Date();
    let day = date.getDate();
    let month = date.getMonth() + 1;
    let year = date.getFullYear();
    let currentDate = `${month}/${day}/${year}`;
    const shoppingAllowed = ['12/11/2022','12/18/2022','1/29/2023','4/2/2023','4/30/2023','6/25/2023','8/27/2023','12/17/2023','12/24/2023','1/28/2024','3/24/2024','4/28/2024','6/30/2024','8/25/2024','12/15/2024','12/22/2024']

    if (shoppingAllowed.includes(currentDate)){
        let isAllowed = document.getElementById('is-shopping-allowed');
        isAllowed.innerHTML = isAllowed.innerHTML.replace("Nie", "Tak");
    }

    let counter = 0;
    shoppingAllowed.forEach(i => {
        let nextSundayDate = new Date(i);
        if (date < nextSundayDate){
            if (counter < 3){
                let currentDate = convertDate(nextSundayDate);
                let node = document.createElement("li");
                let textnode = document.createTextNode(currentDate);
                node.appendChild(textnode);
                node.classList.add("list-group-item");
                document.getElementById("next-sunday").appendChild(node);
            }
            counter += 1;
        }
    })

    function convertDate(nextSundayDate) {
        const months = ['01','02','03','04','05','06','07','08','09','10','11','12',]
        let day = nextSundayDate.getDate();
        let month = months[nextSundayDate.getMonth()];
        let year = nextSundayDate.getFullYear();
        return `${day}.${month}.${year}`;
    }
</script>