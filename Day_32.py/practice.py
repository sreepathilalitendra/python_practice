# CHALLENGE 1: Dog and Cat sound()

class Dog:

    def sound(self):
        print("Dog barks")


class Cat:

    def sound(self):
        print("Cat meows")


dog1 = Dog()
cat1 = Cat()

dog1.sound()
cat1.sound()


# CHALLENGE 2: One function, different objects

class Dog:

    def sound(self):
        print("Dog barks")


class Cat:

    def sound(self):
        print("Cat meows")


def make_sound(animal):
    animal.sound()


make_sound(Dog())
make_sound(Cat())


# CHALLENGE 3: Method overriding

class Vehicle:

    def start(self):
        print("Vehicle starts")


class Car(Vehicle):

    def start(self):
        print("Car starts with a button")


vehicle1 = Vehicle()
car1 = Car()

vehicle1.start()
car1.start()


# CHALLENGE 4: Different payment methods

class CashPayment:

    def pay(self, amount):
        print("Paid by cash:", amount)


class OnlinePayment:

    def pay(self, amount):
        print("Paid online:", amount)


def process_payment(payment, amount):
    payment.pay(amount)


process_payment(CashPayment(), 500)
process_payment(OnlinePayment(), 1000)


# CHALLENGE 5: Different display() methods

class Student:

    def display(self):
        print("I am a student")


class Teacher:

    def display(self):
        print("I am a teacher")


for person in [Student(), Teacher()]:
    person.display()


# CHALLENGE 6: Different area() methods

class Rectangle:

    def area(self):
        length = 10
        width = 5
        return length * width


class Square:

    def area(self):
        side = 4
        return side * side


for shape in [Rectangle(), Square()]:
    print("Area:", shape.area())


# CHALLENGE 7: Different notification methods

class EmailNotification:

    def send(self):
        print("Sending email notification")


class SMSNotification:

    def send(self):
        print("Sending SMS notification")


def notify(notification):
    notification.send()


notify(EmailNotification())
notify(SMSNotification())


# CHALLENGE 8: Different employee salaries

class FullTimeEmployee:

    def calculate_salary(self):
        return 30000


class PartTimeEmployee:

    def calculate_salary(self):
        return 15000


employees = [FullTimeEmployee(), PartTimeEmployee()]

for employee in employees:
    print("Salary:", employee.calculate_salary())