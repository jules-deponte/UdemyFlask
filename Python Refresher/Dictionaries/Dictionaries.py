f_ages = {'alice': 24, 'bob':15, 'charlie':45}

print(f_ages['alice'])

f_ages['doug'] = 20

print(f_ages)

friends = [
    {'name': 'alice', 'age':24},
    {'name': 'bob', 'age':15},
    {'name': 'charle', 'age':45}
]

print(friends[0])

attendance = {'alice': 96, 'bob':80, 'charlie':100}

for student in attendance:
    print(attendance[student])

for k, v in attendance.items():
    print(k, v)