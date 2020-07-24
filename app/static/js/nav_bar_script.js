//Script that makes title of current location bold
const currentLocation = location.href;
const menuItem = document.querySelectorAll('.nav-link');
const menuLength = menuItem.length
for (let i = 0; i < menuLength; i++) {
    //if (menuItem[i].href === currentLocation) {
    //    menuItem[i].className += " nav-link-active"
    //}
    if (menuItem[i].href.split('/').pop() === currentLocation.split('/').pop()) {
        menuItem[i].className += " nav-link-active"
    }

    //console.log('current    ' + currentLocation.split('/').pop())
    //console.log('one of links    ' + menuItem[i].href.split('/').pop())
}


//Script for adaptive burger menu
const navSlide = () => {
    const burger = document.querySelector('.burger');
    const nav = document.querySelector('.nav-links');
    const navLinks = document.querySelectorAll('.nav-links li')


    burger.addEventListener('click', () => {
        //Toggle nav
        nav.classList.toggle('nav-active');

        //Animate links
        navLinks.forEach((link, index) => {
            if(link.style.animation){
                link.style.animation = ''
            }else{
                link.style.animation = `navLinkFade 0.5s ease forwards ${index/7 + 0.5}s`;

            }
        });

        //Burger animation
        burger.classList.toggle('toggle');
    });
}

navSlide()