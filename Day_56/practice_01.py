
from functools import wraps
import time


# Challenge 1: Decorator before and after function execution

def my_decorator(func):

    @wraps(func)
    def wrapper(*args, **kwargs):

        print("Before function execution")

        result = func(*args, **kwargs)

        print("After function execution")

        return result

    return wrapper


@my_decorator
def greet():
    print("Hello Python!")


print("Challenge 1:")
greet()


# Challenge 2: Decorator supporting *args and **kwargs

def log_function(func):

    @wraps(func)
    def wrapper(*args, **kwargs):

        print("Function:", func.__name__)

        return func(*args, **kwargs)

    return wrapper


@log_function
def add(a, b):
    return a + b


print("\nChallenge 2:")
print("Addition:", add(10, 20))


# Challenge 3: Preserve function name and documentation

def preserve_metadata(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)

    return wrapper


@preserve_metadata
def student_details():
    """Displays student details."""
    print("Student: Lalitendra")


print("\nChallenge 3:")
student_details()
print("Function name:", student_details.__name__)
print("Documentation:", student_details.__doc__)


# Challenge 4: Repeat a function three times

def repeat(times):

    def decorator(func):

        @wraps(func)
        def wrapper(*args, **kwargs):

            for count in range(times):
                print(f"Execution {count + 1}:")
                func(*args, **kwargs)

        return wrapper

    return decorator


@repeat(3)
def welcome():
    print("Welcome to CodeMonolith!")


print("\nChallenge 4:")
welcome()


# Challenge 5: Convert returned string into uppercase

def uppercase_result(func):

    @wraps(func)
    def wrapper(*args, **kwargs):

        result = func(*args, **kwargs)

        if isinstance(result, str):
            return result.upper()

        return result

    return wrapper


@uppercase_result
def message():
    return "learning advanced python"


print("\nChallenge 5:")
print(message())


# Challenge 6: Apply two decorators

def uppercase(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs).upper()

    return wrapper


def add_prefix(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        return "CODEMONOLITH: " + func(*args, **kwargs)

    return wrapper


@uppercase
@add_prefix
def get_message():
    return "python is interesting"


print("\nChallenge 6:")
print(get_message())


# Challenge 7: Measure function execution time

def execution_timer(func):

    @wraps(func)
    def wrapper(*args, **kwargs):

        start = time.perf_counter()

        result = func(*args, **kwargs)

        end = time.perf_counter()

        print(f"Execution time: {end - start:.6f} seconds")

        return result

    return wrapper


@execution_timer
def calculate_sum():
    return sum(range(1, 100001))


print("\nChallenge 7:")
print("Total:", calculate_sum())
