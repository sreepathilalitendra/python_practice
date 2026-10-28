
# Day 51: Advanced String Formatting

# 1. Basic f-strings

name = "Lalitendra"
course = "Diploma CSE"

print(f"Name: {name}")
print(f"Course: {course}")


# 2. Formatting decimal places

price = 123.45678

print(f"Price: {price:.2f}")
print(f"Price: {price:.3f}")


# 3. Formatting numbers with commas

population = 1234567

print(f"Population: {population:,}")


# 4. Formatting percentages

percentage = 0.8567

print(f"Percentage: {percentage:.2%}")


# 5. Aligning text

print(f"{'Python':<15} Left aligned")
print(f"{'Python':>15} Right aligned")
print(f"{'Python':^15} Center aligned")


# 6. Formatting integers with leading zeros

student_id = 42

print(f"Student ID: {student_id:05d}")


# 7. Formatting positive and negative numbers

number = 2500

print(f"Default: {number}")
print(f"With sign: {number:+d}")
print(f"With commas: {number:,}")


# 8. Formatting expressions

a = 15
b = 5

print(f"{a} + {b} = {a + b}")
print(f"{a} * {b} = {a * b}")


# 9. Creating a formatted student report

student_name = "Lalitendra"
marks = 87.456
total_marks = 100

print("\n--- Student Report ---")
print(f"Name       : {student_name}")
print(f"Marks      : {marks:.2f}/{total_marks}")
print(f"Percentage : {marks / total_marks:.2%}")


# 10. Formatting a date and time

from datetime import datetime

now = datetime(2026, 10, 28, 9, 30)

print(f"Date: {now:%d-%m-%Y}")
print(f"Time: {now:%I:%M %p}")
print(f"Full date: {now:%A, %d %B %Y}")
