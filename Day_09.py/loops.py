# Day 9 - For Loop


# Without loop
print("Hello")
print("Hello")
print("Hello")
print("Hello")
print("Hello")


# With loop using for loop
for i in range(5):
    print("Hello")


# range(start, stop)
for i in range(1, 6):
    print(i)


# range(start, stop, step)
for i in range(1, 11, 2):
    print(i)


# Reverse loop
# Negative step
for i in range(10, 0, -1):
    print(i)


# For loop with string
name = "Python"
for letter in name:
    print(letter)


# For loop + range()
for number in range(1, 11):
    print(number)


# Multiplication table - Real Example
number = int(input("Enter a number: "))
for i in range(1, 11):
    print(number, "X", i, "=", number * i)