
# Example 1: Basic debugging using print()

def add_numbers(a, b):
    print("Debug: First number:", a)
    print("Debug: Second number:", b)

    result = a + b

    print("Debug: Result:", result)

    return result


print("Addition:", add_numbers(10, 20))


# Example 2: Debugging using breakpoint()

def calculate_total(price, quantity):
    breakpoint()

    total = price * quantity

    return total


# Uncomment the next line to enter the debugger
# print("Total:", calculate_total(100, 3))


# Example 3: Debugging a function

def calculate_average(marks):
    total = sum(marks)
    count = len(marks)

    if count == 0:
        return 0

    return total / count


marks = [80, 90, 75]

print("\nAverage:", calculate_average(marks))


# Example 4: Function for unit testing

def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")

    return a / b


def is_even(number):
    return number % 2 == 0


def get_grade(mark):
    if mark >= 90:
        return "A"

    elif mark >= 75:
        return "B"

    elif mark >= 50:
        return "C"

    return "Fail"


print("\nMultiplication:", multiply(5, 4))
print("Division:", divide(20, 5))
print("Is even:", is_even(10))
print("Grade:", get_grade(85))
