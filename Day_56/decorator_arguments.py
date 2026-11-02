
# Day 56: Decorators with Arguments

from functools import wraps


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
def greet(name):
    print(f"Hello, {name}!")


greet("Lalitendra")
