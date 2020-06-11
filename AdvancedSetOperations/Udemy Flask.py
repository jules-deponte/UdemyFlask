friends = {'alice', 'bob', 'charlie'}
abroad = {'alice', 'bob', 'Doug'}

local_friends = friends.difference(abroad)
print(local_friends)

all_friends = friends.union(abroad)
print(all_friends)

art = {'alice', 'bob', 'cahrlie', 'doug'}
science = {'Earnest', 'frank', 'alice', 'bob'}

both_subjects = art.intersection(science)
print(both_subjects)