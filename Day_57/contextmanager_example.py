
# Day 57: contextmanager Decorator

from contextlib import contextmanager


@contextmanager
def my_context():

    print("Starting the context")

    try:
        yield "Context is active"

    finally:
        print("Cleaning up the context")


with my_context() as message:
    print(message)
