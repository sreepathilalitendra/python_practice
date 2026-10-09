
# DAY 31: PYTHON OOPs
# INHERITANCE



# LESSON 1: Basic Inheritance

class Animal:

    def eat(self):
        print("Animal is eating")


class Dog(Animal):
    pass


dog1 = Dog()

dog1.eat()


# LESSON 2: Parent and Child Class

class Animal:

    def eat(self):
        print("Animal is eating")


class Dog(Animal):

    def bark(self):
        print("Dog is barking")


dog1 = Dog()

dog1.eat()
dog1.bark()


# LESSON 3: __init__() in Parent Class

class Animal:

    def __init__(self, name):
        self.name = name

    def show_name(self):
        print("Name:", self.name)


class Dog(Animal):

    def bark(self):
        print("Dog is barking")


dog1 = Dog("Tommy")

dog1.show_name()
dog1.bark()


# LESSON 4: Using super()

class Animal:

    def __init__(self, name):
        self.name = name


class Dog(Animal):

    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed


dog1 = Dog("Tommy", "Labrador")

print("Name:", dog1.name)
print("Breed:", dog1.breed)


# LESSON 5: Method Inheritance

class Animal:

    def eat(self):
        print("Animal is eating")

    def sleep(self):
        print("Animal is sleeping")


class Dog(Animal):

    def bark(self):
        print("Dog is barking")


dog1 = Dog()

dog1.eat()
dog1.sleep()
dog1.bark()


# LESSON 6: Method Overriding

class Animal:

    def sound(self):
        print("Animal makes a sound")


class Dog(Animal):

    def sound(self):
        print("Dog barks")


dog1 = Dog()

dog1.sound()