import sqlite3

class User:
    def __init__(self, _id, username, password):
        self.id = _id
        self.username = username
        self.password = password

    @classmethod
    def find_by_username(cls, username):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        users_query = "SELECT * FROM users WHERE username = ?"
        result = cursor.execute(users_query, (username,))   # query parameter needs to be in the form of a tuple.
                                                            # The way to make a single value tuple is (value,)
        row = result.fetchone()
        if row is not None:
            user = cls(*row)
        else:
            user = None

        connection.close()
        return user

    @classmethod
    def find_by_id(cls, _id):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        users_query = "SELECT * FROM users WHERE id = ?"
        result = cursor.execute(users_query, (_id,))   # query parameter needs to be in the form of a tuple.
                                                        # The way to make a single value tuple is (value,)
        row = result.fetchone()
        if row is not None:
            user = cls(*row)
        else:
            user = None

        connection.close()
        return user

    def new_user(self, _id, username, password):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        insert_query = "INSERT INTO users (username, password) VALUES (?, ?)"
        cursor.execute(insert_query, (username, password))

        connection.commit()
        connection.close()