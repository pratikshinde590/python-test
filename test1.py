import unittest

class TestDistributeCandies(unittest.TestCase):
    def test_example1(self):
        candies, num_people = 7, 4
        result = distribute_candies(candies, num_people)
        self.assertEqual(result, [1, 2, 3, 1])

    def test_example2(self):
        candies, num_people = 10, 3
        result = distribute_candies(candies, num_people)
        self.assertEqual(result, [5, 2, 3])

    # Add more test cases as needed

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)




