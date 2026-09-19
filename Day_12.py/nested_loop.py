# Day 12 - Nested Loop


# 1. Basic Nested Loop

for i in range(1, 4):
    for j in range(1, 4):
        print(i, j)


# 2. Nested Loop with *

for i in range(3):
    for j in range(3):
        print("*", end=" ")
    print()


# 3. Square Pattern

for i in range(1, 5):
    for j in range(1, 5):
        print("*", end=" ")
    print()


# 4. Number Pattern

for i in range(1, 4):
    for j in range(1, 4):
        print(j, end=" ")
    print()
# 5. Triangle Pattern

for i in range(1, 6):
    for j in range(1, i + 1):
        print("*", end=" ")
    print()