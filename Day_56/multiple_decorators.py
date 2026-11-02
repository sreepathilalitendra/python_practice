
# Day 56: Multiple Decorators

from functools import wraps


def uppercase(func):

    @wraps(func)
    def wrapper():
        result = func()
        return result.upper()

    return wrapper


def add_message(func):

    @wraps(func)
    def wrapper():
        result = func()
        return f"CodeMonolith: {result}"

    return wrapper


@uppercase
@add_message
def get_message():
    return "learning advanced python"


print(get_message())
