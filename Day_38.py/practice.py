# CHALLENGE 1: Print a message before a function

def before_decorator(func):

    def wrapper():
        print("Starting...")
        func()

    return wrapper


@before_decorator
def task():
    print("Task completed")


task()


# CHALLENGE 2: Convert returned text to uppercase

def uppercase_decorator(func):

    def wrapper():
        return func().upper()

    return wrapper


@uppercase_decorator
def get_language():
    return "python"


print(get_language())


# CHALLENGE 3: Log function calls and return the result

def log_decorator(func):

    def wrapper(*args, **kwargs):
        print("Function:", func.__name__)
        return func(*args, **kwargs)

    return wrapper


@log_decorator
def multiply(a, b):
    return a * b


print(multiply(5, 4))


# CHALLENGE 4: Repeat a message three times

def repeat_three_times(func):

    def wrapper(*args, **kwargs):
        for _ in range(3):
            func(*args, **kwargs)

    return wrapper


@repeat_three_times
def say_hello():
    print("Hello, bro!")


say_hello()


# CHALLENGE 5: Decorator for a greeting

def greeting_decorator(func):

    def wrapper(name):
        print("Welcome!")
        return func(name)

    return wrapper


@greeting_decorator
def greet(name):
    print("Hello,", name)


greet("Ravi")


# CHALLENGE 6: Measure execution time

import time


def timer_decorator(func):

    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()

        print("Execution time:", end - start, "seconds")

        return result

    return wrapper


@timer_decorator
def calculate_sum():
    return sum(range(100000))


print("Sum:", calculate_sum())


# CHALLENGE 7: Decorator that checks a positive number

def positive_decorator(func):

    def wrapper(number):
        if number <= 0:
            print("Please provide a positive number")
            return None

        return func(number)

    return wrapper


@positive_decorator
def square(number):
    return number ** 2


print(square(5))
print(square(-3))


# CHALLENGE 8: Decorator that displays the result

def result_decorator(func):

    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print("Result:", result)
        return result

    return wrapper


@result_decorator
def subtract(a, b):
    return a - b


subtract(20, 8)