# Day 62: Comparison Magic Methods

class Student:

    def __init__(self, marks):
        self.marks = marks

    def __eq__(self, other):
        return self.marks == other.marks

    def __lt__(self, other):
        return self.marks < other.marks


student1 = Student(85)
student2 = Student(90)
student3 = Student(85)

print("Equal:", student1 == student3)
print("Student 1 has lower marks:", student1 < student2)