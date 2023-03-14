/*=============== SHOW MENU ===============*/
const navMenu = document.getElementById('nav-menu'),
    navToggle = document.getElementById('nav-toggle'),
    navClose = document.getElementById('nav-close')

/*===== MENU SHOW =====*/
if (navToggle) {
    navToggle.addEventListener('click', () => {
        navMenu.classList.add('show-menu')
    })
}

/*===== MENU HIDDEN =====*/
if (navClose) {
    navClose.addEventListener('click', () => {
        navMenu.classList.remove('show-menu')
    })
}

/*=============== REMOVE MENU MOBILE ===============*/
const navLink = document.querySelectorAll('.nav__link')

function linkAction() {
    const navMenu = document.getElementById('nav-menu')
    navMenu.classList.remove('show-menu')
}
navLink.forEach(n => n.addEventListener('click', linkAction))

/*=============== SCROLL REVEAL ANIMATION ===============*/
const sr = ScrollReveal({
    distance: '50px',
    duration: 3000,
})

sr.reveal(``, { origin: 'bottom' })
sr.reveal(`.h-lk`, { origin: 'right', delay: 600 })
sr.reveal(`.pray`, { origin: 'left', distance: '100px', delay: 200 })
sr.reveal(`.text-left`, { origin: 'right', distance: '100px', delay: 200 })
sr.reveal(``, { origin: 'top', delay: 300 })
sr.reveal(`.text__content-box1,.h-t,.box,.box2,.grid-item1,.item-img`, { origin: 'top', distance: '50px', delay: 100 })