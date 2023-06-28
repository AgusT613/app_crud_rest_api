import sqlite3
from os.path import abspath, split, join

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
            return print(f'Table {self.table_name} created successfully!')
        except Exception as error:
            return print(f'Create table error ----> {error}')
    # Delete a table
    def drop(self):
        query = f'DROP TABLE {self.table_name}'
        try:
            Table.conn(query, self.path)
            return print(f'Table {self.table_name} deleted completely')
        except Exception as error:
            return print(f'Delete table error ----> {error}')
    # Select everything from table
    def select_everything_from(self):
        pass
    
    def delete_everything_from(self):
        pass
    
    def insert_into_table_values(self):
        pass
    
    def insert_registry(self):
        pass
    
    def import_random_users(self, number_of_users: str):
        pass
    
# TEST
if __name__ == '__main__':
    
    user_table = Table('Test')
    user_table.create()