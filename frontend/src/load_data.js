// Creates one table row element
function createTableRow(id, firstName, lastName, age, email, country){
    // ----------------------------------------
    // Row container
    let tableRow = document.createElement('tr')
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

    // ----------------------------------------
    // Apend the document fragment to the table row container
    tableRow.appendChild(fragment)
    return tableRow
}

// Load table from database
async function getContentDatabase(){
    // ----------------------------------------
    // Connection to database
    const backend = 'http://127.0.0.1:8000'
    // Table body element container
    let tableBody = document.querySelector('.content__table__body')

    // ----------------------------------------
    // Server response
    let server_response = await fetch(backend + '/users')
    let status = server_response.status
    // Status code
    if (status !== 200) {
        return console.error(`Status code ${status}. The backend is not available now`);
    }
    console.log(`Status code ${status}. The backend was setup without issues`);

    // ----------------------------------------
    // If everything works OK, then displays the content
    let content = await server_response.json()
    let fragment = document.createDocumentFragment()
    // For each user create a table row
    content.forEach(user => {
        let id = user['id']
        let firstName = user['firstName']
        let lastName = user['lastName']
        let age = user['age']
        let email = user['email']
        let country = user['country']

        let tableRow = createTableRow(id, firstName, lastName, age, email, country)
        fragment.appendChild(tableRow)
    })

    // ----------------------------------------
    tableBody.appendChild(fragment)
}

getContentDatabase()