# Day 18 - Dictionary Practice


# Creating a Dictionary

student = {
    "name": "Sreepathi Lalitendra",
    "age": 18,
    "course": "Diploma CSE"
}
print(student)


# Accessing Values

print(student["name"])
print(student["course"])


# Adding a New Item

student["city"] = "Hyderabad"
print(student)


# Changing a Value

student["age"] = 19
print(student)


# Removing an Item

student.pop("city")
print(student)


# Checking a Key

print("name" in student)


# Dictionary Length

print(len(student))


# Looping Through Keys

for key in student:
    print(key)


# Looping Through Values

for value in student.values():
    print(value)


# Looping Through Keys and Values

student = {
    "name": "Sreepathi Lalitendra",
    "age": 18,
    "course": "Diploma CSE"
}

for key, value in student.items():
    print(key, value)