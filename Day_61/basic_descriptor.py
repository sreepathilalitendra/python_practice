# Day 61: Basic Custom Descriptor

class PositiveAge:

    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self

        return instance.__dict__.get(self.name)

    def __set__(self, instance, value):
        if not isinstance(value, int) or isinstance(value, bool):
            raise TypeError("Age must be an integer.")

        if value < 1:
            raise ValueError("Age must be positive.")

        instance.__dict__[self.name] = value


class Student:

    age = PositiveAge()

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age


student1 = Student("Lalitendra", 18)

print("Name:", student1.name)
print("Age:", student1.age)

student1.age = 19

print("Updated Age:", student1.age)

# This raises ValueError:
# student1.age = -5