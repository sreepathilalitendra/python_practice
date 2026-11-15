
from functools import (
    partial,
    reduce,
    lru_cache,
    wraps,
    total_ordering,
    singledispatch
)


# Example 1: partial()
# Create a new function with preset arguments

print("EXAMPLE 1: PARTIAL")

def multiply(a, b):
    return a * b

double = partial(multiply, 2)

print(double(5))
print(double(10))


# Example 2: reduce()
# Combine all values into one result

print("\nEXAMPLE 2: REDUCE")

numbers = [1, 2, 3, 4, 5]

total = reduce(
    lambda a, b: a + b,
    numbers
)

print("Sum:", total)


# Example 3: lru_cache()
# Store previously calculated results

print("\nEXAMPLE 3: LRU CACHE")

@lru_cache(maxsize=None)
def factorial(number):
    if number <= 1:
        return 1

    return number * factorial(number - 1)


print("Factorial:", factorial(5))
print("Factorial:", factorial(6))
print("Cache Info:", factorial.cache_info())


# Example 4: wraps()
# Preserve original function information in decorators

print("\nEXAMPLE 4: WRAPS")

def my_decorator(function):

    @wraps(function)
    def wrapper():
        print("Before function execution")

        function()

        print("After function execution")

    return wrapper


@my_decorator
def greet():
    """This function displays a greeting."""
    print("Hello, Python!")


greet()

print("Function Name:", greet.__name__)
print("Function Description:", greet.__doc__)


# Example 5: total_ordering()
# Automatically generate comparison methods

print("\nEXAMPLE 5: TOTAL ORDERING")

@total_ordering
class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def __eq__(self, other):
        return self.marks == other.marks

    def __lt__(self, other):
        return self.marks < other.marks


student1 = Student("Rahul", 85)
student2 = Student("Arjun", 90)

print("Student 1 < Student 2:", student1 < student2)
print("Student 1 > Student 2:", student1 > student2)
print("Student 1 == Student 2:", student1 == student2)


# Example 6: singledispatch()
# Different behavior based on argument type

print("\nEXAMPLE 6: SINGLEDISPATCH")

@singledispatch
def display(value):
    print("Unknown Type:", value)


@display.register
def _(value: int):
    print("Integer:", value)


@display.register
def _(value: str):
    print("String:", value)


@display.register
def _(value: list):
    print("List:", value)


display(100)
display("Python")
display([10, 20, 30])
display(10.5)


# Mini Project: Discount Calculator Using partial()

print("\nMINI PROJECT: DISCOUNT CALCULATOR")

def calculate_price(price, discount):
    return price - (price * discount / 100)


ten_percent_discount = partial(
    calculate_price,
    discount=10
)

twenty_percent_discount = partial(
    calculate_price,
    discount=20
)

original_price = 1000

print("Original Price:", original_price)
print("10% Discount:", ten_percent_discount(original_price))
print("20% Discount:", twenty_percent_discount(original_price))


print("\nDAY 69 MAIN LESSON COMPLETED!")
