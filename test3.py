import unittest
from program3 import reverse_string

class TestReverseString(unittest.TestCase):
    def test_reverse_string(self):
        self.assertEqual(reverse_string("hello"), "olleh")
        self.assertEqual(reverse_string("python"), "nohtyp")
        self.assertEqual(reverse_string("world"), "dlrow")

if __name__ == "__main__":
    unittest.main(argv=['first-arg-is-ignored'], exit=False)


