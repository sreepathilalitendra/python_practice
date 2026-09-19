# Challenge 1
# Create a 3 x 3 star pattern

for i in range(1, 4):
    for j in range(1, 4):
        print("*", end=" ")
    print()


# Challenge 2
# Create a 5 x 5 star pattern

for i in range(1, 6):
    for j in range(1, 6):
        print("*", end=" ")
    print()


# Challenge 3
# Print this pattern
# 1 2 3
# 1 2 3
# 1 2 3

for i in range(1, 4):
    for j in range(1, 4):
        print(j, end=" ")
    print()


# Challenge 4
# Print this pattern
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()


# Challenge 5
# Print this star triangle
# *
# * *
# * * *
# * * * *
# * * * * *

for i in range(1, 6):
    for j in range(1, i + 1):
        print("*", end=" ")
    print()


# Challenge 6
# Create a multiplication table pattern
# using nested loop

for i in range(1, 4):
    for j in range(1, 11):
        print(i, "X", j, "=", i * j)
    print()