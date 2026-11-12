def square(number):
    return number * number


numbers = [1, 2, 3, 4, 5]

result = map(square, numbers)

print(list(result))