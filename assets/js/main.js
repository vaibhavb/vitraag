
document.addEventListener('DOMContentLoaded', () => {
    var burger = document.querySelector('.navbar-burger');
    var menu = document.querySelector('#'+burger.dataset.target);
    burger.addEventListener('click', function() {
        burger.classList.toggle('is-active');
        menu.classList.toggle('is-active');
    });
  });