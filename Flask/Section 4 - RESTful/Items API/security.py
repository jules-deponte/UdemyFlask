from user import User

def authenticate(username, password):
    user = User.find_by_username(username)
    if user is not None and user.password == password:
        return user

def identity(payload):
    user_id = payload['identity']
    print(payload)
    return User.find_by_id(user_id)

def new_user(username, password):
    User.new_user(1,1, username, password)
    return