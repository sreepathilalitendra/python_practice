# CHALLENGE 1: Print list values using next()

numbers = [2, 4, 6, 8]

iterator = iter(numbers)

print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))


# CHALLENGE 2: Iterate through a word

word = "CODE"

iterator = iter(word)

print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))


# CHALLENGE 3: Iterate through a tuple

colors = ("Red", "Green", "Blue")

iterator = iter(colors)

print(next(iterator))
print(next(iterator))
print(next(iterator))


# CHALLENGE 4: Safely consume an iterator

numbers = [10, 20, 30]

iterator = iter(numbers)

while True:
    try:
        print(next(iterator))

    except StopIteration:
        break


# CHALLENGE 5: Iterate through dictionary keys

student = {
    "name": "Ravi",
    "age": 18,
    "course": "CSE"
}

iterator = iter(student)

for key in iterator:
    print(key)


# CHALLENGE 6: Iterate through dictionary values

student = {
    "name": "Ravi",
    "age": 18,
    "course": "CSE"
}

iterator = iter(student.values())

for value in iterator:
    print(value)


# CHALLENGE 7: Convert an iterator into a list

numbers = [10, 20, 30, 40]

iterator = iter(numbers)

remaining_values = list(iterator)

print(remaining_values)


# CHALLENGE 8: Check iterator exhaustion

numbers = [100, 200]

iterator = iter(numbers)

print(next(iterator))
print(next(iterator))

try:
    print(next(iterator))

except StopIteration:
    print("No more values")