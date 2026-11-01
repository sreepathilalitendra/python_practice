
# Day 55: Iterator Basics

numbers = [10, 20, 30, 40, 50]

# Convert list into an iterator
number_iterator = iter(numbers)

# Retrieve values one by one
print(next(number_iterator))
print(next(number_iterator))
print(next(number_iterator))
print(next(number_iterator))
print(next(number_iterator))
