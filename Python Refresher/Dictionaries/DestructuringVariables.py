t = 5, 11
x, y = t

print(x, y)

attendance = {'alice': 96, 'bob':80, 'charlie':100}

# for student in attendance:
#     print(attendance[student])

# for k, v in attendance.items():
#     print(k, v)

print(list(attendance.items()))

lst = [1, 2, 3, 4, 5]

head, *tail = lst
print(head, tail)