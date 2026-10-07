# DAY 30: PYTHON OOPs
# ENCAPSULATION



# LESSON 1: Public Attribute

class Student:

    def __init__(self, name):
        self.name = name


student1 = Student("Lalitendra")

print(student1.name)


# LESSON 2: Protected Attribute

class Student:

    def __init__(self, name):
        self._name = name


student1 = Student("Lalitendra")

print(student1._name)


# LESSON 3: Private Attribute

class Student:

    def __init__(self, name):
        self.__name = name


student1 = Student("Lalitendra")

print(student1._Student__name)


# LESSON 4: Getter Method

class Student:

    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name


student1 = Student("Lalitendra")

print(student1.get_name())


# LESSON 5: Setter Method

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


# LESSON 6: Getter + Setter with Validation

class Student:

    def __init__(self, age):
        self.__age = age

    def get_age(self):
        return self.__age

    def set_age(self, age):

        if age >= 0:
            self.__age = age
        else:
            print("Age cannot be negative!")


student1 = Student(18)

print(student1.get_age())

student1.set_age(19)

print(student1.get_age())

student1.set_age(-5)

print(student1.get_age())