# CHALLENGE 1

class Student:

    def __init__(self, name, course):
        self.name = name
        self.course = course


student1 = Student("Lalitendra", "Diploma CSE")

print(student1.name)
print(student1.course)


# CHALLENGE 2

class Student:

    def __init__(self, name):
        self.name = name


student1 = Student("Lalitendra")
student2 = Student("Rahul")

print(student1.name)
print(student2.name)


# CHALLENGE 3

class Car:

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model


car1 = Car("Toyota", "Fortuner")

print(car1.brand)
print(car1.model)


# CHALLENGE 4

class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age


person1 = Person("Lalitendra", 18)

print(person1.name)
print(person1.age)


# CHALLENGE 5

class Student:

    def __init__(self, name):
        self.name = name

    def introduce(self):
        print("My name is", self.name)


student1 = Student("Lalitendra")

student1.introduce()


# CHALLENGE 6

class Calculator:

    def add(self, a, b):
        return a + b


calculator = Calculator()

result = calculator.add(10, 20)

print("Result:", result)


# CHALLENGE 7

class Laptop:

    def __init__(self, brand, price):
        self.brand = brand
        self.price = price


laptop1 = Laptop("Dell", 50000)
laptop2 = Laptop("HP", 45000)

print(laptop1.brand, laptop1.price)
print(laptop2.brand, laptop2.price)


# CHALLENGE 8

class Dog:

    def sound(self):
        print("Dog is barking")


dog1 = Dog()

dog1.sound()