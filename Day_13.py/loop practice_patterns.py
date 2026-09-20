# Day 13 - Pattern Programs


# Increasing Number Pattern

for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()


# Increasing Star Pattern

for i in range(1, 6):
    for j in range(i):
        print("*", end=" ")
    print()


# Decreasing Star Pattern

for i in range(5, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()