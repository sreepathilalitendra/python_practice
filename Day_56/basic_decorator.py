
# Day 56: Decorator with Function Arguments

from functools import wraps


def log_function(func):

    @wraps(func)
    def wrapper(*args, **kwargs):

        print(f"Calling function: {func.__name__}")

        result = func(*args, **kwargs)

        print("Function execution completed")

        return result

    return wrapper


@log_function
def add(a, b):
    return a + b


@log_function
def introduce(name, city):
    return f"My name is {name} and I am from {city}."


print("Addition:", add(10, 20))

print("\nIntroduction:")
print(introduce("Lalitendra", "Hyderabad"))
