
from functools import (
    partial,
    reduce,
    lru_cache,
    wraps,
    total_ordering,
    singledispatch
)


# Challenge 1: partial() - Triple a Number

print("CHALLENGE 1: PARTIAL")

def multiply(a, b):
    return a * b


triple = partial(multiply, 3)

print("Triple of 5:", triple(5))
print("Triple of 10:", triple(10))


# Challenge 2: reduce() - Product of Numbers

print("\nCHALLENGE 2: REDUCE PRODUCT")

numbers = [2, 3, 4, 5]

product_result = reduce(
    lambda a, b: a * b,
    numbers
)

print("Product:", product_result)


# Challenge 3: reduce() - Largest Number

print("\nCHALLENGE 3: LARGEST NUMBER")

numbers = [25, 80, 45, 100, 60, 90]

largest = reduce(
    lambda a, b: a if a > b else b,
    numbers
)

print("Largest Number:", largest)


# Challenge 4: lru_cache() - Fibonacci Series

print("\nCHALLENGE 4: FIBONACCI")

@lru_cache(maxsize=None)
def fibonacci(number):

    if number <= 1:
        return number

    return fibonacci(number - 1) + fibonacci(number - 2)


for number in range(10):
    print(fibonacci(number), end=" ")


print("\nCache Information:", fibonacci.cache_info())


# Challenge 5: wraps() - Custom Decorator

print("\n\nCHALLENGE 5: WRAPS")

def my_decorator(function):

    @wraps(function)
    def wrapper():
        print("Function Started")

        function()

        print("Function Completed")

    return wrapper


@my_decorator
def greet():
    """Display a welcome message."""
    print("Welcome to Python!")


greet()

print("Function Name:", greet.__name__)
print("Function Description:", greet.__doc__)


# Challenge 6: total_ordering() - Employee Salary Comparison

print("\nCHALLENGE 6: EMPLOYEE SALARY")

@total_ordering
class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __eq__(self, other):
        if not isinstance(other, Employee):
            return NotImplemented

        return self.salary == other.salary

    def __lt__(self, other):
        if not isinstance(other, Employee):
            return NotImplemented

        return self.salary < other.salary


employee1 = Employee("Rahul", 30000)
employee2 = Employee("Arjun", 40000)

print("Rahul < Arjun:", employee1 < employee2)
print("Rahul > Arjun:", employee1 > employee2)
print("Rahul == Arjun:", employee1 == employee2)


# Challenge 7: singledispatch() - Display Different Types

print("\nCHALLENGE 7: SINGLEDISPATCH")

@singledispatch
def display(value):
    print("Unknown Type:", value)


@display.register
def _(value: int):
    print("Integer Value:", value)


@display.register
def _(value: str):
    print("String Value:", value)


@display.register
def _(value: list):
    print("List Values:", value)


display(100)
display("CodeMonolith")
display([10, 20, 30])
display(10.5)


# Challenge 8: MINI PROJECT - Tax Calculator Using partial()

print("\nCHALLENGE 8: TAX CALCULATOR")

def calculate_tax(amount, tax_rate):
    tax = amount * tax_rate / 100
    return amount + tax


gst_5 = partial(calculate_tax, tax_rate=5)
gst_12 = partial(calculate_tax, tax_rate=12)
gst_18 = partial(calculate_tax, tax_rate=18)

price = 1000

print("Original Price:", price)
print("Price with 5% Tax:", gst_5(price))
print("Price with 12% Tax:", gst_12(price))
print("Price with 18% Tax:", gst_18(price))


print("\nDAY 69 CHALLENGES COMPLETED!")
