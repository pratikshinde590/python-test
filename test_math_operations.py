# test_math_operations.py
import unittest
from math_operations import add, subtract, multiply, divide

class TestMathOperations(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 5), 4)

    def test_subtraction(self):
        self.assertEqual(subtract(8, 4), 4)
        self.assertEqual(subtract(5, 2), 3)

    def test_multiplication(self):
        self.assertEqual(multiply(3, 4), 12)
        self.assertEqual(multiply(-2, 6), -12)

    def test_division(self):
        self.assertEqual(divide(10, 2), 5)
        self.assertEqual(divide(8, 4), 2)
        
        # Test division by zero
        self.assertEqual(divide(5, 0), "Cannot divide by zero")

if __name__ == '__main__':
    unittest.main()
