
# DAY 34: LIST COMPREHENSION


# LESSON 1: Create a list of squares

numbers = [1, 2, 3, 4, 5]

squares = [number ** 2 for number in numbers]

print("Squares:", squares)


# LESSON 2: Create a list of even numbers

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_numbers = [number for number in numbers if number % 2 == 0]

print("Even numbers:", even_numbers)


# LESSON 3: Create a list of odd numbers

odd_numbers = [number for number in numbers if number % 2 != 0]

print("Odd numbers:", odd_numbers)


# LESSON 4: Convert strings to uppercase

names = ["lalitendra", "python", "coding"]

uppercase_names = [name.upper() for name in names]

print("Uppercase:", uppercase_names)


# LESSON 5: Filter numbers greater than 5

numbers = [2, 5, 7, 9, 3, 10, 4]

greater_numbers = [number for number in numbers if number > 5]

print("Numbers greater than 5:", greater_numbers)


# LESSON 6: If-else inside list comprehension

numbers = [1, 2, 3, 4, 5, 6]

results = [
    "Even" if number % 2 == 0 else "Odd"
    for number in numbers
]

print("Results:", results)


# LESSON 7: Convert temperatures from Celsius to Fahrenheit

celsius = [0, 10, 20, 30, 40]

fahrenheit = [
    (temperature * 9 / 5) + 32
    for temperature in celsius
]
print("Fahrenheit:", fahrenheit)




# LESSON 8: Extract word lengths
words = ["Python", "Java", "HTML", "JavaScript"]
lengths = [len(word) for word in words]
print("Word lengths:", lengths)
print("Word lengths:", lengths)