import unittest
from super_digit import super_digit

class TestSuperDigit(unittest.TestCase):
    def test_super_digit(self):
        self.assertEqual(super_digit("123", 3), 9)
        self.assertEqual(super_digit("9875", 4), 8)
        self.assertEqual(super_digit("148", 3), 3)
        self.assertEqual(super_digit("111", 10), 3)
        self.assertEqual(super_digit("543", 100), 3)


if __name__ == '__main__':
    unittest.main()
