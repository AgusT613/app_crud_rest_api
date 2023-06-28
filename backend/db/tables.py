import sqlite3
from os.path import abspath, split, join
import requests
import pandas as pd

class Table():
    def __init__(self, table_name: str):
        self.table_name = table_name
        # DB folder path
        db_folder = split(abspath(__file__))[0]
        self.path = join(db_folder, 'user.db')

    # Connection to database
    @staticmethod
    def conn(query: str, path: str):
        with sqlite3.connect(path) as conn:
            cursor = conn.cursor()
            cursor.execute(query)
            conn.commit()
    # Fetch all content
    @staticmethod
    def fetch_all(query: str, path: str):
        with sqlite3.connect(path) as conn:
            cursor = conn.cursor()
            result = cursor.execute(query)
            return result.fetchall()
    # Operate many data with a list of tuples
    @staticmethod
    def execute_many(query: str, path: str, data: list):
        with sqlite3.connect(path) as conn:
            cursor = conn.cursor()
            cursor.executemany(query, data)
            conn.commit()

    # Create new table
    def create(self):
        query = f'''
            CREATE TABLE IF NOT EXISTS {self.table_name} (
                "UserId" INTEGER,
                "FirstName" TEXT NOT NULL,
                "LastName" TEXT NOT NULL,
                "Age" INTEGER NOT NULL,
                "Email" TEXT NOT NULL,
                "Country" TEXT NOT NULL,
                PRIMARY KEY ("UserId" AUTOINCREMENT)
            )
        '''
        try:
            Table.conn(query, self.path)
            print(f'Table {self.table_name} created successfully!')
        except Exception as error:
            print(f'Create table error ----> {error}')

    # Delete a table
    def drop(self):
        query = f'DROP TABLE {self.table_name}'
        query_2 = f'UPDATE sqlite_sequence SET seq = 0 WHERE name = "{self.table_name}"'
        try:
            Table.conn(query, self.path)
            print(f'Table {self.table_name} deleted completely')
            Table.conn(query_2, self.path)
            print(f'SQLite sequence was reset to 0')
        except Exception as error:
            print(f'Delete table error ----> {error}')

    # Select everything from table
    def select_everything_from(self) -> list:
        query = f'SELECT * FROM {self.table_name}'
        try:
            # Result is a list of tuples
            result = Table.fetch_all(query, self.path)
        except Exception as error:
            return print(f'Could not fetch data ----> {error}')
        # Convert to list of dicts
        user_list = list()
        for person in result:
            data = {
                "id": person[0],
                "firstName": person[1],
                "lastName": person[2],
                "age": person[3],
                "email": person[4],
                "country": person[5]
            }
            user_list.append(data)
        print('---- DATA ----')
        df = pd.DataFrame(user_list)
        print(df)
        return user_list

    # Delete everything from table
    def delete_everything_from(self):
        query = f'DELETE FROM {self.table_name}'
        try:
            Table.conn(query, self.path)
            print(f'Data from table {self.table_name} was deleted')
        except Exception as error:
            print(f'Could not delete data. Error ----> {error}')
    
    def insert_registry(self, data: dict):
        query = f'''
            INSERT INTO {self.table_name} (FirstName, LastName, Age, Email, Country)
            VALUES (
                '{data['firstName']}',
                '{data['lastName']}',
                {data['age']},
                '{data['email']}',
                '{data['country']}'
            )
        '''
        try:
            Table.conn(query, self.path)
            message = 'New registry added successfully'
            print(message)
            return message
        except Exception as error:
            message = 'Could not insert new registry'
            print(f'{message} ----> {error}')
            return message
    
    def import_random_users(self, number_of_users: str):
        # Random users API
        users_api_link = f'https://randomuser.me/api/?results={number_of_users}'
        response = requests.get(users_api_link).status_code
        # Evaluate status code
        if response != 200: return print(f'Status code: {response}')
        print(f'Status code: {response}')
        # JSON
        content = requests.get(users_api_link).json()
        user_list = list()
        for person in content['results']:
            data = (
                None,
                person["name"]["first"],
                person["name"]["last"],
                person["dob"]["age"],
                person["email"],
                person["location"]["country"]
            )
            user_list.append(data)
        print('Data was created')
        # Query to insert many data
        query = f'INSERT INTO {self.table_name} VALUES (?, ?, ?, ?, ?, ?)'
        # Insert with executemany. Must be a list of tuples
        try:
            Table.execute_many(query, self.path, user_list)
            print(f'Data was added to table {self.table_name} successfully')
        except Exception as error:
            print(f'Could not add data ----> {error}')
    
# TEST
if __name__ == '__main__':
    user_table = Table('Users')
    user_table.create()
    user_table.import_random_users(45)