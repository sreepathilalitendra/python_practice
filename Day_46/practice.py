import math
import random
from datetime import date
from pathlib import Path

# Challenge 1: Math
number = 49
print("Square root:", math.sqrt(number))

# Challenge 2: Random number
print("Lucky number:", random.randint(1, 100))

# Challenge 3: Today's date
print("Today's date:", date.today())

# Challenge 4: Current folder name
print("Folder name:", Path.cwd().name)
