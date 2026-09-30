# Day 23 - Random Module

import random


# random.randint()
number = random.randint(1, 10)
print(number)


# random.randrange()
number = random.randrange(1, 10)
print(number)


# random.random()
number = random.random()
print(number)


# random.choice()
languages = ["Python", "Java", "C", "C++"]

language = random.choice(languages)

print(language)


# random.shuffle()
numbers = [1, 2, 3, 4, 5]

random.shuffle(numbers)

print(numbers)