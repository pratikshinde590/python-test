import unittest
from program1 import add_numbers  # Import directly from program1

class TestAddNumbers(unittest.TestCase):
    def test_add_positive_numbers(self):
        self.assertEqual(add_numbers(2, 3), 5)

if __name__ == "__main__":
    unittest.main()


