# Day 3 - Input Function and Type Conversion


# input() Function
name = input("Enter your name: ")
print(name)


# Example 2
name = input("Enter your name: ")
age = input("Enter your age: ")

print(name)
print(age)


# input() Function always returns a string value
age = input("Enter your age: ")

print(type(age))


# Type Conversion

# String to Integer
age = int(input("Enter your age: "))

print(age)
print(type(age))


# String to Float
percentage = float(input("Enter your percentage: "))

print(percentage)
print(type(percentage))


# Integer to String conversion
age = 18
age_text = str(age)

print(age_text)
print(type(age_text))


# A Real Example of input() Function
name = input("Enter your name: ")
age = int(input("Enter your age: "))
percentage = float(input("Enter your percentage: "))

print("Name:", name)
print("Age:", age)
print("Percentage:", percentage)