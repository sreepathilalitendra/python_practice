# CHALLENGE 1: Create cubes of numbers

numbers = [1, 2, 3, 4, 5]

cubes = [number ** 3 for number in numbers]

print("Cubes:", cubes)


# CHALLENGE 2: Find numbers divisible by 3

numbers = [3, 5, 6, 8, 9, 12, 14, 15]

divisible_by_3 = [
    number for number in numbers
    if number % 3 == 0
]

print("Divisible by 3:", divisible_by_3)


# CHALLENGE 3: Get names with more than 4 letters

names = ["Ravi", "Lalitendra", "Anu", "Python"]

long_names = [name for name in names if len(name) > 4]

print("Long names:", long_names)


# CHALLENGE 4: Convert numbers to strings

numbers = [10, 20, 30, 40]

string_numbers = [str(number) for number in numbers]

print("String numbers:", string_numbers)


# CHALLENGE 5: Replace negative numbers with zero

numbers = [-5, 10, -2, 7, -1, 4]

results = [number if number >= 0 else 0 for number in numbers]

print("Updated numbers:", results)


# CHALLENGE 6: Extract the first letter of each word

words = ["Python", "Java", "HTML", "CSS"]

first_letters = [word[0] for word in words]

print("First letters:", first_letters)


# CHALLENGE 7: Calculate squares of even numbers only

numbers = [1, 2, 3, 4, 5, 6, 7, 8]

even_squares = [
    number ** 2 for number in numbers
    if number % 2 == 0
]

print("Even squares:", even_squares)


# CHALLENGE 8: Label numbers as positive or non-positive

numbers = [-3, 0, 4, -1, 8]

labels = [
    "Positive" if number > 0 else "Non-positive"
    for number in numbers
]

print("Labels:", labels)