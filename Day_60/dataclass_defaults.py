# Day 60: Dataclass Default Values

from dataclasses import dataclass


@dataclass
class Employee:
    name: str
    role: str = "Trainee"
    salary: int = 15000


employee1 = Employee("Arun")
employee2 = Employee("Kiran", "Python Developer", 25000)

print(employee1)
print(employee2)