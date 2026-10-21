# Day 44: __name__ == "__main__"

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


if __name__ == "__main__":
    print("Calculator is running directly")

    print("Addition:", add(10, 5))
    print("Subtraction:", subtract(10, 5))