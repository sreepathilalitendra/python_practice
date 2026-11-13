from collections import namedtuple

Student = namedtuple("Student", ["name", "age", "course"])

student1 = Student("Lalitendra", 18, "CSE")

print("Name:", student1.name)
print("Age:", student1.age)
print("Course:", student1.course)