
# Day 54: Generator Expression Review

# 1. List comprehension

numbers = [1, 2, 3, 4, 5]

squares_list = [number ** 2 for number in numbers]

print("List:", squares_list)


# 2. Generator expression

squares_generator = (number ** 2 for number in numbers)

print("Generator:", squares_generator)


# 3. Access generator values using next()

print("First value:", next(squares_generator))
print("Second value:", next(squares_generator))
print("Third value:", next(squares_generator))


# 4. Loop through remaining values

print("Remaining values:")

for value in squares_generator:
    print(value)


# 5. Create a fresh generator

even_generator = (
    number for number in range(1, 11)
    if number % 2 == 0
)

print("Even numbers from generator:")

for number in even_generator:
    print(number)


# 6. Convert generator into a list

another_generator = (number * 10 for number in range(1, 6))

converted_list = list(another_generator)

print("Converted list:", converted_list)
