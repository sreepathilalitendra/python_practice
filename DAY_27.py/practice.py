# CHALLENGE 1:
# Handle invalid integer input

try:
    num = int(input("Enter an integer: "))
    print("Number:", num)

except ValueError:
    print("Please enter a valid integer!")


# CHALLENGE 2:
# Handle division by zero

try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    result = a / b
    print("Result:", result)

except ZeroDivisionError:
    print("Cannot divide by zero!")

except ValueError:
    print("Please enter valid numbers!")


# CHALLENGE 3:
# Use try, except, and else

try:
    num = int(input("Enter a number: "))

except ValueError:
    print("Invalid input!")

else:
    print("Conversion successful!")
    print("Number:", num)


# CHALLENGE 4:
# Use finally

try:
    print("Python program is running")

finally:
    print("Program completed")


# CHALLENGE 5:
# Raise ValueError if the number is negative

try:
    num = int(input("Enter a positive number: "))

    if num < 0:
        raise ValueError("Number cannot be negative!")

    print("Number:", num)

except ValueError as error:
    print("Error:", error)


# CHALLENGE 6:
# Handle a missing file

try:
    with open("missing.txt", "r") as file:
        print(file.read())

except FileNotFoundError:
    print("File does not exist!")


# CHALLENGE 7:
# Calculator with exception handling

try:
    a = float(input("Enter first number: "))
    operator = input("Enter operator (+, -, *, /): ")
    b = float(input("Enter second number: "))

    if operator == "+":
        result = a + b

    elif operator == "-":
        result = a - b

    elif operator == "*":
        result = a * b

    elif operator == "/":
        result = a / b

    else:
        raise ValueError("Invalid operator!")

    print("Result:", result)

except ZeroDivisionError:
    print("Cannot divide by zero!")

except ValueError as error:
    print("Error:", error)