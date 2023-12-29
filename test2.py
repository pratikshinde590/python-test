import unittest
from program2 import sum_of_squares

class TestSumOfSquares(unittest.TestCase):
    def test_sum_of_squares(self):
        self.assertEqual(sum_of_squares([1, 2, 3]), 14)
        self.assertEqual(sum_of_squares([2, 4, 6]), 56)
        self.assertEqual(sum_of_squares([5, 3, 1]), 35)

if __name__ == "__main__":
    unittest.main(argv=['first-arg-is-ignored'], exit=False)


