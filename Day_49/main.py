
# Day 49: JSON in Python

import json

# 1. Python dictionary
student = {
    "name": "Lalitendra",
    "age": 18,
    "course": "Diploma CSE",
    "skills": ["Python", "Java", "SQL"],
    "is_student": True
}

print("----- PYTHON DICTIONARY -----")
print(student)


# 2. json.dumps() - Convert Python data to a JSON string
json_text = json.dumps(student, indent=4)

print("\n----- PYTHON TO JSON -----")
print(json_text)


# 3. json.loads() - Convert a JSON string to Python data
python_data = json.loads(json_text)

print("\n----- JSON TO PYTHON -----")
print("Name:", python_data["name"])
print("Course:", python_data["course"])
print("Skills:", python_data["skills"])


# 4. json.dump() - Write JSON data to a file
with open("student.json", "w", encoding="utf-8") as file:
    json.dump(student, file, indent=4)

print("\nJSON data saved to student.json")


# 5. json.load() - Read JSON data from a file
with open("student.json", "r", encoding="utf-8") as file:
    loaded_student = json.load(file)

print("\n----- DATA READ FROM FILE -----")
print("Name:", loaded_student["name"])
print("Age:", loaded_student["age"])
print("Is student:", loaded_student["is_student"])
