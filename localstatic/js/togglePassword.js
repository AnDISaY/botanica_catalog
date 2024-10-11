toggleBtn = document.querySelector('.admin-login__form__icon');

toggleBtn.addEventListener('click', ()=> {
    var input = document.getElementById("passwordInput");
    if (input.type === "password") {
      input.type = "text";
    } else {
      input.type = "password";
    }
})