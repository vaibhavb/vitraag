function activateBurger() {
    const burger = document.querySelector('.navbar-burger');
    if (!burger) {
        console.error('Burger element not found');
        return;
    }

    if (burger.dataset.burgerActivated) {
        return;
    }
    burger.dataset.burgerActivated = 'true';

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

    // Only listen for 'click' - modern touch browsers already fire a click
    // event after tap, so also binding 'touchstart' caused the menu to open
    // and immediately close again (touchstart opens it, the synthesized
    // click that follows toggles it shut).
    burger.addEventListener('click', toggleMenu);

    console.log('Burger menu activated');
}

document.addEventListener('DOMContentLoaded', activateBurger);
window.onload = activateBurger;
