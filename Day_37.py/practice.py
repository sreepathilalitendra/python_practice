# CHALLENGE 1: Generate numbers from 1 to 10

def numbers_generator():
    for number in range(1, 11):
        yield number


for number in numbers_generator():
    print(number)


# CHALLENGE 2: Generate cubes

def cubes_generator(limit):
    for number in range(1, limit + 1):
        yield number ** 3


print(list(cubes_generator(5)))


# CHALLENGE 3: Generate odd numbers

def odd_numbers_generator(numbers):
    for number in numbers:
        if number % 2 != 0:
            yield number


print(list(odd_numbers_generator([1, 2, 3, 4, 5, 6, 7])))


# CHALLENGE 4: Generate word lengths

def word_lengths(words):
    for word in words:
        yield len(word)


print(list(word_lengths(["Python", "Java", "HTML"])))


# CHALLENGE 5: Generate multiplication table

def multiplication_table(number):
    for multiplier in range(1, 11):
        yield f"{number} x {multiplier} = {number * multiplier}"


for line in multiplication_table(5):
    print(line)


# CHALLENGE 6: Generate Fibonacci numbers

def fibonacci_generator(count):
    first = 0
    second = 1

    for _ in range(count):
        yield first
        first, second = second, first + second


print(list(fibonacci_generator(10)))


# CHALLENGE 7: Generate positive numbers only

def positive_numbers(numbers):
    for number in numbers:
        if number > 0:
            yield number


print(list(positive_numbers([-3, 5, 0, 8, -1, 2])))


# CHALLENGE 8: Generate uppercase words

def uppercase_words(words):
    for word in words:
        yield word.upper()


print(list(uppercase_words(["python", "coding", "developer"])))