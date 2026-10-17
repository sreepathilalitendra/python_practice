
# DAY 40: RECURSION IN PYTHON


# LESSON 1: Simple recursion

def say_hello(number):
    if number == 0:
        return

    print("Hello Python!")
    say_hello(number - 1)


say_hello(3)


# LESSON 2: Countdown

def countdown(number):
    if number == 0:
        print("Done!")
        return

    print(number)
    countdown(number - 1)


countdown(5)


# LESSON 3: Sum of numbers from 1 to n

def sum_numbers(number):
    if number == 0:
        return 0

    return number + sum_numbers(number - 1)


print("Sum:", sum_numbers(5))


# LESSON 4: Factorial

def factorial(number):
    if number < 0:
        raise ValueError("Number must be non-negative")

    if number == 0 or number == 1:
        return 1

    return number * factorial(number - 1)


print("Factorial:", factorial(5))


# LESSON 5: Power of a number

def power(base, exponent):
    if exponent < 0:
        raise ValueError("Exponent must be non-negative")

    if exponent == 0:
        return 1

    return base * power(base, exponent - 1)


print("Power:", power(2, 4))


# LESSON 6: Fibonacci sequence

def fibonacci(number):
    if number < 0:
        raise ValueError("Number must be non-negative")

    if number == 0:
        return 0

    if number == 1:
        return 1

    return fibonacci(number - 1) + fibonacci(number - 2)


for number in range(7):
    print(fibonacci(number))


# LESSON 7: Sum of digits

def sum_of_digits(number):
    number = abs(number)

    if number < 10:
        return number

    return number % 10 + sum_of_digits(number // 10)


print("Digit sum:", sum_of_digits(1234))


# LESSON 8: Reverse a string

def reverse_string(text):
    if len(text) <= 1:
        return text

    return reverse_string(text[1:]) + text[0]


print("Reversed:", reverse_string("Python"))