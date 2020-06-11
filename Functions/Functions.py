# def hello():
#     print("hello")

# hello()

# def age_in_seconds():
#     age = int(input('Enter age: '))
#     print(age * 365.25 * 24 * 3600)

# age_in_seconds()
friends = ['alice', 'bob']

def add_freind():
    name = input('Enter Name: ')
    f = friends + [name] # This way, you can use global variables within a user defined function.
    print(f)

add_freind()