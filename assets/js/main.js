function activateBurger() {
    const burger = document.querySelector('.navbar-burger');
    if (!burger) {
        console.error('Burger element not found');
        return;
    }

    const menuId = burger.dataset.target;
    const menu = document.getElementById(menuId);
    if (!menu) {
        console.error('Menu element not found');
        return;
    }

    function toggleMenu(event) {
        event.preventDefault();
        burger.classList.toggle('is-active');
        menu.classList.toggle('is-active');
    }

    burger.addEventListener('click', toggleMenu);
    burger.addEventListener('touchstart', toggleMenu);

    console.log('Burger menu activated');
}

document.addEventListener('DOMContentLoaded', activateBurger);
window.onload = activateBurger;
