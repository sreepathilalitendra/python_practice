# Day 62: String Representation

class Student:

    def __init__(self, name, course):
        self.name = name
        self.course = course

    def __str__(self):
        return f"{self.name} - {self.course}"

    def __repr__(self):
        return f"Student(name={self.name!r}, course={self.course!r})"


student1 = Student("Lalitendra", "Diploma CSE")

print("Using str():", str(student1))
print("Using repr():", repr(student1))