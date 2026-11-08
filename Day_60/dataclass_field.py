# Day 60: Dataclass Field

from dataclasses import dataclass, field


@dataclass
class Student:
    name: str
    marks: list[int] = field(default_factory=list)


student1 = Student("Lalitendra")
student2 = Student("Arun")

student1.marks.append(90)
student1.marks.append(85)

student2.marks.append(75)

print(student1)
print(student2)