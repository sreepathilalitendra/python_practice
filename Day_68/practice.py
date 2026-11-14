
from itertools import (
    count,
    cycle,
    repeat,
    chain,
    combinations,
    permutations,
    product,
    islice,
    groupby
)


# Challenge 1: count() - First 10 Even Numbers

print("CHALLENGE 1: EVEN NUMBERS")

even_numbers = count(start=2, step=2)

for number in islice(even_numbers, 10):
    print(number)


# Challenge 2: cycle() - Repeat Colors

print("\nCHALLENGE 2: REPEATING COLORS")

colors = ["Red", "Green", "Blue"]

for color in islice(cycle(colors), 9):
    print(color)


# Challenge 3: repeat() - Repeat Text

print("\nCHALLENGE 3: REPEATING TEXT")

for text in repeat("CodeMonolith", 5):
    print(text)


# Challenge 4: chain() - Combine Lists

print("\nCHALLENGE 4: COMBINE LISTS")

list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = [7, 8, 9]

combined = chain(list1, list2, list3)

print(list(combined))


# Challenge 5: combinations() - Language Pairs

print("\nCHALLENGE 5: LANGUAGE COMBINATIONS")

languages = ["Python", "Java", "C", "JavaScript"]

language_pairs = combinations(languages, 2)

for pair in language_pairs:
    print(pair)


# Challenge 6: permutations() - Letter Arrangements

print("\nCHALLENGE 6: LETTER PERMUTATIONS")

letters = ["A", "B", "C"]

arrangements = permutations(letters, 2)

for arrangement in arrangements:
    print(arrangement)


# Challenge 7: product() - Size and Color

print("\nCHALLENGE 7: PRODUCT COMBINATIONS")

sizes = ["Small", "Medium", "Large"]
colors = ["Red", "Blue"]

product_combinations = product(sizes, colors)

for combination in product_combinations:
    print(combination)


# Challenge 8: islice() - Select Numbers

print("\nCHALLENGE 8: ISLICE")

numbers = count(start=1)

selected_numbers = islice(numbers, 4, 10)

print(list(selected_numbers))


# Challenge 9: groupby() - Group Students

print("\nCHALLENGE 9: STUDENT GROUPING")

students = [
    ("Rahul", "Python"),
    ("Kiran", "Python"),
    ("Arjun", "Java"),
    ("Ravi", "Java"),
    ("Suman", "C")
]

for course, group in groupby(
    students,
    key=lambda student: student[1]
):
    student_names = [student[0] for student in group]

    print(course, ":", student_names)


# Challenge 10: Mini Project - Course and Batch Generator

print("\nCHALLENGE 10: COURSE BATCH GENERATOR")

courses = ["Python", "Java", "Web Development"]

batches = ["Morning", "Evening"]

course_batches = product(courses, batches)

for number, (course, batch) in enumerate(
    course_batches,
    start=1
):
    print(f"{number}. Course: {course} | Batch: {batch}")


print("\nDAY 68 CHALLENGES COMPLETED!")
