# Write a simple unit test for a function that adds two numbers

import unittest
from addnums_Day35 import nums_addition


class TestNumberAddition(unittest.TestCase):
    def test_numberaddition(self):
        self.assertEqual(nums_addition(5, 7), 12)
        self.assertEqual(nums_addition(8, -4), 4)
        self.assertEqual(nums_addition(4.0, 6.0), 10.0)
        self.assertEqual(nums_addition(4, 6.0), 10.0)
        self.assertEqual(nums_addition(4.0, -6.0), -2.0)

if __name__ == '__main__':
    unittest.main()
