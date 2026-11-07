# Day 61: Property Getter and Setter

class Student:

    def __init__(self, name: str, age: int):
        self._name = name
        self._age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value: int):
        if value < 1:
            raise ValueError("Age must be positive.")

        self._age = value


student1 = Student("Lalitendra", 18)

print("Original Age:", student1.age)

student1.age = 19

print("Updated Age:", student1.age)

# This raises ValueError:
# student1.age = -5