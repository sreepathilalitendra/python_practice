# Day 7 - If, Else and Elif


# if statement
age = 18
if age >= 18:
    print("You are eligible to vote.")


# if with comparison operators
marks = 80
if marks >= 40:
    print("You have passed the exam.")


# if-else statement
marks = 30
if marks >= 40:
    print("You have passed the exam.")
else:
    print("You have failed the exam.")


# Real-life example of if-else statement
age = int(input("Enter your age: "))
if age >= 18:
    print("Adult")
else:
    print("Not an Adult")


# if-elif-else statement
marks = 85
if marks >= 90:
    print("Excellent")
elif marks >= 75:
    print("Very Good")
elif marks >= 40:
    print("PASS")
else:
    print("FAIL")


# Multiple conditions with separate if statements
marks = 75
if marks >= 90:
    print("Excellent")
if marks >= 75:
    print("Very Good")
if marks >= 40:
    print("PASS")


# Nested if
age = 18
if age >= 18:
    print("Age requirement satisfied")
    if age >= 21:
        print("21 or above")


# Real Example
marks = int(input("Enter your marks: "))
if marks >= 40:
    print("You are passed!")
else:
    print("You are failed.")


# Example - 2
number = int(input("Enter a number: "))
if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")