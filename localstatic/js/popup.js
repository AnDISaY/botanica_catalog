const popupLink = document.querySelector('.popup-link');
const body = document.querySelector('body');

let unlock = true;

const timeout = 800;



document.addEventListener('keydown', function (e) {
    if (e.which === 27) {
        const popupActive = document.querySelector('.popup.open');
        popupClose(popupActive);
    }
})

function bodyLock() {
    body.classList.add('lock');

    unlock = false;
    setTimeout(function () {
        unlock = true;
    },  timeout);
}

function bodyUnlock() {
    setTimeout(function () {
        body.classList.remove('lock');
    },  timeout)

    unlock = false;
    setTimeout(function () {
        unlock = true;
    },  timeout)
}


function popupOpen(popup) {
    if (popup && unlock) {
        const popupActive = document.querySelector('.popup.open');
        if (popupActive) {
            popupClose(popupActive, false);
        } else {
            bodyLock();
        }
    }
    popup.classList.add('open');
    popup.addEventListener('click', function (e) {
        if (!e.target.closest('.popup__container')) {
            popupClose(e.target.closest('.popup'));
        }
    });
}

function popupClose(popupActive, doUnlock=true) {
    if (unlock) {
        popupActive.classList.remove('open');
        if (doUnlock) {
            bodyUnlock();
        }
    }
}


popupLink.addEventListener('click', function (e) {
    let popupName = popupLink.getAttribute('href').replace('#', '');
    let currentPopup = document.getElementById(popupName);
    // console.log(currentPopup)
    popupOpen(currentPopup)
    e.preventDefault();
})

const popupCloseEl = document.querySelectorAll('.close-popup');
popupCloseEl.forEach(el => {
    el.addEventListener('click', function (e) {
        popupClose(el.closest('.popup'));
        e.preventDefault();
    })
})