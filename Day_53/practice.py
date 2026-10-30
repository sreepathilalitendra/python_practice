# Challenge 1: Sort by length

words = [
    "Developer",
    "Python",
    "AI",
    "Programming",
    "Code"
]

print(sorted(words, key=len))


# Challenge 2: Sort by absolute value

numbers = [-50, 10, -5, 30, -20]

print(sorted(numbers, key=abs))


# Challenge 3: Sort students by highest marks

students = [
    ("Asha", 85),
    ("Ravi", 95),
    ("Kiran", 75),
    ("Arjun", 90)
]

result = sorted(
    students,
    key=lambda student: student[1],
    reverse=True
)

print(result)


# Challenge 4: Sort employee records by salary

employees = [
    {"name": "Asha", "salary": 30000},
    {"name": "Ravi", "salary": 45000},
    {"name": "Kiran", "salary": 25000}
]

result = sorted(
    employees,
    key=lambda employee: employee["salary"]
)

for employee in result:
    print(employee)


# Challenge 5: Sort by marks, then name

students = [
    ("Ravi", 90),
    ("Asha", 90),
    ("Kiran", 85),
    ("Arjun", 85)
]

result = sorted(
    students,
    key=lambda student: (-student[1], student[0])
)

print(result)
