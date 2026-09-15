# Day 8 - Logical Operators


# and operator
age = 20
marks = 80
print(age >= 18 and marks >= 40)


# Example - 2
age = 16
marks = 80
print(age >= 18 and marks >= 40)


# or operator
age = 16
marks = 80
print(age >= 18 or marks >= 40)


# not operator
age = 20
print(not (age >= 18))


# Example - 2
print(not (10 > 20))


# Real Example -> Marks
marks = int(input("Enter your marks: "))
if marks >= 90 and marks <= 100:
    print("Grade A")
elif marks >= 75 and marks <= 89:
    print("Grade B")
elif marks >= 60 and marks <= 74:
    print("Grade C")
elif marks >= 40 and marks <= 59:
    print("Grade D")
else:
    print("Fail")


# Example with and
age = 20
marks = 80
if age >= 18 and marks >= 40:
    print("Eligible")
else:
    print("Not Eligible")


# Example with or
age = 16
marks = 80
if age >= 18 or marks >= 40:
    print("Condition satisfied")
else:
    print("Condition not satisfied")