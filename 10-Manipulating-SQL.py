import sqlite3
connection = sqlite3.connect('example.db')
cursor = connection.cursor()
cursor.execute("PRAGMA foreign_keys=ON")

rows = list(cursor.execute("SELECT * FROM users"))
print(rows)