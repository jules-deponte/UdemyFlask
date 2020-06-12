class ClassTest:
    def instance_method(self):
        print(f"called instance_method of {self}")

    @classmethod
    def class_method(cls):
        print(f"Call class_method of {cls}")

    # A static method is a method that contains no information about the class
    # and acts as if it is a separate function.
    @staticmethod
    def static_method():
        print("Called static_method")

test = ClassTest()
test.instance_method()

# do not have to instantialise an instance of a class to calla  class method. 
ClassTest.class_method()

ClassTest.static_method()


print('-------------------------------------------------------------------------------')
class Book:
    TYPES = ['hardcover', 'paperback']

    def __init__(self, name, book_type, weight):
        self.name = name
        self.book_type = book_type
        self.weight = weight

    @classmethod
    def hardcover(cls, name, weight):
        return print(f'name: {name}, {Book.TYPES[0]}, weighing {weight + 100}g')

    @classmethod
    def paperback(cls, name, weight):
        return print(f'name: {name}, {Book.TYPES[1]}, weighing {weight}g')

book = Book.hardcover("Harry Potter", 1500)
light = Book.paperback('Python 101', 600)
