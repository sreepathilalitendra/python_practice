# Challenge 1: List slicing

numbers = [5, 10, 15, 20, 25, 30, 35]

print("First four:", numbers[:4])
print("Last two:", numbers[-2:])
print("Reversed:", numbers[::-1])


# Challenge 2: Sorting and copying

values = [45, 12, 89, 34, 67]

sorted_values = sorted(values, reverse=True)
copied_values = values.copy()
copied_values.append(100)

print("Descending:", sorted_values)
print("Original:", values)
print("Copy:", copied_values)


# Challenge 3: Dictionary merging

first = {"Python": 80, "Java": 75}
second = {"Java": 90, "SQL": 85}

merged = first | second

print("Merged:", merged)


# Challenge 4: enumerate and zip

languages = ["Python", "Java", "C++"]

for index, language in enumerate(languages, start=1):
    print(index, language)

names = ["Asha", "Ravi", "Kiran"]
marks = [88, 92, 85]

for name, mark in zip(names, marks):
    print(f"{name}: {mark}")


# Challenge 5: Student average

student = {
    "name": "Lalitendra",
    "marks": [85, 90, 88]
}

average = sum(student["marks"]) / len(student["marks"])

print("Student:", student["name"])
print(f"Average: {average:.2f}")
