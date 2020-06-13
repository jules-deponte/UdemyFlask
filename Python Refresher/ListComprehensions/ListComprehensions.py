numbers = [1, 3, 5]
doubled = []

for num in numbers:
    doubled.append(num * 2)

print(doubled)

# List comprehension:
doubled = [num * 2 for num in numbers]

print(doubled)

#-----------#-----------#-----------#-----------
friends = ['alice', 'anne', 'amy']

# Find the names that start with an 'a'
starts_a = [f for f in friends if f[0] == 'a']
print(starts_a)

print(friends == starts_a)
print(friends is starts_a)
print(id(friends))

