def divide(numerator, denominator):
    if denominator == 0:
        raise ZeroDivisionError('Denominator cannot be 0')
    return numerator / denominator

def calculate(*values, operator):
    return operator(*values)

result = calculate(20, 4, operator=divide)
print(result)
print('---------------------------------------------------')

def search(seq, expected, finder):
    for elem in seq:
        if finder(elem) == expected:
            return elem
    
    raise RuntimeError(f'Could not fine an element with {expected}')

friends = [
    {'name':'alice smith', 'age':24},
    {'name':'Ian Steele', 'age':30},
    {'name':'rob jones', 'age':27}
]

def get_friend_name(friend):
    return friend['name']

print(search(friends, 'alice smith', get_friend_name))
