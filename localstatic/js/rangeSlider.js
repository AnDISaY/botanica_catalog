const rangeInputPrice = document.querySelector(".range-input-price input"),
rangeInputSquare = document.querySelector(".range-input-square input"),
priceInput = document.querySelector(".price-input input"),
squareInput = document.querySelector(".square-input input"),
priceRange = document.querySelectorAll(".project-filter__slider .project-filter__progress")[0],
squareRange = document.querySelectorAll(".project-filter__slider .project-filter__progress")[1];


rangeInputPrice.addEventListener("input", e =>{
    val = parseInt(rangeInputPrice.value);

    priceRange.style.width = ((val * 100)/rangeInputPrice.max) + "%";
    priceInput.value = val;
});


rangeInputSquare.addEventListener("input", e =>{
    val = parseInt(rangeInputSquare.value);

    squareRange.style.width = ((val * 100)/rangeInputSquare.max) + "%";
    squareInput.value = val;
});
