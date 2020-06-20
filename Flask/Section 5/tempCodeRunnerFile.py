import sqlite3

connection = sqlite3.connect('data.db')

cursor = connection.cursor()

for row in cursor.execute("SELECT * FROM users"):
    print(row)