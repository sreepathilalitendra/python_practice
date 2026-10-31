


# Challenge 1: Generate cubes from 1 to 10

cubes = [number ** 3 for number in range(1, 11)]

print("1. Cubes:", cubes)


# Challenge 2: Numbers divisible by both 3 and 5

numbers = [
    number for number in range(1, 101)
    if number % 3 == 0 and number % 5 == 0
]

print("\n2. Numbers divisible by 3 and 5:", numbers)


# Challenge 3: Convert names into uppercase

names = ["sree", "arun", "kiran", "balu"]

uppercase_names = [name.upper() for name in names]

print("\n3. Uppercase names:", uppercase_names)


# Challenge 4: Dictionary containing numbers and cubes

number_cubes = {
    number: number ** 3
    for number in range(1, 6)
}

print("\n4. Number cubes:", number_cubes)


# Challenge 5: Unique even numbers using set comprehension

values = [1, 2, 2, 3, 4, 4, 5, 6, 6, 8]

unique_even = {
    number for number in values
    if number % 2 == 0
}

print("\n5. Unique even numbers:", sorted(unique_even))


# Challenge 6: Generator expression for multiples of 7

multiples = (number * 7 for number in range(1, 11))

print("\n6. Multiples of 7:")

for value in multiples:
    print(value)


# Challenge 7: Retrieve first three generator values using next()

generator = (number * 7 for number in range(1, 11))

print("\n7. First three values:")

print(next(generator))
print(next(generator))
print(next(generator))
