# Day 18 - Dictionaries


# 1. Creating a Dictionary

student = {
    "name": "Sreepathi Lalitendra",
    "age": 18,
    "course": "Diploma CSE"
}
print(student)


# 2. Accessing Values

student = {
    "name": "Sreepathi Lalitendra",
    "age": 18,
    "course": "Diploma CSE"
}
print(student["name"])
print(student["age"])


# 3. Adding a New Item

student = {
    "name": "Sreepathi Lalitendra",
    "age": 18
}
student["city"] = "Hyderabad"
print(student)


# 4. Changing a Value

student = {
    "name": "Sreepathi Lalitendra",
    "age": 18
}
student["age"] = 19
print(student)


# 5. Removing an Item - pop()

student = {
    "name": "Sreepathi Lalitendra",
    "age": 18,
    "city": "Hyderabad"
}
student.pop("city")
print(student)


# 6. Checking a Key - in

student = {
    "name": "Sreepathi Lalitendra",
    "age": 18
}
print("name" in student)
print("city" in student)


# 7. Dictionary Length - len()

student = {
    "name": "Sreepathi Lalitendra",
    "age": 18,
    "course": "Diploma CSE"
}
print(len(student))


# 8. Looping Through Keys

student = {
    "name": "Sreepathi Lalitendra",
    "age": 18,
    "course": "Diploma CSE"
}
for key in student:
    print(key)


# 9. Looping Through Values - values()

student = {
    "name": "Sreepathi Lalitendra",
    "age": 18,
    "course": "Diploma CSE"
}
for value in student.values():
    print(value)


# 10. Looping Through Keys and Values - items()

student = {
    "name": "Sreepathi Lalitendra",
    "age": 18,
    "course": "Diploma CSE"
}
for key, value in student.items():
    print(key, value)