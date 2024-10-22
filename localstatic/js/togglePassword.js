const toggleBtns = document.querySelectorAll('.admin-login__form__icon');

toggleBtns.forEach(btn => btn.addEventListener('click', ()=> {
    var input = document.getElementById("passwordInput"),
    invisibleIcon = document.getElementById("invisibleIcon"),
    visibleIcon = document.getElementById("visibleIcon");
    if (input.type === "password") {
      input.type = "text";
      invisibleIcon.style.display = "none";
      visibleIcon.style.display = "flex";
    } else {
      input.type = "password";
      invisibleIcon.style.display = "flex";
      visibleIcon.style.display = "none";
    }
}))