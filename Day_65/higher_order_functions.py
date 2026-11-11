def square(number):
    return number * number


def calculate(function, value):
    return function(value)


result = calculate(square, 6)

print("Result:", result)