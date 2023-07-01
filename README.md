# Application with a RestAPI and Database

This proyect implements the standard python library sqlite3 to create a database
and connects to it through different methods and functions.

### Content

- Backend
  - FastAPI
  - SQLite3
  - [Random User API](randomuser.me)

## About the proyect

The main class `Table` , on `tables.py` , is an object in which it is being implemented
the different queries as methods and functions that can be called from the FastAPI
application.

### How it starts

> Creates a new table object named 'Users'

```
user_table = Table('Users')
```

> Creates the table 'Users' on database

```
user_table.create()
```

> Import a number of random users from [Random User API](randomuser.me)

```
user_table.import_random_users(45)
```

In addition, the data will be able to be manipulated by a frontend user
in future commits.

## About the path of the database

By default the database is named as `user.db` in the same directory as `tables.py`.
