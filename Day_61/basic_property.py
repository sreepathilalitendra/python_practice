# Day 61: Basic Property

class Student:

    def __init__(self, name: str):
        self._name = name

    @property
    def name(self):
        return self._name


student1 = Student("Lalitendra")

print("Student Name:", student1.name)