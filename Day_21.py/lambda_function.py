# Day 21 - Lambda Functions

# Creating a Lambda Function
square = lambda number: number * number
print(square(5))


# Lambda with One Argument
double = lambda number: number * 2
print(double(5))


# Lambda with Multiple Arguments
add = lambda a, b: a + b
print(add(10, 20))

multiply = lambda a, b: a * b
print(multiply(5, 4))


# Lambda with if-else
check_number = lambda number: "Even" if number % 2 == 0 else "Odd"
print(check_number(10))
print(check_number(7))


# Lambda with map()
numbers = [1, 2, 3, 4, 5]
double = list(map(lambda number: number * 2, numbers))
print(double)


# Lambda with filter()
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(lambda number: number % 2 == 0, numbers))
print(even_numbers)


# Lambda with sorted()
numbers = [5, 2, 8, 1, 3]
sorted_numbers = sorted(numbers, key=lambda number: number)
print(sorted_numbers)