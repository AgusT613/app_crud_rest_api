// HTML Elements - Edit user and close window
const editButton = document.querySelector('.popup')
const closeButton = document.querySelector('.popup__content__close__button')

// Open user editor
export function openEditor(){
    editButton.setAttribute('style', 'display: flex')
}

// Close user editor
closeButton.addEventListener('click', ()=>{
    editButton.setAttribute('style', 'display: none')
})