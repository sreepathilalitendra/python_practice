
# Day 47: Regex Challenge

import re

# Challenge 1: Find all numbers
text1 = "I have 12 books and 5 pens."
print("Numbers:", re.findall(r"\d+", text1))


# Challenge 2: Find all words
text2 = "Python is easy to learn."
print("Words:", re.findall(r"\b\w+\b", text2))


# Challenge 3: Find all words starting with P
text3 = "Python Programming is Powerful"
print("Words starting with P:", re.findall(r"\bP\w*", text3))


# Challenge 4: Replace all spaces with hyphens
text4 = "learn python every day"
print("Updated text:", re.sub(r"\s+", "-", text4))
