# DAY 28: PYTHON OOPs
# CLASSES AND OBJECTS



# LESSON 1: Creating a Class

class Student:
    name = "Lalitendra"
    course = "Diploma CSE"


# LESSON 2: Creating an Object

student1 = Student()

print(student1.name)
print(student1.course)


# LESSON 3: Multiple Objects

student1 = Student()
student2 = Student()

print(student1.name)
print(student2.name)


# LESSON 4: __init__() Method

class Student:

    def __init__(self, name, course):
        self.name = name
        self.course = course


student1 = Student("Lalitendra", "Diploma CSE")

print(student1.name)
print(student1.course)


# LESSON 5: Using self

class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age


student1 = Student("Lalitendra", 18)

print(student1.name)
print(student1.age)


# LESSON 6: Method inside a Class

class Student:

    def __init__(self, name):
        self.name = name

    def introduce(self):
        print("My name is", self.name)


student1 = Student("Lalitendra")

student1.introduce()