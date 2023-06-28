import sqlite3
import os

# DB folder path
abs_path = os.path.abspath(__file__)
db_folder = os.path.split(abs_path)[0]
db_path = os.path.join(db_folder, 'user.db')

def create_table(table_name):
    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()
        query = f'''
            CREATE TABLE IF NOT EXISTS {table_name} (
                "UserId" INTEGER,
                "FirstName" TEXT NOT NULL,
                "LastName" TEXT NOT NULL,
                "Age" INTEGER NOT NULL,
                "Email" TEXT NOT NULL,
                "Country" TEXT NOT NULL,
                PRIMARY KEY ("UserId" AUTOINCREMENT)
            );
        '''
        cursor.execute(query)
        conn.commit()
        print(f'Table {table_name} created')

def delete_table(table_name: str):
    try:
        with sqlite3.connect(db_path) as conn:
            cursor = conn.cursor()
            query = f'''
                DROP TABLE {table_name}
            '''
            cursor.execute(query)
            print(f'Table {table_name} deleted')
            conn.commit()
    except:
        print('No table found')
        print('Error from DELETE_TABLE function')

def delete_from_table(table_name: str):
    try:
        with sqlite3.connect(db_path) as conn:
            cursor = conn.cursor()
            query = f'''
                DELETE FROM {table_name}
            '''
            cursor.execute(query)
            conn.commit()
            print(f'Deleted everything from {table_name}')
    except:
        print('Error from DELETE_FROM_TABLE function')

def fetch_table_data(table_name: str):
    try:
        with sqlite3.connect(db_path) as conn:
            cursor = conn.cursor()
            query = f'''
                SELECT * FROM {table_name}
            '''
            result = cursor.execute(query)
            return result.fetchall()
    except:
        print('No table found')
        print('Error from FETCH_TABLE_DATA function')

def insert_data_to(table_name: str, data_list: list):
    try:
        with sqlite3.connect(db_path) as conn:
            cursor = conn.cursor()
            query = f'''
                INSERT INTO {table_name} VALUES (?, ?, ?, ?, ?, ?)
            '''
            cursor.executemany(query, data_list)
            conn.commit()
            print('Added values')
    except:
        print('Error ocurred')
        print('Error from INSERT_DATA_TO function')

def insert_registry(table_name: str, body: dict):
    try:
        with sqlite3.connect(db_path) as conn:
            cursor = conn.cursor()
            query = f'''
                INSERT INTO {table_name} (FirstName, LastName, Age, Email, Country)
                VALUES (
                    '{body['firstName']}',
                    '{body['lastName']}',
                    {body['age']},
                    '{body['email']}',
                    '{body['country']}'
                )
            '''
            cursor.execute(query)
            conn.commit()
            print("New user created successfully")
            return 200
    except:
        print("Error from INSERT_REGISTRY function")

if __name__ == '__main__':
    pass