def add(x, y):
    return x + y

print(add(5, 7))

print((lambda x, y: x + y)(1, 2))

def double(x):
    return x * 2

seq = [1, 3, 5, 7, 9]
doubled = [double(x) for x in seq]
print(doubled)

print(list(map(double, seq)))
# map() goes through each element in seq, and applies the double() function to each element.
print(list(map(lambda x: x * 2, seq)))