
# Day 56: functools.wraps

from functools import wraps


def my_decorator(func):

    @wraps(func)
    def wrapper():
        print("Executing function...")
        return func()

    return wrapper


@my_decorator
def greet():
    """This function displays a greeting."""
    print("Hello from CodeMonolith!")


greet()

print("\nFunction name:", greet.__name__)
print("Documentation:", greet.__doc__)
