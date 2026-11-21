# Challenge 1: Five variables with proper naming

student_name = "Lalitendra"
student_age = 18
student_course = "Diploma CSE"
student_college = "St. Mary's Group of Institutions"
student_percentage = 85.5

print("Student Details")
print(student_name)
print(student_age)
print(student_course)
print(student_college)
print(student_percentage)


# Challenge 2: Calculate discount

def calculate_discount(price: float, discount: float) -> float:
    """Calculate the discounted price."""
    discount_amount = price * discount / 100
    final_price = price - discount_amount

    return final_price


print("\nDiscounted Price:", calculate_discount(1000, 10))


# Challenge 3: Function with docstring

def calculate_square(number: int) -> int:
    """Return the square of a given number."""
    return number ** 2


print("\nSquare:", calculate_square(5))
print(calculate_square.__doc__)


# Challenge 4: Remove duplicate code

def display_student(name: str, course: str) -> None:
    """Display student information."""
    print("Name:", name)
    print("Course:", course)


print("\nStudent One")
display_student("Lalitendra", "Diploma CSE")

print("\nStudent Two")
display_student("Rahul", "B.Tech CSE")


# Challenge 5: Create StudentDetails class

class StudentDetails:

    def __init__(self, name: str, course: str):
        self.name = name
        self.course = course

    def display(self) -> None:
        print("Name:", self.name)
        print("Course:", self.course)


print("\nStudent Class")

student = StudentDetails("Lalitendra", "Diploma CSE")
student.display()


# Challenge 6: Type hints in three functions

def add_numbers(a: int, b: int) -> int:
    return a + b


def multiply_numbers(a: int, b: int) -> int:
    return a * b


def calculate_average(marks: list[int]) -> float:
    if not marks:
        return 0.0

    return sum(marks) / len(marks)


print("\nAddition:", add_numbers(10, 20))
print("Multiplication:", multiply_numbers(5, 4))
print("Average:", calculate_average([80, 90, 70]))


# Challenge 7: Constants using uppercase names

TAX_RATE = 5
MAX_STUDENTS = 50
COLLEGE_NAME = "St. Mary's Group of Institutions"

print("\nConstants")
print("Tax Rate:", TAX_RATE)
print("Maximum Students:", MAX_STUDENTS)
print("College:", COLLEGE_NAME)


# Challenge 8: Refactored calculator

def add(a: float, b: float) -> float:
    return a + b


def subtract(a: float, b: float) -> float:
    return a - b


def multiply(a: float, b: float) -> float:
    return a * b


def divide(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("Cannot divide by zero")

    return a / b


print("\nCalculator")
print("Addition:", add(20, 10))
print("Subtraction:", subtract(20, 10))
print("Multiplication:", multiply(20, 10))
print("Division:", divide(20, 10))


# Challenge 9: Code quality checking
# Run these commands in the terminal:
# python -m flake8 day75_challenge.py
# python -m pylint day75_challenge.py


# Challenge 10: Clean Student Management Program

class Student:

    def __init__(
        self,
        name: str,
        roll_number: int,
        marks: list[int]
    ):
        self.name = name
        self.roll_number = roll_number
        self.marks = marks

    def calculate_average(self) -> float:
        if not self.marks:
            return 0.0

        return sum(self.marks) / len(self.marks)

    def display_report(self) -> None:
        print("\nStudent Report")
        print("Name:", self.name)
        print("Roll Number:", self.roll_number)
        print("Marks:", self.marks)
        print("Average:", self.calculate_average())


students = [
    Student("Lalitendra", 101, [85, 90, 80]),
    Student("Rahul", 102, [75, 80, 85]),
    Student("Arjun", 103, [90, 95, 88])
]

print("\nStudent Management System")

for student in students:
    student.display_report()
