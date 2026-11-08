# Day 62: Callable Objects and Indexing

class Calculator:

    def __init__(self, multiplier):
        self.multiplier = multiplier

    def __call__(self, number):
        return number * self.multiplier


class NumberCollection:

    def __init__(self, numbers):
        self.numbers = numbers

    def __getitem__(self, index):
        return self.numbers[index]


# Callable object
calculator = Calculator(5)

print("Callable Result:", calculator(10))


# Indexing object
collection = NumberCollection([10, 20, 30, 40])

print("First Element:", collection[0])
print("Second Element:", collection[1])