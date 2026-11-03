
# Day 57: Context Manager with Exception Handling

from contextlib import contextmanager


@contextmanager
def safe_operation():

    print("Operation started")

    try:
        yield
    except ValueError as error:
        print("Handled error:", error)
    finally:
        print("Operation completed")


with safe_operation():
    print("Inside the operation")
    raise ValueError("Something went wrong")

print("Program continues normally")
