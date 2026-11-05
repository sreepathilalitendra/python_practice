# Day 59: Function Type Hints


# Function with integer parameters and integer return type
def add_numbers(a: int, b: int) -> int:
    return a + b


# Function with string parameter and string return type
def greet(name: str) -> str:
    return f"Hello, {name}!"


# Function with float parameters and float return type
def calculate_percentage(marks: float, total: float) -> float:
    return (marks / total) * 100


# Calling functions
result = add_numbers(10, 20)
print("Addition:", result)

message = greet("Lalitendra")
print(message)

percentage = calculate_percentage(425, 500)
print("Percentage:", percentage)

# Type Hints with Classes

class Student:

    def __init__(self, name: str, age: int) -> None:
        self.name: str = name
        self.age: int = age

    def display(self) -> None:
        print("Name:", self.name)
        print("Age:", self.age)


student1 = Student("Lalitendra", 18)

student1.display()