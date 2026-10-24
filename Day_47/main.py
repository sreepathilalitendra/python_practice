
# Day 47: Regular Expressions (Regex) Basics

import re

text = "My name is Lalitendra. My roll number is 12345."

# 1. re.search() - Find the first match
result = re.search("Lalitendra", text)

print("----- SEARCH -----")
if result:
    print("Match found:", result.group())
else:
    print("No match found")


# 2. re.findall() - Find all numbers
numbers = re.findall(r"\d+", text)

print("\n----- FINDALL -----")
print("Numbers found:", numbers)


# 3. re.match() - Match at the beginning
result = re.match("My", text)

print("\n----- MATCH -----")
if result:
    print("Match found:", result.group())
else:
    print("No match at the beginning")


# 4. re.sub() - Replace matching text
new_text = re.sub("Lalitendra", "Python Learner", text)

print("\n----- SUBSTITUTE -----")
print(new_text)


# 5. Search for all words starting with M
words = re.findall(r"\bM\w*", text)

print("\n----- WORD PATTERN -----")
print("Words starting with M:", words)
