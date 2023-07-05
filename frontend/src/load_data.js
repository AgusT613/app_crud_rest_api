import { createTableRow } from './user_table'
 
// Connection to database
const localhost = 'http://127.0.0.1:8000'
// Table body element container
let tableBody = document.querySelector('.content__table__body')

// Load table from database
async function fetchDatabase(){
    try {
        // Database connection
        const server = await fetch(localhost + '/users')
        let data = await server.json()

        let fragment = document.createDocumentFragment()
        // For each user create a table row
        data.forEach(user => {
            let id = user['id']
            let firstName = user['firstName']
            let lastName = user['lastName']
            let age = user['age']
            let email = user['email']
            let country = user['country']
        
            let tableRow = createTableRow(id, firstName, lastName, age, email, country)
            fragment.appendChild(tableRow)
        })
        // Append to table container
        tableBody.appendChild(fragment)
    }
    catch (error) {
        if (error instanceof TypeError) {
            let message = `The user data could not be imported due to the failed connection: ${error}`
            console.error(message);
        }
    }
}

fetchDatabase()