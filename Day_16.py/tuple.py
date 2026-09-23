# Day 16 - Tuples


# Creating a Tuple

fruits = ("Apple", "Banana", "Mango")
print(fruits)


# Accessing Tuple Items

fruits = ("Apple", "Banana", "Mango")
print(fruits[0])
print(fruits[1])
print(fruits[2])


# Positive Indexing

fruits = ("Apple", "Banana", "Mango")
print(fruits[0])
print(fruits[2])


# Negative Indexing

fruits = ("Apple", "Banana", "Mango")
print(fruits[-1])
print(fruits[-2])


# Tuple Length - len()

fruits = ("Apple", "Banana", "Mango")
print(len(fruits))


# Checking Items - in

fruits = ("Apple", "Banana", "Mango")
print("Apple" in fruits)
print("Orange" in fruits)


# Tuple Slicing

fruits = ("Apple", "Banana", "Mango")
print(fruits[0:2])


# Looping Through a Tuple

fruits = ("Apple", "Banana", "Mango")
for fruit in fruits:
    print(fruit)