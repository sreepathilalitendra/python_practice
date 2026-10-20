# Challenge 1: Calculator module functions

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


print("Addition:", add(10, 5))
print("Subtraction:", subtract(10, 5))
print("Multiplication:", multiply(10, 5))


# Challenge 2: Student module function

def student_details(name, course):
    return f"{name} is studying {course}."


print(student_details("Lalitendra", "Diploma CSE"))


# Challenge 3: Import from Python's math module

from math import sqrt, factorial

print("Square root:", sqrt(81))
print("Factorial:", factorial(5))


# Challenge 4: Package-style calculator and greeting functions

def square(number):
    return number ** 2


def greet(name):
    return f"Hello, {name}!"


print("Square:", square(5))
print(greet("Python learner"))


# Challenge 5: Safe division

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"

    return a / b


print("Division:", divide(10, 2))
print("Division by zero:", divide(10, 0))
