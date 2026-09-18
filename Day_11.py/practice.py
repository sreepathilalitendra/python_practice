# Day 11 - Break, Continue and Pass Practice


# Challenge 1 - Break
# Stop the loop when i reaches 6
for i in range(1, 10):
    if i == 6:
        break

    print(i)


# Challenge 2 - Continue
# Skip number 5
for i in range(1, 10):
    if i == 5:
        continue

    print(i)


# Challenge 3 - Continue
# Print only odd numbers
for i in range(1, 20):
    if i % 2 == 0:
        continue

    print(i)


# Challenge 4 - Break
# Stop the loop when i reaches 10
for i in range(1, 20):
    if i == 10:
        break

    print(i)


# Challenge 5 - Pass
# Use pass when i is 3
for i in range(1, 5):
    if i == 3:
        pass

    print(i)


# Challenge 6 - Break with user input
# Stop when the loop reaches the user's number
number = int(input("Enter a number: "))
for i in range(1, number + 1):
    if i == number:
        break

    print(i)