# CHALLENGE 1:
# Student class with private __name

class Student:

    def __init__(self, name):
        self.__name = name


student1 = Student("Lalitendra")


# CHALLENGE 2:
# Getter method for student's name

class Student:

    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name


student1 = Student("Lalitendra")

print(student1.get_name())


# CHALLENGE 3:
# Setter method to change student's name

class Student:

    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name


student1 = Student("Lalitendra")

print(student1.get_name())

student1.set_name("Rahul")

print(student1.get_name())


# CHALLENGE 4:
# BankAccount with private __balance

class BankAccount:

    def __init__(self, balance):
        self.__balance = balance

    def get_balance(self):
        return self.__balance


account = BankAccount(5000)

print(account.get_balance())


# CHALLENGE 5:
# Getter and setter for balance

class BankAccount:

    def __init__(self, balance):
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def set_balance(self, balance):
        self.__balance = balance


account = BankAccount(5000)

print(account.get_balance())

account.set_balance(8000)

print(account.get_balance())


# CHALLENGE 6:
# Prevent negative balance

class BankAccount:

    def __init__(self, balance):
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def set_balance(self, balance):

        if balance >= 0:
            self.__balance = balance
        else:
            print("Balance cannot be negative!")


account = BankAccount(5000)

print(account.get_balance())

account.set_balance(8000)

print(account.get_balance())

account.set_balance(-1000)

print(account.get_balance())


# CHALLENGE 7:
# Person with private __age and validation

class Person:

    def __init__(self, age):
        self.__age = age

    def get_age(self):
        return self.__age

    def set_age(self, age):

        if age >= 0:
            self.__age = age
        else:
            print("Age cannot be negative!")


person1 = Person(18)

print(person1.get_age())

person1.set_age(19)

print(person1.get_age())

person1.set_age(-5)


# CHALLENGE 8:
# Product with private __price
# Prevent negative price

class Product:

    def __init__(self, price):
        self.__price = price

    def get_price(self):
        return self.__price

    def set_price(self, price):

        if price >= 0:
            self.__price = price
        else:
            print("Price cannot be negative!")


product1 = Product(500)

print(product1.get_price())

product1.set_price(750)

print(product1.get_price())

product1.set_price(-100)

print(product1.get_price())