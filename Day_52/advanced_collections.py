
# Day 52: Advanced List, Tuple, and Dictionary Operations


# 1. Advanced list slicing

numbers = [10, 20, 30, 40, 50, 60]

print("First three:", numbers[:3])
print("Last three:", numbers[-3:])
print("Every second item:", numbers[::2])
print("Reversed:", numbers[::-1])


# 2. Sorting a list

marks = [78, 95, 62, 88, 70]

marks.sort()
print("Ascending:", marks)

marks.sort(reverse=True)
print("Descending:", marks)


# 3. Copying a list

original = [1, 2, 3]
copied = original.copy()

copied.append(4)

print("Original:", original)
print("Copied:", copied)


# 4. List unpacking

student = ["Lalitendra", 18, "Diploma CSE"]

name, age, course = student

print("Name:", name)
print("Age:", age)
print("Course:", course)


# 5. Tuple unpacking

coordinates = (25, 40)

x, y = coordinates

print("X:", x)
print("Y:", y)


# 6. Tuple methods

colors = ("red", "blue", "green", "blue")

print("Blue count:", colors.count("blue"))
print("Blue index:", colors.index("blue"))


# 7. Dictionary get()

student_marks = {
    "Python": 90,
    "Java": 85,
    "SQL": 88
}

print("Python marks:", student_marks.get("Python"))
print("C marks:", student_marks.get("C", "Not found"))


# 8. Updating a dictionary

student_marks.update({
    "Java": 92,
    "HTML": 80
})

print("Updated marks:", student_marks)


# 9. Merging dictionaries

first = {"name": "Lalitendra", "course": "CSE"}
second = {"city": "Hyderabad", "year": 2026}

combined = first | second

print("Combined:", combined)


# 10. enumerate()

languages = ["Python", "Java", "C++"]

for index, language in enumerate(languages, start=1):
    print(index, language)


# 11. zip()

names = ["Asha", "Ravi", "Kiran"]
scores = [90, 85, 92]

for name, score in zip(names, scores):
    print(f"{name}: {score}")


# 12. Practical student report using a dictionary

student = {
    "name": "Lalitendra",
    "course": "Diploma CSE",
    "marks": [85, 90, 88]
}

average = sum(student["marks"]) / len(student["marks"])

print("\n--- Student Report ---")
print("Name:", student["name"])
print("Course:", student["course"])
print("Marks:", student["marks"])
print(f"Average: {average:.2f}")
