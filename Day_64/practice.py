# Challenge 1: Basic Inheritance

class Vehicle:
    def start(self):
        print("Vehicle started")


class Bike(Vehicle):
    def ride(self):
        print("Bike is riding")


bike = Bike()

bike.start()
bike.ride()


print("\n------------------------------\n")


# Challenge 2: Phone and Camera

class Camera:
    def take_photo(self):
        print("Camera is ready")
        print("Photo captured")


class Phone:
    def __init__(self):
        self.camera = Camera()

    def open_camera(self):
        self.camera.take_photo()


phone = Phone()

phone.open_camera()


print("\n------------------------------\n")


# Challenge 3: Computer and Processor

class Processor:
    def run(self):
        print("Processor is running")


class Computer:
    def __init__(self):
        self.processor = Processor()

    def start_computer(self):
        self.processor.run()
        print("Computer started successfully")


computer = Computer()

computer.start_computer()


print("\n------------------------------\n")


# Challenge 4: Person and Teacher

class Person:
    def __init__(self, name):
        self.name = name

    def display_name(self):
        print("Name:", self.name)


class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

    def display_details(self):
        self.display_name()
        print("Subject:", self.subject)


teacher = Teacher("Rahul", "Python")

teacher.display_details()


print("\n------------------------------\n")


# Challenge 5: Library and Book

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author


class Library:
    def __init__(self):
        self.book = Book("Python Basics", "John")

    def display_book(self):
        print("Book:", self.book.title)
        print("Author:", self.book.author)


library = Library()

library.display_book()


print("\n------------------------------\n")


# Challenge 6: Smartphone Mini Project

class Battery:
    def charge(self):
        print("Battery is charging")


class Camera:
    def take_photo(self):
        print("Camera is ready")
        print("Photo captured")


class Smartphone:
    def __init__(self):
        self.battery = Battery()
        self.camera = Camera()

    def use_phone(self):
        self.battery.charge()
        self.camera.take_photo()
        print("Smartphone is working")


smartphone = Smartphone()

smartphone.use_phone()


print("\n------------------------------\n")


# Challenge 7: Computer System Mini Project

class Processor:
    def __init__(self, name):
        self.name = name


class RAM:
    def __init__(self, size):
        self.size = size


class Storage:
    def __init__(self, capacity):
        self.capacity = capacity


class ComputerSystem:
    def __init__(self):
        self.processor = Processor("Intel i5")
        self.ram = RAM("16 GB")
        self.storage = Storage("512 GB SSD")

    def display_specs(self):
        print("Computer Specifications")
        print("Processor:", self.processor.name)
        print("RAM:", self.ram.size)
        print("Storage:", self.storage.capacity)


system = ComputerSystem()

system.display_specs()
