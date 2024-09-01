const tabs = document.querySelectorAll('.tab-btn');
const all_content = document.querySelectorAll('.tab-content');

function contentInital() {
    tabs[0].classList.add('active');
    all_content[0].classList.add('active');
}

contentInital()

tabs.forEach((tab, index) => {
    tab.addEventListener('click', ()=> {
        tabs.forEach(tab => {tab.classList.remove('active')});
        tab.classList.add('active');
        all_content.forEach(content => {content.classList.remove('active')});
        all_content[index].classList.add('active');
    })
    
})

// const leng = tabs.length

// function tabChange(index) {
//     if (index >= leng) index = 0;
//     if (index < 0) index = leng - 1;

//     tabs.forEach(tab => {tab.classList.remove('active')});
//     tabs[index].classList.add('active');
//     all_content.forEach(content => {content.classList.remove('active')});
//     all_content[index].classList.add('active');


//     document.addEventListener('keydown', function(event) {
//         if(event.key === "ArrowLeft") {
//             tabChange(index - 1);
//         }
//         if(event.key === "ArrowRight") {
//             tabChange(index + 1);
//         }
//     });
// }

// tabChange(0)