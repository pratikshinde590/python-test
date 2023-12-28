import unittest
from program1 import add_numbers

class TestMultiplyNumbers(unittest.TestCase):
    def test_add_positive_numbers(self):
        self.assertEqual(add_numbers(2, 3), 6)

if __name__ == "__main__":
    unittest.main()



