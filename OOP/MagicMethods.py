class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# This is the string that is printed when printing the instance of the class.
    def __str__(self):
        return f'{self.name} is {self.age} years old.'


# This is used to print out an unambiguous representation of the class so others can reproduce it.
    def __repr__(self):
        return f'<Person("{self.name}", {self.age})>'


bob = Person('Bob', 35)

print(bob.__repr__())