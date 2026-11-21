
# Day 75: Code Quality, Refactoring and PEP 8

# Example 1: Good variable naming

student_name = "Lalitendra"
student_age = 18
student_course = "Diploma CSE"

print("Student Name:", student_name)
print("Student Age:", student_age)
print("Student Course:", student_course)


# Example 2: Proper function naming

def calculate_total(price, quantity):
    total = price * quantity
    return total


print("\nTotal:", calculate_total(100, 3))


# Example 3: Using docstrings

def calculate_square(number):
    """Return the square of a number."""
    return number ** 2


print("\nSquare:", calculate_square(5))
print(calculate_square.__doc__)


# Example 4: Avoid duplicate code

def display_message(message):
    print(message)


display_message("\nWelcome to Python")
display_message("Welcome to CodeMonolith")


# Example 5: Refactoring duplicate code

def calculate_area(length, width):
    """Calculate the area of a rectangle."""
    return length * width


rectangle_one = calculate_area(10, 5)
rectangle_two = calculate_area(8, 4)

print("\nRectangle One Area:", rectangle_one)
print("Rectangle Two Area:", rectangle_two)


# Example 6: Type hints

def add_numbers(a: int, b: int) -> int:
    """Return the sum of two integers."""
    return a + b


print("\nAddition:", add_numbers(20, 30))


# Example 7: Constants using uppercase names

TAX_RATE = 0.05
PRODUCT_PRICE = 1000

tax_amount = PRODUCT_PRICE * TAX_RATE
final_price = PRODUCT_PRICE + tax_amount

print("\nTax Amount:", tax_amount)
print("Final Price:", final_price)


# Example 8: List comprehension

numbers = [1, 2, 3, 4, 5, 6]

even_numbers = [
    number
    for number in numbers
    if number % 2 == 0
]

print("\nEven Numbers:", even_numbers)


# Example 9: Using meaningful conditions

def is_eligible(age: int) -> bool:
    return age >= 18


print("\nEligible:", is_eligible(20))


# Example 10: Clean student report program

def calculate_average(marks: list[int]) -> float:
    """Calculate average marks."""
    if not marks:
        return 0.0

    return sum(marks) / len(marks)


def display_student_report(
    name: str,
    marks: list[int]
) -> None:
    """Display student details and average marks."""
    average = calculate_average(marks)

    print("\nStudent Report")
    print("Name:", name)
    print("Marks:", marks)
    print("Average:", average)


student_marks = [85, 90, 80]

display_student_report(
    "Lalitendra",
    student_marks
)
