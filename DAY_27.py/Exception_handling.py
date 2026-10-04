 # DAY 27: PYTHON EXCEPTION HANDLING
# 1. try and except

try:
    num = int(input("Enter a number: "))
    print("Number:", num)

except ValueError:
    print("Please enter a valid number!")


# 2. Handle division by zero

try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    print("Result:", a / b)

except ZeroDivisionError:
    print("Cannot divide by zero!")

except ValueError:
    print("Please enter numbers only!")


# 3. Using else

try:
    num = int(input("Enter a number: "))

except ValueError:
    print("Invalid input!")

else:
    print("Your number is:", num)


# 4. Using finally

try:
    print("Python is easy to learn!")

except Exception:
    print("An error occurred")

finally:
    print("Program finished")


# 5. Raising an exception

try:
    age = int(input("Enter your age: "))

    if age < 0:
        raise ValueError("Age cannot be negative")

    print("Age:", age)

except ValueError as error:
    print("Error:", error)


# 6. Handling a missing file

try:
    with open("missing.txt", "r") as file:
        print(file.read())

except FileNotFoundError:
    print("File does not exist!")