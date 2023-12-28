import unittest
from lab.program2 import multiply_numbers

class TestMultiplyNumbers(unittest.TestCase):
    def test_multiply_positive_numbers(self):
        self.assertEqual(multiply_numbers(2, 3), 6)

if __name__ == "__main__":
    unittest.main()

