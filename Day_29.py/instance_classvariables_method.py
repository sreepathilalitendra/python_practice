# ==========================================
# DAY 29: OOPs
# INSTANCE & CLASS VARIABLES + METHODS
# ==========================================


# LESSON 1: Instance Variables

class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age


student1 = Student("Lalitendra", 18)
student2 = Student("Rahul", 19)

print(student1.name)
print(student2.name)


# LESSON 2: Class Variable

class Student:

    college = "St. Mary's"

    def __init__(self, name):
        self.name = name


student1 = Student("Lalitendra")
student2 = Student("Rahul")

print(student1.college)
print(student2.college)


# LESSON 3: Instance Method

class Student:

    def __init__(self, name):
        self.name = name

    def introduce(self):
        print("My name is", self.name)


student1 = Student("Lalitendra")

student1.introduce()


# LESSON 4: Changing Instance Variable

class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age


student1 = Student("Lalitendra", 18)

print(student1.age)

student1.age = 19

print(student1.age)


# LESSON 5: Changing Class Variable

class Student:

    college = "St. Mary's"

    def __init__(self, name):
        self.name = name


student1 = Student("Lalitendra")

print(student1.college)

Student.college = "ABC College"

print(student1.college)


# LESSON 6: Multiple Methods

class Calculator:

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b


calculator = Calculator()

print(calculator.add(10, 5))
print(calculator.subtract(10, 5))
print(calculator.multiply(10, 5))