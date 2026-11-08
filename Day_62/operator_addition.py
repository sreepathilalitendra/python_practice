# Day 62: Operator Overloading

class Number:

    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return Number(self.value + other.value)


num1 = Number(10)
num2 = Number(20)

result = num1 + num2

print("Addition:", result.value)