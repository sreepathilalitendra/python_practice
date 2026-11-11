# Challenge 1: Pure Function

def multiply(a, b):
    return a * b


result = multiply(10, 5)

print("Challenge 1")
print("Result:", result)


print("\n------------------------------\n")


# Challenge 2: First-Class Function

def welcome():
    return "Welcome to CodeMonolith!"


# Store function in a variable
message = welcome

# Call function using variable
print("Challenge 2")
print(message())


print("\n------------------------------\n")


# Challenge 3: Function as Argument

def square(number):
    return number * number


def display(function, number):
    result = function(number)
    print("Result:", result)


print("Challenge 3")
display(square, 8)


print("\n------------------------------\n")


# Challenge 4: Higher-Order Function

def double(number):
    return number * 2


def triple(number):
    return number * 3


def calculate(function, number):
    return function(number)


print("Challenge 4")
print(calculate(double, 10))
print(calculate(triple, 10))


print("\n------------------------------\n")


# Challenge 5: Immutability

numbers = [10, 20, 30]

new_numbers = numbers + [40]

print("Challenge 5")
print("Original:", numbers)
print("New List:", new_numbers)


print("\n------------------------------\n")


# Challenge 6: Functional Programming Mini Project

def calculate_square(number):
    return number * number


def process_numbers(function, numbers):
    results = []

    for number in numbers:
        results.append(function(number))

    return results


original_numbers = [2, 4, 6, 8, 10]

squared_numbers = process_numbers(
    calculate_square,
    original_numbers
)


print("Challenge 6")
print("Original:", original_numbers)
print("Squared:", squared_numbers)
