# rewrite this code using OOP

student = {'name':'bob', 'grades':(89, 90, 93, 78, 90)}

def average(seq):
    return sum(seq) / len(seq)

print(average(student['grades']))

print('#------------OOP----------------')

# Define a class. 
class Student():
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def avg_grades(self):
        return sum(self.grades) / len(self.grades)

# Create an object which is an instance of the class.
student = Student('alice', (77,88,99))
print(student.name)
print(student.grades)
print(student.avg_grades())
alice = Student('alice', (1,2,3))
print(alice.avg_grades())
