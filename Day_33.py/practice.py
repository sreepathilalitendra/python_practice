from abc import ABC, abstractmethod


# CHALLENGE 1: Vehicle

class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass


class Bike(Vehicle):

    def start(self):
        print("Bike starts")


class Car(Vehicle):

    def start(self):
        print("Car starts")


Bike().start()
Car().start()


# CHALLENGE 2: Employee

class Employee(ABC):

    @abstractmethod
    def calculate_salary(self):
        pass


class FullTimeEmployee(Employee):

    def calculate_salary(self):
        return 30000


class PartTimeEmployee(Employee):

    def calculate_salary(self):
        return 15000


print("Full-time salary:", FullTimeEmployee().calculate_salary())
print("Part-time salary:", PartTimeEmployee().calculate_salary())


# CHALLENGE 3: Shape

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass


class Square(Shape):

    def area(self):
        side = 4
        return side * side


class Circle(Shape):

    def area(self):
        radius = 5
        return 3.14 * radius * radius


print("Square area:", Square().area())
print("Circle area:", Circle().area())


# CHALLENGE 4: Notification

class Notification(ABC):

    @abstractmethod
    def send(self, message):
        pass


class EmailNotification(Notification):

    def send(self, message):
        print("Email:", message)


class SMSNotification(Notification):

    def send(self, message):
        print("SMS:", message)


EmailNotification().send("Hello!")
SMSNotification().send("Hello!")


# CHALLENGE 5: Payment

class Payment(ABC):

    @abstractmethod
    def pay(self, amount):
        pass


class CashPayment(Payment):

    def pay(self, amount):
        print("Cash payment:", amount)


class OnlinePayment(Payment):

    def pay(self, amount):
        print("Online payment:", amount)


CashPayment().pay(500)
OnlinePayment().pay(750)