# Creating a Set

fruits = {"Apple", "Banana", "Mango"}
print(fruits)


# Duplicate Values

fruits = {"Apple", "Banana", "Mango", "Apple", "Mango", "Apple", "Banana"}
print(fruits)


# Adding an Item - add()

fruits = {"Apple", "Banana", "Mango"}
fruits.add("Orange")
print(fruits)


# Adding Multiple Items - update()

fruits = {"Apple", "Banana"}
fruits.update(["Mango", "Orange"])
print(fruits)


# Removing an Item - remove()

fruits = {"Apple", "Banana", "Mango"}
fruits.remove("Banana")
print(fruits)


# Removing an Item - discard()

fruits = {"Apple", "Banana", "Orange"}
fruits.discard("Banana")
print(fruits)


# Checking Items - in

fruits = {"Apple", "Banana", "Mango"}
print("Apple" in fruits)
print("Banana" in fruits)


# Set Length - len()

fruits = {"Apple", "Banana", "Mango"}
print(len(fruits))


# Looping Through a Set

fruits = {"Apple", "Banana", "Mango"}
for fruit in fruits:
    print(fruit)