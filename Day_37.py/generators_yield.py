
# DAY 37: GENERATORS AND YIELD


# LESSON 1: Basic generator

def count_numbers():
    yield 1
    yield 2
    yield 3


numbers = count_numbers()

print(next(numbers))
print(next(numbers))
print(next(numbers))


# LESSON 2: Generator with a for loop

def fruits():
    yield "Apple"
    yield "Banana"
    yield "Mango"


for fruit in fruits():
    print(fruit)


# LESSON 3: Generator with a range

def count_up_to(limit):
    number = 1

    while number <= limit:
        yield number
        number += 1


for number in count_up_to(5):
    print(number)


# LESSON 4: Generate squares

def square_numbers(limit):
    for number in range(1, limit + 1):
        yield number ** 2


for square in square_numbers(5):
    print(square)


# LESSON 5: Generator expression

squares = (number ** 2 for number in range(1, 6))

print(next(squares))
print(next(squares))
print(list(squares))


# LESSON 6: Generator that filters even numbers

def even_numbers(numbers):
    for number in numbers:
        if number % 2 == 0:
            yield number


values = [1, 2, 3, 4, 5, 6]

for number in even_numbers(values):
    print(number)


# LESSON 7: Generator with strings

def get_characters(word):
    for character in word:
        yield character


for character in get_characters("Python"):
    print(character)


# LESSON 8: Generate Fibonacci numbers

def fibonacci(count):
    first = 0
    second = 1

    for _ in range(count):
        yield first

        first, second = second, first + second


for number in fibonacci(8):
    print(number)