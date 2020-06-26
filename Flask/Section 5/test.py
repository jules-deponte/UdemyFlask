import sqlite3

connection = sqlite3.connect('data.db')

cursor = connection.cursor()

user_check_query = "SELECT * FROM items"
result = cursor.execute(user_check_query)
for row in result:
    print(row)
if result:
    connection.close()
    print("{'message':'Username already exists.'}")

create_table = "CREATE TABLE users (ID int, username text, password text)"
cursor.execute(create_table)

user = (1, 'bob', 'asdf')

insert_query = "INSERT INTO users VALUES (?, ?, ?)"
cursor.execute(insert_query, user)

users = [
    (2, 'alice', 'qwerty'),
    (3, 'charlie', 'zxcv')
]

cursor.executemany(insert_query, users)

select_qurery = "SELECT * FROM users"
for row in cursor.execute(select_qurery):
    print(row)

connection.commit()

connection.close()