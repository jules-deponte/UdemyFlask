import functools

users = {'username':'bob smith', 'access_level':'admin'}

def make_secure(access_level):
    def decorator(func):
        @functools.wraps(func)
        def secure_function(*args, **kwargs):
            if users['access_level'] == access_level:
                return func(*args, **kwargs)
            else:
                return f'No {access_level} permissions for {users["username"]}'
                
        return secure_function
    return decorator


@make_secure('admin')
def get_admin_password():
        return '1234'

@make_secure('user')
def get_user_password():
        return 'password1'


print(get_admin_password())
print(get_user_password())