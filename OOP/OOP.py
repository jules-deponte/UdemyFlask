student = {'name':'bob', 'grades':(89, 90, 93, 78, 90)}

def average(seq):
    return sum(seq) / len(seq)

print(average(student['grades']))