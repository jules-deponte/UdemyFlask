def named(**kwargs):
    print(kwargs)


named(name='Alice', age=25)


# def named(name, age):
#     print(name, age)

details = {'name':'bob', 'age':15}
named(**details)

def print_nicely(**kwargs):
    named(**kwargs)
    for k, v in kwargs.items():
        print(f'{k}: {v}')


print_nicely(name='charlie', age = 23)