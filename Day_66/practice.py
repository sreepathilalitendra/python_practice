# Challenge 1: map()
# Calculate cubes of numbers

numbers = [1, 2, 3, 4, 5]

cubes = list(map(lambda number: number ** 3, numbers))

print("Challenge 1: Cubes")
print(cubes)


print("\n------------------------------\n")


# Challenge 2: filter()
# Find odd numbers

numbers = [10, 15, 20, 25, 30, 35, 40, 45]

odd_numbers = list(
    filter(lambda number: number % 2 != 0, numbers)
)

print("Challenge 2: Odd Numbers")
print(odd_numbers)


print("\n------------------------------\n")


# Challenge 3: zip()
# Combine students and marks

students = ["Rahul", "Arjun", "Kiran"]

marks = [85, 90, 95]

student_data = zip(students, marks)

print("Challenge 3: Student Marks")

for name, mark in student_data:
    print(name, "-", mark)


print("\n------------------------------\n")


# Challenge 4: enumerate()
# Display subjects with numbering

subjects = ["Python", "Java", "DBMS", "OS"]

print("Challenge 4: Subjects")

for index, subject in enumerate(subjects, start=1):
    print(index, subject)


print("\n------------------------------\n")


# Challenge 5: map() + filter()
# Multiply by 2 and select values greater than 15

numbers = [2, 5, 8, 10, 12, 15]

doubled_numbers = map(
    lambda number: number * 2,
    numbers
)

filtered_numbers = list(
    filter(lambda number: number > 15, doubled_numbers)
)

print("Challenge 5: Filtered Numbers")
print(filtered_numbers)


print("\n------------------------------\n")


# Challenge 6: Student Marks Mini Project
# Combine zip(), enumerate(), and filter()

names = ["Rahul", "Arjun", "Kiran", "Ravi"]

marks = [85, 35, 90, 40]

student_data = zip(names, marks)

passed_students = filter(
    lambda student: student[1] >= 40,
    student_data
)

print("Challenge 6: Student Results")
print("Passed Students")

for index, (name, mark) in enumerate(passed_students, start=1):
    print(index, name, "-", mark)
