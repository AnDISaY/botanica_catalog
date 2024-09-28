document.querySelectorAll('.footer-mobile__accordeon__btn').forEach((el, index) => {
    el.addEventListener('click', () => {
        let content = el.nextElementSibling;

        if (content.style.maxHeight) {
            document.querySelectorAll('.footer-mobile__accordeon__content').forEach((el) => el.style.maxHeight = null);
            document.querySelectorAll('.footer-mobile__accordeon__btn').forEach((el) => el.classList.remove('accordeon-padding'));
            document.querySelectorAll('.footer-mobile__accordeon__btn img').forEach((el) => el.classList.remove('img-active'));
        } else {
            document.querySelectorAll('.footer-mobile__accordeon__content').forEach((el) => el.style.maxHeight = null);
            document.querySelectorAll('.footer-mobile__accordeon__btn').forEach((el) => el.classList.remove('accordeon-padding'));
            document.querySelectorAll('.footer-mobile__accordeon__btn img').forEach((el) => el.classList.remove('img-active'));
            document.querySelectorAll('.footer-mobile__accordeon__btn img')[index].classList.add('img-active');
            content.style.maxHeight = content.scrollHeight + "px";
            document.querySelectorAll('.footer-mobile__accordeon__btn')[index].classList.add('accordeon-padding');
        }
    })
})