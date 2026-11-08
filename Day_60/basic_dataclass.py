# Day 60: Basic Dataclass

from dataclasses import dataclass


@dataclass
class Student:
    name: str
    age: int
    course: str


student1 = Student("Lalitendra", 18, "Diploma CSE")

print(student1)
print("Name:", student1.name)
print("Age:", student1.age)
print("Course:", student1.course)

student2 = Student("Lalitendra", 18, "Diploma CSE")
print("Are students equal?", student1 == student2)
