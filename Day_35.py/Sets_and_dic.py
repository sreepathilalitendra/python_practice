
# DAY 35: SET AND DICTIONARY COMPREHENSIONS


# LESSON 1: Set comprehension

numbers = [1, 2, 2, 3, 3, 4, 5]

unique_numbers = {number for number in numbers}

print("Unique numbers:", unique_numbers)


# LESSON 2: Set comprehension with a condition

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_numbers = {
    number for number in numbers
    if number % 2 == 0
}

print("Even numbers:", even_numbers)


# LESSON 3: Create a set of uppercase names

names = ["ravi", "anu", "ravi", "python"]

uppercase_names = {name.upper() for name in names}

print("Uppercase names:", uppercase_names)


# LESSON 4: Dictionary comprehension for squares

numbers = [1, 2, 3, 4, 5]

squares = {
    number: number ** 2
    for number in numbers
}

print("Squares:", squares)


# LESSON 5: Dictionary comprehension with a condition

numbers = [1, 2, 3, 4, 5, 6, 7, 8]

even_squares = {
    number: number ** 2
    for number in numbers
    if number % 2 == 0
}

print("Even squares:", even_squares)


# LESSON 6: Create a dictionary from two lists

names = ["Ravi", "Anu", "Kiran"]
ages = [18, 19, 20]

people = {
    names[index]: ages[index]
    for index in range(len(names))
}

print("People:", people)


# LESSON 7: Convert prices to discounted prices

prices = {
    "Book": 200,
    "Pen": 50,
    "Bag": 800
}

discounted_prices = {
    item: price * 0.90
    for item, price in prices.items()
}

print("Discounted prices:", discounted_prices)


# LESSON 8: Convert words into a length dictionary

words = ["Python", "Java", "HTML"]

word_lengths = {
    word: len(word)
    for word in words
}

print("Word lengths:", word_lengths)