let menu = document.querySelector('#menu-btn');
let navbar = document.querySelector('.navbar');

menu.onclick = () =>{
    menu.classList.toggle('fa-times');
    navbar.classList.toggle('active');
}

window.onscroll = () =>{
    menu.classList.remove('fa-times');
    navbar.classList.remove('active');
}


// changing navbar when scrolled
window.addEventListener('scroll', () => {
    document.querySelector('fas').classList.toggle
    ('window-scroll', window.scrollY > 0)
})

const menu = document.querySelector(".navbar");
const menuBtn = document.querySelector("#open-menu-btn");
const closeBtn = document.querySelector("#close-menu-btn");

menuBtn.addEventListener('click', () => {
    menu.style.display  = "flex";
    closeBtn.style.display = "inline-block";
    menuBtn.style.display = "none";
})

const closeNav = () =>{
    menu.style.display  = "none";
    closeBtn.style.display = "none";
    menuBtn.style.display = "inline-block";
}

closeBtn.addEventListener('click', closeNav)