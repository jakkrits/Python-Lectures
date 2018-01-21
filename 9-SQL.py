import sqlite3

connect = sqlite3.connect('example.db')
cursor = connect.cursor()
cursor.execute("PRAGMA foreign_keys=ON")

""" Create users table """
cursor.execute("""
CREATE TABLE users(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    email TEXT NOT NULL,
    name TEXT NOT NULL
)
""")

""" Create car table """
cursor.execute("""
    CREATE TABLE cars(
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        brand TEXT NOT NULL,
        model TEXT NOT NULL,
        owner INTEGER NOT NULL,
        FOREIGN KEY(owner) REFERENCES users(id) ON DELETE CASCADE
    )
""")

""" Create one user with two cars """
cursor.execute("INSERT INTO users VALUES(NULL, 'jakks@gmail.com', 'jakrit')")
cursor.execute("INSERT INTO cars VALUES(NULL, 'Fiat', 'Polo', 1)")
cursor.execute("INSERT INTO cars VALUES(NULL, 'BMW', 'X5', 1)")