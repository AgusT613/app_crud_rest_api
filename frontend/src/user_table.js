import { openEditor } from './pop_up'

// Create three dots icon (edit user)
function createIcon(userData){
    // ----------------------------------------
    // Main Container
    let container = document.createElement('td')
    let containerClassName = 'content__table__body__edit'
    container.setAttribute('class', containerClassName)
    // Edit user button event listener
    userData.shift()
    container.addEventListener('click', ()=>{
        openEditor(userData)
    })
    // ----------------------------------------
    // Edit user icon
    let editIcon = document.createElement('span')
    let editIconClassName = 'content__table__body__icon'
    editIcon.setAttribute('class', editIconClassName)
    // ----------------------------------------
    // Append icon to main container
    container.appendChild(editIcon)
    return container
}

// Create one table row element
export function createTableRow(id, firstName, lastName, age, email, country){
    // ----------------------------------------
    // Row container
    let tableRow = document.createElement('tr')
    let tableRowClassName = 'content__table__body__user__data'
    tableRow.setAttribute('class', tableRowClassName)
    // Data colums
    let userData = [id, firstName, lastName, age, email, country]

    // ----------------------------------------
    // Document fragment
    let fragment = document.createDocumentFragment()
    // Fill each table cell and append to the document fragment
    userData.forEach(data => {
        let dataCellElement = document.createElement('td')
        dataCellElement.textContent = data
        fragment.appendChild(dataCellElement)
    })
    // Put the edit icon on the data cell
    let editIcon = createIcon(userData)
    fragment.appendChild(editIcon)

    // ----------------------------------------
    // Apend the document fragment to the table row container
    tableRow.appendChild(fragment)
    return tableRow
}