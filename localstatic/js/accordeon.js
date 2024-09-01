document.querySelectorAll('.footer-mobile__accordeon__btn').forEach((el) => {
    el.addEventListener('click', () => {
        let content = el.nextElementSibling;

        if (content.style.maxHeight) {
            document.querySelectorAll('.footer-mobile__accordeon__content').forEach((el) => el.style.maxHeight = null);
        } else {
            document.querySelectorAll('.footer-mobile__accordeon__content').forEach((el) => el.style.maxHeight = null);
            content.style.maxHeight = content.scrollHeight + "px";
        }
    })
})