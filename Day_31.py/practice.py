# CHALLENGE 1:
# Create Animal and Dog classes

class Animal:

    def eat(self):
        print("Animal is eating")


class Dog(Animal):
    pass


dog1 = Dog()

dog1.eat()


# CHALLENGE 2:
# Dog inherits eat() and has its own bark()

class Animal:

    def eat(self):
        print("Animal is eating")


class Dog(Animal):

    def bark(self):
        print("Dog is barking")


dog1 = Dog()

dog1.eat()
dog1.bark()


# CHALLENGE 3:
# Parent class with name

class Person:

    def __init__(self, name):
        self.name = name


class Student(Person):

    def study(self):
        print(self.name, "is studying")


student1 = Student("Lalitendra")

print(student1.name)
student1.study()


# CHALLENGE 4:
# Use super() to initialize parent data

class Person:

    def __init__(self, name):
        self.name = name


class Student(Person):

    def __init__(self, name, course):
        super().__init__(name)
        self.course = course


student1 = Student("Lalitendra", "Diploma CSE")

print("Name:", student1.name)
print("Course:", student1.course)


# CHALLENGE 5:
# Create parent and child methods

class Vehicle:

    def start(self):
        print("Vehicle started")


class Car(Vehicle):

    def drive(self):
        print("Car is driving")


car1 = Car()

car1.start()
car1.drive()


# CHALLENGE 6:
# Method overriding

class Animal:

    def sound(self):
        print("Animal makes a sound")


class Cat(Animal):

    def sound(self):
        print("Cat meows")


cat1 = Cat()

cat1.sound()


# CHALLENGE 7:
# Person and Employee inheritance

class Person:

    def __init__(self, name):
        self.name = name


class Employee(Person):

    def __init__(self, name, salary):
        super().__init__(name)
        self.salary = salary

    def display(self):
        print("Name:", self.name)
        print("Salary:", self.salary)


employee1 = Employee("Lalitendra", 25000)

employee1.display()


# CHALLENGE 8:
# Multilevel inheritance

class Grandparent:

    def house(self):
        print("Grandparent has a house")


class Parent(Grandparent):

    def car(self):
        print("Parent has a car")


class Child(Parent):

    def bike(self):
        print("Child has a bike")


child1 = Child()

child1.house()
child1.car()
child1.bike()