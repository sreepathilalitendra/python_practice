
# Day 46: Useful Python Standard Library Modules

# 1. math module
import math

print("----- MATH MODULE -----")
print("Square root:", math.sqrt(25))
print("Factorial:", math.factorial(5))
print("Ceiling:", math.ceil(4.2))
print("Floor:", math.floor(4.8))


# 2. random module
import random

print("\n----- RANDOM MODULE -----")
print("Random number:", random.randint(1, 10))

fruits = ["apple", "banana", "mango"]
print("Random fruit:", random.choice(fruits))


# 3. datetime module
import datetime

print("\n----- DATETIME MODULE -----")
today = datetime.date.today()
current_time = datetime.datetime.now()

print("Today's date:", today)
print("Current date and time:", current_time)


# 4. os module
import os

print("\n----- OS MODULE -----")
print("Current working directory:", os.getcwd())
print("Operating system:", os.name)


# 5. pathlib module
from pathlib import Path

print("\n----- PATHLIB MODULE -----")
current_folder = Path.cwd()

print("Current folder:", current_folder)
print("Folder name:", current_folder.name)
print("Is this a directory?", current_folder.is_dir())
