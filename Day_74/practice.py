
import unittest

# Challenge 1: Subtract two numbers
def subtract(a, b):
    return a - b


# Challenge 2: Find the largest of two numbers
def find_largest(a, b):
    return max(a, b)


# Challenge 3: Calculate square of a number
def square(number):
    return number ** 2


# Challenge 4: Check whether a number is positive
def is_positive(number):
    return number > 0


# Challenge 5: Test subtraction
class TestCalculator(unittest.TestCase):

    def test_subtract(self):
        self.assertEqual(subtract(20, 10), 10)


# Challenge 6: Test largest number
    def test_find_largest(self):
        self.assertEqual(find_largest(25, 15), 25)


# Challenge 7: Test square
    def test_square(self):
        self.assertEqual(square(5), 25)


# Challenge 8: Test positive and negative numbers
    def test_positive_number(self):
        self.assertTrue(is_positive(10))

    def test_negative_number(self):
        self.assertFalse(is_positive(-5))


# Challenge 9: Test an exception
def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")

    return a / b


class TestDivision(unittest.TestCase):

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            divide(10, 0)


# Challenge 10: Calculator Testing Program
def add(a, b):
    return a + b


def multiply(a, b):
    return a * b


def calculator_divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")

    return a / b


class TestCalculatorOperations(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(add(10, 20), 30)

    def test_subtraction(self):
        self.assertEqual(subtract(30, 10), 20)

    def test_multiplication(self):
        self.assertEqual(multiply(5, 4), 20)

    def test_division(self):
        self.assertEqual(calculator_divide(20, 5), 4)

    def test_division_error(self):
        with self.assertRaises(ValueError):
            calculator_divide(10, 0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
