# Challenge 1: Greeting function

def greet(name):
    return f"Hello, {name}!"


if __name__ == "__main__":
    print(greet("Lalitendra"))


# Challenge 2: Calculator functions

def add(a, b):
    return a + b


def multiply(a, b):
    return a * b


if __name__ == "__main__":
    print("Addition:", add(10, 5))
    print("Multiplication:", multiply(10, 5))


# Challenge 3: Check __name__

print("Current module name:", __name__)


# Challenge 4: Square function

def square(number):
    return number ** 2


if __name__ == "__main__":
    print("Square:", square(6))