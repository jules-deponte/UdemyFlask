users = {'username':'bob smith', 'access_level':'guest'}

def get_admin_password():
    return '1234'

def make_secure(func):
    def secure_function():
        if users['access_level'] == 'admin':
            return func()
        else:
            return f'No admin permissions for {users["username"]}'
    return secure_function

get_admin_password = make_secure(get_admin_password)
print(get_admin_password())