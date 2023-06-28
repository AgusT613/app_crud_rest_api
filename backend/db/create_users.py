import requests
import pandas as pd
from database import create_table, delete_table, insert_data_to

def response(link: str):
    return requests.get(link)

def response_content(link: str):
    return requests.get(link).json()

# Create a JSON file with users
def create_users(number_of_users: int):
    # Random users API
    users_api_link = f'https://randomuser.me/api/?results={number_of_users}'
    # Evalute status code
    try:
        print(f'Status code: {response(users_api_link).status_code}')
    except Exception:
        return print(f'Status code: {response(users_api_link).status_code}')
    # User list contains tuples of users
    user_list = list()
    for person in response_content(users_api_link)["results"]:
        data = (
            None,
            person["name"]["first"],
            person["name"]["last"],
            person["dob"]["age"],
            person["email"],
            person["location"]["country"]
        )
        user_list.append(data)
    # Create data frame to display the content
    df = pd.DataFrame(user_list)
    # Insert to database
    try:
        insert_data_to("Users", user_list)
        print(f'Inserted {number_of_users} new users')
        return user_list, df
    except:
        print('Error from UPLOAD_DATA_TO_DB')

# Script
if __name__ == '__main__':
    create_table("Users")
    create_users(5)