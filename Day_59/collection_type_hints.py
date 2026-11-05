# Day 59: Collection Type Hints


# List
marks: list[int] = [85, 90, 78, 95]

# Tuple
subjects: tuple[str, ...] = ("Python", "Java", "DBMS")

# Dictionary
student: dict[str, int] = {
    "Maths": 85,
    "Python": 90,
    "Java": 78
}

# Set
numbers: set[int] = {10, 20, 30, 40}


print("Marks:", marks)
print("Subjects:", subjects)
print("Student Marks:", student)
print("Numbers:", numbers)