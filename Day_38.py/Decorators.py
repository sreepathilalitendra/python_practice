# DAY 38: PYTHON DECORATORS


# LESSON 1: Basic decorator

def my_decorator(func):

    def wrapper():
        print("Function started")
        func()
        print("Function finished")

    return wrapper


@my_decorator
def greet():
    print("Hello, bro!")


greet()


# LESSON 2: Decorator with a different function

def welcome_decorator(func):

    def wrapper():
        print("Welcome!")
        func()

    return wrapper


@welcome_decorator
def show_message():
    print("Learning Python every day!")


show_message()


# LESSON 3: Decorator with arguments

def repeat_decorator(func):

    def wrapper(name):
        print("Starting function")
        func(name)
        print("Function completed")

    return wrapper


@repeat_decorator
def greet_user(name):
    print("Hello,", name)


greet_user("Lalitendra")


# LESSON 4: Decorator with return values

def uppercase_decorator(func):

    def wrapper():
        result = func()
        return result.upper()

    return wrapper


@uppercase_decorator
def get_name():
    return "python developer"


print(get_name())


# LESSON 5: Reusable decorator with *args and **kwargs

def log_decorator(func):

    def wrapper(*args, **kwargs):
        print("Calling function:", func.__name__)
        result = func(*args, **kwargs)
        print("Function completed")
        return result

    return wrapper


@log_decorator
def add(a, b):
    return a + b


print("Result:", add(10, 20))


# LESSON 6: Decorator with multiple arguments

def display_decorator(func):

    def wrapper(*args, **kwargs):
        print("Executing...")
        return func(*args, **kwargs)

    return wrapper


@display_decorator
def student_details(name, course):
    print("Name:", name)
    print("Course:", course)


student_details("Lalitendra", "Diploma CSE")


# LESSON 7: Decorator without @ syntax

def simple_decorator(func):

    def wrapper():
        print("Before")
        func()
        print("After")

    return wrapper


def say_hello():
    print("Hello!")


say_hello = simple_decorator(say_hello)

say_hello()


# LESSON 8: Multiple decorators

def first_decorator(func):

    def wrapper():
        print("First decorator")
        func()

    return wrapper


def second_decorator(func):

    def wrapper():
        print("Second decorator")
        func()

    return wrapper


@first_decorator
@second_decorator
def message():
    print("Python is awesome!")


message()