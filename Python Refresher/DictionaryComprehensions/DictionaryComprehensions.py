users = [
    (0, 'alice', 'password1'),
    (1, 'bob', 'Strongpassword1'),
    (2, 'charlie', 'asdf')
]

mapping = {user[1]: user for user in users}

print(mapping)

user_input = input('Enter your name: ')
pass_input = input('Enter your password: ')

_, name, password = mapping[user_input]
if password == pass_input:
    print('correct')
else:
    print('incorrect')