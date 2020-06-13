
def mulitply(*args):
    total = 1
    for arg in args:
        total *= arg

    return total
    

print(mulitply(1,2,3))

# Destructuring variable using *
def add(x, y):
    return x + y

nums = [3, 5]

print(add(*nums))
print(mulitply(*nums))

# using ** will deconstruct the dictionary into its key-value pairs
nums = {'x':3, 'y':5}
print(add(**nums))

# With this syntax, you can pass in many different postional arguments and you must innclude a named argument.
def apply(*args, operator):
    if operator == '*':

        return mulitply(*args)
    elif operator == '+':
        return sum(args)
    else:
        print('No valid operator provided')
        
print(apply(1,4,7, operator = '*'))