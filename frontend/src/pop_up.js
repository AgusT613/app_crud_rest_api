//
const inputs = document.querySelectorAll('.popup__content__input')
function showUserInfo(userData){
    inputs.forEach((input, index) => {
        input.setAttribute('value', userData[index])
    })
}

// HTML Elements - Edit user and close window
const editButton = document.querySelector('.popup')
const closeButton = document.querySelector('.popup__content__close__button')

// Open user editor
export function openEditor(userData){
    showUserInfo(userData)
    editButton.setAttribute('style', 'display: flex')
}

// Close user editor
closeButton.addEventListener('click', ()=>{
    editButton.setAttribute('style', 'display: none')
})