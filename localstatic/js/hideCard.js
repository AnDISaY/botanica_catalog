const showMore = document.querySelector('.project-apartments__show-more');

function showCard() {
    const showMore = document.querySelector('.project-apartments__show-more');
    var cards = Array.from(document.querySelectorAll('.hide-content'));
    let count = 0;

    for (const card of cards.slice(count, count+6)) {
        card.classList.remove("hide-content");
        card.classList.add("show-content");
    }

    showMore.remove();
    if (cards.slice(count).length > 6) {
        const showMoreEl = document.createElement('div');
        showMoreEl.classList.add('project-apartments__show-more');
        showMoreEl.classList.add('show-content');
        const showMoreSpan = document.createElement('span');
        showMoreSpan.innerHTML = "Посмотреть больше вилл";
        showMoreEl.appendChild(showMoreSpan);
        document.querySelector('.project-apartments__wrapper').appendChild(showMoreEl);
        const showMore2 = document.querySelector('.project-apartments__show-more');
        showMore2.addEventListener('click', showCard);
    }

    count += 6;
}

showMore.addEventListener('click', showCard);