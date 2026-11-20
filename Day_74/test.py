
import unittest

from day74_main import (
    add_numbers,
    calculate_average,
    multiply,
    divide,
    is_even,
    get_grade
)


class TestPythonFunctions(unittest.TestCase):

    # Test 1: Addition
    def test_add_numbers(self):
        self.assertEqual(add_numbers(10, 20), 30)


    # Test 2: Multiplication
    def test_multiply(self):
        self.assertEqual(multiply(5, 4), 20)


    # Test 3: Division
    def test_divide(self):
        self.assertEqual(divide(20, 5), 4)


    # Test 4: Division by zero
    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            divide(10, 0)


    # Test 5: Even number
    def test_is_even(self):
        self.assertTrue(is_even(10))


    # Test 6: Odd number
    def test_is_odd(self):
        self.assertFalse(is_even(7))


    # Test 7: Grade A
    def test_grade_a(self):
        self.assertEqual(get_grade(95), "A")


    # Test 8: Grade B
    def test_grade_b(self):
        self.assertEqual(get_grade(80), "B")


    # Test 9: Average
    def test_average(self):
        self.assertEqual(
            calculate_average([80, 90, 70]),
            80
        )


    # Test 10: Empty marks
    def test_empty_average(self):
        self.assertEqual(calculate_average([]), 0)


if __name__ == "__main__":
    unittest.main()
