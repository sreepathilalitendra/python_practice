
# Day 48: Regex Groups, Substitution and Advanced Patterns

import re

# 1. Capturing groups
text = "Name: Lalitendra, Age: 18"

result = re.search(r"Name: (\w+), Age: (\d+)", text)

print("----- CAPTURING GROUPS -----")
if result:
    print("Complete match:", result.group(0))
    print("Name:", result.group(1))
    print("Age:", result.group(2))


# 2. Named capturing groups
text = "Email: learner@example.com"

result = re.search(
    r"Email: (?P<email>[\w.-]+@[\w.-]+\.\w+)",
    text
)

print("\n----- NAMED GROUPS -----")
if result:
    print("Email:", result.group("email"))


# 3. re.finditer() - Find matches and their positions
text = "Python 123, Java 456, C++ 789"

print("\n----- FINDITER -----")
for result in re.finditer(r"\d+", text):
    print("Number:", result.group(), "| Position:", result.start())


# 4. re.sub() - Replace a pattern
text = "Contact me at 9876543210 or 9123456780"

updated_text = re.sub(r"\d{10}", "[PHONE]", text)

print("\n----- SUBSTITUTION -----")
print(updated_text)


# 5. re.compile() - Reuse a pattern
pattern = re.compile(r"\b[A-Z][a-z]+\b")

text = "Python is Easy and Java is Popular"

print("\n----- COMPILED PATTERN -----")
print(pattern.findall(text))


# 6. Case-insensitive matching
text = "Python python PYTHON"

print("\n----- IGNORE CASE -----")
print(re.findall(r"python", text, re.IGNORECASE))
