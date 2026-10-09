
# DAY 32: PYTHON OOP
# POLYMORPHISM



# LESSON 1: Same Method Name in Different Classes

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


# LESSON 2: Polymorphism with a Function

class Dog:

    def sound(self):
        print("Dog barks")


class Cat:

    def sound(self):
        print("Cat meows")


def make_sound(animal):
    animal.sound()


dog1 = Dog()
cat1 = Cat()

make_sound(dog1)
make_sound(cat1)


# LESSON 3: Method Overriding

class Animal:

    def sound(self):
        print("Animal makes a sound")


class Dog(Animal):

    def sound(self):
        print("Dog barks")


animal1 = Animal()
dog1 = Dog()

animal1.sound()
dog1.sound()


# LESSON 4: Polymorphism with Inheritance

class Animal:

    def sound(self):
        print("Animal makes a sound")


class Dog(Animal):

    def sound(self):
        print("Dog barks")


class Cat(Animal):

    def sound(self):
        print("Cat meows")


animals = [Animal(), Dog(), Cat()]

for animal in animals:
    animal.sound()


# LESSON 5: Polymorphism with Different Shapes

class Circle:

    def area(self):
        radius = 5
        return 3.14 * radius * radius


class Square:

    def area(self):
        side = 4
        return side * side


circle1 = Circle()
square1 = Square()

print("Circle area:", circle1.area())
print("Square area:", square1.area())


# LESSON 6: Built-in Polymorphism

print(len("Python"))
print(len([10, 20, 30]))
print(len({"name": "Lalitendra", "course": "CSE"}))