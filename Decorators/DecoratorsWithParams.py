import functools

users = {'username':'bob smith', 'access_level':'admin'}


def make_secure(func):
    @functools.wraps(func)
    def secure_function(*args, **kwargs):
        if users['access_level'] == 'admin':
            return func(*args, **kwargs)
        else:
            return f'No admin permissions for {users["username"]}'
    return secure_function


@make_secure
def get_password(panel):
    if panel == 'admin':
        return '1234'
    if panel == 'billing':
        return 'password1'

# get_admin_password = make_secure(get_admin_password)
print(get_password('billing'))