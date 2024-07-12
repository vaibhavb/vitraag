
document.addEventListener('DOMContentLoaded', () => {
    var burger = document.querySelector('.navbar-burger');
    var menu = document.querySelector('#'+burger.dataset.target);
    burger.addEventListener('click', function() {
        burger.classList.toggle('is-active');
        menu.classList.toggle('is-active');
    });
    burger.addEventListener('touchstart', function(e) {
    e.preventDefault(); // Prevent default touch behavior
    console.log('Burger touched');
    burger.classList.toggle('is-active');
    menu.classList.toggle('is-active');
}, false);
  });
