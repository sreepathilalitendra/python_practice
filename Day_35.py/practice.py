# CHALLENGE 1: Get unique odd numbers

numbers = [1, 3, 3, 4, 5, 5, 7, 8]

unique_odds = {
    number for number in numbers
    if number % 2 != 0
}

print("Unique odd numbers:", unique_odds)


# CHALLENGE 2: Get words longer than 4 letters

words = ["Python", "Java", "HTML", "JavaScript"]

long_words = {
    word for word in words
    if len(word) > 4
}

print("Long words:", long_words)


# CHALLENGE 3: Create a square dictionary

numbers = [2, 4, 6, 8]

square_dict = {
    number: number ** 2
    for number in numbers
}

print("Square dictionary:", square_dict)


# CHALLENGE 4: Keep only passing marks (35 and above)

marks = {
    "Ravi": 75,
    "Anu": 28,
    "Kiran": 45,
    "Sita": 32
}

passed_students = {
    name: mark
    for name, mark in marks.items()
    if mark >= 35
}

print("Passed students:", passed_students)


# CHALLENGE 5: Create a dictionary of word lengths

words = ["cat", "python", "code", "developer"]

length_dict = {
    word: len(word)
    for word in words
}

print("Word lengths:", length_dict)


# CHALLENGE 6: Convert Celsius to Fahrenheit

celsius_values = [0, 10, 20, 30, 40]

fahrenheit_values = {
    celsius: (celsius * 9 / 5) + 32
    for celsius in celsius_values
}

print("Temperatures:", fahrenheit_values)


# CHALLENGE 7: Get unique first letters

words = ["apple", "ant", "banana", "ball", "cat"]

first_letters = {
    word[0] for word in words
}

print("First letters:", first_letters)


# CHALLENGE 8: Increase each price by 10%

prices = {
    "Book": 100,
    "Pen": 20,
    "Bag": 500
}

updated_prices = {
    item: price * 1.10
    for item, price in prices.items()
}

print("Updated prices:", updated_prices)