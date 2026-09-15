# Challenge 1
age = 20
if age >= 18:
    print("You are eligible for vote")


# Challenge 2
marks = int(input("Enter your marks: "))
if marks >= 40:
    print("PASS")
else:
    print("FAIL")


# Challenge 3
number = int(input("Enter a number: "))
if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")


# Challenge 4
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


# Challenge 5
age = int(input("Enter your age: "))
marks = int(input("Enter your marks: "))
if age >= 18 and marks >= 40:
    print("Eligible")
else:
    print("Not Eligible")