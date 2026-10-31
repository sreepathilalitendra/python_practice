
# Day 54: Comprehension Review

# 1. List comprehension

numbers = [1, 2, 3, 4, 5]

squares = [number ** 2 for number in numbers]

print("Squares:", squares)


# 2. List comprehension with condition

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_numbers = [number for number in numbers if number % 2 == 0]

print("Even numbers:", even_numbers)


# 3. List comprehension with if-else

results = [
    "Even" if number % 2 == 0 else "Odd"
    for number in numbers
]

print("Even or Odd:", results)


# 4. String comprehension

names = ["sree", "arun", "kiran", "balu"]

uppercase_names = [name.upper() for name in names]

print("Uppercase names:", uppercase_names)


# 5. Nested list comprehension

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

flattened = [number for row in matrix for number in row]

print("Flattened list:", flattened)


# 6. Dictionary comprehension

numbers = [1, 2, 3, 4, 5]

number_squares = {
    number: number ** 2
    for number in numbers
}

print("Dictionary:", number_squares)


# 7. Set comprehension

numbers = [1, 2, 2, 3, 3, 4, 5]

unique_squares = {number ** 2 for number in numbers}

print("Unique squares:", unique_squares)
