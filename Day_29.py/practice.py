# ==========================================
# DAY 29: CHALLENGE SOLUTIONS
# ==========================================


# CHALLENGE 1:
# Student class with name and age

class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age


student1 = Student("Lalitendra", 18)

print(student1.name)
print(student1.age)


# CHALLENGE 2:
# Two students with different names and ages

class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age


student1 = Student("Lalitendra", 18)
student2 = Student("Rahul", 19)

print(student1.name, student1.age)
print(student2.name, student2.age)


# CHALLENGE 3:
# Student class with a class variable

class Student:

    college = "St. Mary's"

    def __init__(self, name):
        self.name = name


student1 = Student("Lalitendra")

print(student1.name)
print(student1.college)


# CHALLENGE 4:
# Change the age of a student

class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age


student1 = Student("Lalitendra", 18)

print(student1.age)

student1.age = 19

print(student1.age)


# CHALLENGE 5:
# Calculator with add and subtract

class Calculator:

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b


calculator = Calculator()

print(calculator.add(10, 5))
print(calculator.subtract(10, 5))


# CHALLENGE 6:
# Car class with display method

class Car:

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display(self):
        print("Brand:", self.brand)
        print("Model:", self.model)


car1 = Car("Toyota", "Fortuner")

car1.display()


# CHALLENGE 7:
# Person class with introduce method

class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print("My name is", self.name)
        print("My age is", self.age)


person1 = Person("Lalitendra", 18)

person1.introduce()


# CHALLENGE 8:
# Laptop class with class and instance variables

class Laptop:

    category = "Electronics"

    def __init__(self, brand, price):
        self.brand = brand
        self.price = price


laptop1 = Laptop("Dell", 50000)

print("Brand:", laptop1.brand)
print("Price:", laptop1.price)
print("Category:", laptop1.category)