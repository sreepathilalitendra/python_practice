# DAY 33: ABSTRACTION IN PYTHON

from abc import ABC, abstractmethod


# LESSON 1: Abstract Class

class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass


# LESSON 2: Implementing an Abstract Method

class Dog(Animal):

    def sound(self):
        print("Dog barks")


class Cat(Animal):

    def sound(self):
        print("Cat meows")


dog = Dog()
cat = Cat()

dog.sound()
cat.sound()


# LESSON 3: Abstract Class with Multiple Methods

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def display(self):
        pass


class Rectangle(Shape):

    def area(self):
        length = 10
        width = 5
        return length * width

    def display(self):
        print("I am a rectangle")


rectangle = Rectangle()

rectangle.display()
print("Area:", rectangle.area())


# LESSON 4: Practical Example - Payment System

class Payment(ABC):

    @abstractmethod
    def pay(self, amount):
        pass


class UpiPayment(Payment):

    def pay(self, amount):
        print("Paid using UPI:", amount)


class CardPayment(Payment):

    def pay(self, amount):
        print("Paid using card:", amount)


upi = UpiPayment()
card = CardPayment()

upi.pay(500)
card.pay(1000)