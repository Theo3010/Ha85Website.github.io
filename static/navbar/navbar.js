const template = document.querySelector(".navbar__item-template");
const navbarContent = document.querySelector(".navbar__content");
const navbarContainer = document.querySelector(".navbar__container");
const WebsiteNames = ["Forside", "Fodbold", "Håndbold", "Badminton", "Esport", "Gymnastik og Dans", "Høvdingebold", "Volleyball", "Løb", "Sponoser", "Om Ha85"];

WebsiteNames.forEach(Names => {
    const cloneNode = template.content.cloneNode(true);
    const navbarItem = cloneNode.children[0];
    
    navbarItem.children[0].textContent = Names;
    navbarItem.children[0].href = "/" + Names.toLowerCase();
    
    navbarContent.appendChild(cloneNode);
});

const navbarHamburger = document.querySelector(".navbar__hamburger");
navbarHamburger.addEventListener("click", function() {
    navbarContainer.classList.toggle("navbar__container--open");
});

