# Challenge 1 - Square of a Number
number = 6

square = lambda number: number * number

print(square(number))


# Challenge 2 - Cube of a Number
number = 5

cube = lambda number: number * number * number

print(cube(number))


# Challenge 3 - Sum of Two Numbers
a = 10
b = 20

add = lambda a, b: a + b

print(add(a, b))


# Challenge 4 - Even or Odd
number = 7

check_number = lambda number: "Even" if number % 2 == 0 else "Odd"

print(check_number(number))


# Challenge 5 - Double Every Number
numbers = [1, 2, 3, 4, 5]

double_numbers = list(map(lambda number: number * 2, numbers))

print(double_numbers)


# Challenge 6 - Even Numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8]

even_numbers = list(filter(lambda number: number % 2 == 0, numbers))

print(even_numbers)


# Challenge 7 - Numbers Greater Than 5
numbers = [2, 7, 4, 9, 3, 8, 1]

greater_numbers = list(filter(lambda number: number > 5, numbers))

print(greater_numbers)


# Challenge 8 - Sort Numbers
numbers = [5, 2, 8, 1, 3]

sorted_numbers = sorted(numbers, key=lambda number: number)

print(sorted_numbers)


# Challenge 9 - Larger Number
a = 10
b = 20

larger = lambda a, b: a if a > b else b

print(larger(a, b))


# Challenge 10 - Squares Using map()
numbers = [1, 2, 3, 4, 5]

squares = list(map(lambda number: number * number, numbers))

print(squares)