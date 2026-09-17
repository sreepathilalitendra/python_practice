# Challenge 1
# Print numbers from 1 to 10
count = 1
while count <= 10:
    print(count)
    count = count + 1


# Challenge 2
# Print even numbers from 2 to 20
count = 2
while count <= 20:
    if count % 2 == 0:
        print(count)

    count = count + 1


# Challenge 2 - Example 2
# Print even numbers without using if
count = 0
while count < 20:
    count += 2
    print(count)


# Challenge 3
# Print numbers from 10 to 1
count = 10
while count >= 1:
    print(count)
    count = count - 1


# Challenge 4
# Take a number from the user and print up to 10
number = int(input("Enter a number: "))
while number <= 10:
    print(number)
    number = number + 1


# Challenge 5
# Multiplication table from 1 to 10
number = int(input("Enter a number: "))
count = 1
while count <= 10:
    print(number, "X", count, "=", number * count)
    count = count + 1