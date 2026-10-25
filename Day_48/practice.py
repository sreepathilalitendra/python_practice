
# Day 48: Regex Challenge

import re

# Challenge 1: Extract username and domain
email = "student@example.com"

result = re.search(r"([\w.-]+)@([\w.-]+)", email)

if result:
    print("Username:", result.group(1))
    print("Domain:", result.group(2))


# Challenge 2: Find all dates in the text
text = "Events: 25-10-2026 and 01-11-2026"

dates = re.findall(r"\d{2}-\d{2}-\d{4}", text)
print("Dates:", dates)


# Challenge 3: Replace all digits with *
text = "Python123 is fun456"

updated = re.sub(r"\d", "*", text)
print("Updated text:", updated)


# Challenge 4: Find numbers and their positions
text = "A10 B20 C30"

for match in re.finditer(r"\d+", text):
    print("Number:", match.group(), "Position:", match.start())


# Challenge 5: Use a compiled pattern
pattern = re.compile(r"\bcat\b", re.IGNORECASE)

text = "Cat and cat are animals. category is another word."

print("Cat matches:", pattern.findall(text))
