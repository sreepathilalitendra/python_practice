
# DAY 36: ITERATORS AND ITERABLES


# LESSON 1: Loop through a list

numbers = [10, 20, 30, 40]

for number in numbers:
    print(number)


# LESSON 2: Create an iterator using iter()

numbers = [100, 200, 300]

iterator = iter(numbers)

print(next(iterator))
print(next(iterator))
print(next(iterator))


# LESSON 3: Iterate through a string

name = "Python"

iterator = iter(name)

print(next(iterator))
print(next(iterator))
print(next(iterator))


# LESSON 4: Check iterable and iterator types

numbers = [1, 2, 3]

iterator = iter(numbers)

print("List type:", type(numbers))
print("Iterator type:", type(iterator))


# LESSON 5: Use a while loop with an iterator

numbers = [5, 10, 15, 20]

iterator = iter(numbers)

while True:
    try:
        number = next(iterator)
        print(number)

    except StopIteration:
        break


# LESSON 6: Iterate through a dictionary

student = {
    "name": "Lalitendra",
    "course": "CSE",
    "language": "Python"
}

iterator = iter(student)

print(next(iterator))
print(next(iterator))
print(next(iterator))


# LESSON 7: Create a fresh iterator

numbers = [1, 2, 3]

first_iterator = iter(numbers)

print(next(first_iterator))
print(next(first_iterator))

second_iterator = iter(numbers)

print(next(second_iterator))


# LESSON 8: Use a for loop with iterables

colors = ["Red", "Blue", "Green"]

for color in colors:
    print(color)