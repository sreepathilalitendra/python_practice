# Challenge 1 - Random Number
import random

number = random.randint(1, 100)

print(number)


# Challenge 2 - Random Number from Range
number = random.randrange(1, 20)

print(number)


# Challenge 3 - Random Decimal
number = random.random()

print(number)


# Challenge 4 - Random Choice
languages = ["Python", "Java", "C", "C++", "JavaScript"]

language = random.choice(languages)

print(language)


# Challenge 5 - Shuffle Numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

random.shuffle(numbers)

print(numbers)


# Challenge 6 - Random Color
colors = ["Red", "Green", "Blue", "Yellow", "Purple"]

color = random.choice(colors)

print(color)


# Challenge 7 - Random Even Number
even_number = random.randrange(2, 21, 2)

print(even_number)


# Challenge 8 - Random Student
students = ["Rahul", "Arjun", "Sreepathi", "Kiran", "Ravi"]

student = random.choice(students)

print(student)


# Challenge 9 - Random Dice
dice = random.randint(1, 6)

print("Dice:", dice)


# Challenge 10 - Random Password Character
characters = ["A", "B", "C", "1", "2", "3"]

character = random.choice(characters)

print("Random character:", character)