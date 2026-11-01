
# Day 55: Generator Functions

def generate_numbers():

    print("Generating first number")
    yield 10

    print("Generating second number")
    yield 20

    print("Generating third number")
    yield 30


numbers = generate_numbers()

print(next(numbers))
print(next(numbers))
print(next(numbers))
