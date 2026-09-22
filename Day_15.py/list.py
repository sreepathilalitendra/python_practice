# Day 15 - Lists


# Creating a List

fruits = ["Apple", "Banana", "Mango"]

print(fruits)


# Accessing List Items

fruits = ["Apple", "Banana", "Mango"]

print(fruits[0])
print(fruits[1])
print(fruits[2])


# Positive Indexing

print(fruits[0])
print(fruits[1])


# Negative Indexing

print(fruits[-1])
print(fruits[-2])


# Changing an Item

fruits = ["Apple", "Banana", "Mango"]

fruits[1] = "Orange"

print(fruits)


# Adding Items - append()

fruits = ["Apple", "Banana"]

fruits.append("Mango")

print(fruits)


# Adding Items - insert()

fruits = ["Apple", "Banana", "Mango"]

fruits.insert(1, "Orange")

print(fruits)


# Removing Items - remove()

fruits = ["Apple", "Banana", "Mango"]

fruits.remove("Banana")

print(fruits)


# Removing Items - pop()

fruits = ["Apple", "Banana", "Mango"]

fruits.pop()

print(fruits)


# List Length - len()

fruits = ["Apple", "Banana", "Mango"]

print(len(fruits))


# Checking Items - in

print("Apple" in fruits)
print("Orange" in fruits)


# List Slicing

print(fruits[0:2])


# Looping Through a List

for fruit in fruits:
    print(fruit)