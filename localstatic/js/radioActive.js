const inputRadio = document.querySelectorAll('.project-filter__radio-wrapper input'),
labelRadio = document.querySelectorAll('.project-filter__radio');

labelRadio.forEach((label, index) => {
    label.addEventListener('click', ()=> {
        labelRadio.forEach(label => {label.classList.remove('radio-active')});
        label.classList.add('radio-active');
        inputRadio[index].checked = true;
    })
})