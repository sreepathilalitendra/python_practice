
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


# Example 1: count()

print("EXAMPLE 1: COUNT")

numbers = count(start=1, step=2)

for number in islice(numbers, 5):
    print(number)


# Example 2: cycle()

print("\nEXAMPLE 2: CYCLE")

colors = ["Red", "Green", "Blue"]

for color in islice(cycle(colors), 7):
    print(color)


# Example 3: repeat()

print("\nEXAMPLE 3: REPEAT")

for value in repeat("Python", 4):
    print(value)


# Example 4: chain()

print("\nEXAMPLE 4: CHAIN")

numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]
numbers3 = [7, 8, 9]

result = chain(numbers1, numbers2, numbers3)

print(list(result))


# Example 5: islice()

print("\nEXAMPLE 5: ISLICE")

numbers = count(10)

result = list(islice(numbers, 2, 8))

print(result)


# Example 6: combinations()

print("\nEXAMPLE 6: COMBINATIONS")

subjects = ["Python", "Java", "C"]

result = combinations(subjects, 2)

for item in result:
    print(item)


# Example 7: permutations()

print("\nEXAMPLE 7: PERMUTATIONS")

letters = ["A", "B", "C"]

result = permutations(letters, 2)

for item in result:
    print(item)


# Example 8: product()

print("\nEXAMPLE 8: PRODUCT")

sizes = ["Small", "Large"]
colors = ["Red", "Blue"]

result = product(sizes, colors)

for item in result:
    print(item)


# Example 9: groupby()

print("\nEXAMPLE 9: GROUPBY")

students = [
    ("Rahul", "Python"),
    ("Kiran", "Python"),
    ("Arjun", "Java"),
    ("Ravi", "Java"),
    ("Suman", "C")
]

for subject, group in groupby(
    students,
    key=lambda student: student[1]
):
    names = [student[0] for student in group]

    print(subject, ":", names)


# Mini Project: Product Combination Generator

print("\nMINI PROJECT: PRODUCT GENERATOR")

product_sizes = ["Small", "Medium", "Large"]

product_colors = ["Red", "Blue", "Black"]

combinations_result = product(
    product_sizes,
    product_colors
)

for number, item in enumerate(
    combinations_result,
    start=1
):
    print(number, item)


# Display first 4 combinations

print("\nFIRST 4 COMBINATIONS")

limited_result = islice(
    product(product_sizes, product_colors),
    4
)

for item in limited_result:
    print(item)


print("\nDAY 68 MAIN LESSON COMPLETED!")
