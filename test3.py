import unittest
from program3 import divide_numbers

class TestDivideNumbers(unittest.TestCase):
    def test_divide_positive_numbers(self):
        self.assertEqual(divide_numbers(6, 3), 2)

if __name__ == "__main__":
    unittest.main()
