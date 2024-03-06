# Write a test case for a function that checks if a number is prime

import unittest
from primenum_Day33 import isprime

class TestIsPrimeFunction(unittest.TestCase):
    def test_isprime(self):
        self.assertTrue(isprime(5))
        self.assertTrue(isprime(53))
        self.assertTrue(isprime(97))
        self.assertFalse(isprime(1))
        self.assertFalse(isprime(10))
        self.assertFalse(isprime(88))


if __name__ == '__main__':
    unittest.main()