import time
from functools import wraps


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

    total = sum(range(1, 100001))

    return total


print("Total:", calculate_sum())