const rangeInputPrice = document.querySelectorAll(".range-input-price input"),
priceInput = document.querySelectorAll(".price-input input"),
range = document.querySelectorAll(".project-filter__slider .project-filter__progress")[0];
let priceGap = 500000;

priceInput.forEach(input =>{
    input.addEventListener("input", e =>{
        let minPrice = parseInt(priceInput[0].value),
        maxPrice = parseInt(priceInput[1].value);
        
        if((maxPrice - minPrice >= priceGap) && maxPrice <= rangeInputPrice[1].max){
            if(e.target.className.split(" ")[2] === "input-min"){
                rangeInputPrice[0].value = minPrice;
                range.style.left = ((minPrice / rangeInputPrice[0].max) * 100) + "%";
            }else{
                rangeInputPrice[1].value = maxPrice;
                range.style.right = 100 - (maxPrice / rangeInputPrice[1].max) * 100 + "%";
            }
        }
    });
});

rangeInputPrice.forEach(input =>{
    input.addEventListener("input", e =>{
        let minVal = parseInt(rangeInputPrice[0].value),
        maxVal = parseInt(rangeInputPrice[1].value);

        if((maxVal - minVal) < priceGap){
            if(e.target.className === "range-min"){
                rangeInputPrice[0].value = maxVal - priceGap;
            }else{
                rangeInputPrice[1].value = minVal + priceGap;
            }
        }else{
            priceInput[0].value = minVal;
            priceInput[1].value = maxVal;
            range.style.left = ((minVal / rangeInputPrice[0].max) * 100) + "%";
            range.style.right = 100 - (maxVal / rangeInputPrice[1].max) * 100 + "%";
        }
    });
});


const rangeInputSquare = document.querySelectorAll(".range-input-square input"),
squareInput = document.querySelectorAll(".square-input input"),
range2 = document.querySelectorAll(".project-filter__slider .project-filter__progress")[1];
let priceGap2 = 500;

squareInput.forEach(input =>{
    input.addEventListener("input", e =>{
        let minPrice = parseInt(squareInput[0].value),
        maxPrice = parseInt(squareInput[1].value);
        
        if((maxPrice - minPrice >= priceGap2) && maxPrice <= rangeInputSquare[1].max){
            if(e.target.className.split(" ")[2] === "input-min2"){
                rangeInputSquare[0].value = minPrice;
                range2.style.left = ((minPrice / rangeInputSquare[0].max) * 100) + "%";
            }else{
                rangeInputSquare[1].value = maxPrice;
                range2.style.right = 100 - (maxPrice / rangeInputSquare[1].max) * 100 + "%";
            }
        }
    });
});

rangeInputSquare.forEach(input =>{
    input.addEventListener("input", e =>{
        let minVal = parseInt(rangeInputSquare[0].value),
        maxVal = parseInt(rangeInputSquare[1].value);

        if((maxVal - minVal) < priceGap2){
            if(e.target.className === "range-min2"){
                rangeInputSquare[0].value = maxVal - priceGap2;
            }else{
                rangeInputSquare[1].value = minVal + priceGap2;
            }
        }
        else{
            squareInput[0].value = minVal;
            squareInput[1].value = maxVal;
            range2.style.left = ((minVal / rangeInputSquare[0].max) * 100) + "%";
            range2.style.right = 100 - (maxVal / rangeInputSquare[1].max) * 100 + "%";
        }
    });
});