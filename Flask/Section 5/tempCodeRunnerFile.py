import sqlite3

connection = sqlite3.connect('data.db')

cursor = connection.cursor()

user_check_query = "SELECT * FROM items"
result = cursor.execute(user_check_query)
for row in result:
    print(row)