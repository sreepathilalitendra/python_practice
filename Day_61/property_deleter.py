# Day 61: Property Deleter

class Student:

    def __init__(self, name: str):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.deleter
    def name(self):
        print("Deleting student name...")
        del self._name


student1 = Student("Lalitendra")

print("Name:", student1.name)

del student1.name

print("Name deleted successfully!")