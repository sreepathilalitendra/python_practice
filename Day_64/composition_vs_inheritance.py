# Inheritance example

class Person:
    def introduce(self):
        print("I am a person")


class Student(Person):
    def study(self):
        print("I am studying")


student = Student()

student.introduce()
student.study()


print()


# Composition example

class Laptop:
    def start(self):
        print("Laptop started")


class Developer:
    def __init__(self):
        self.laptop = Laptop()

    def work(self):
        self.laptop.start()
        print("Developer is working")


developer = Developer()

developer.work()