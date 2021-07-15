import unittest
from negative_sum import negative_sum


class TestNegativeSum(unittest.TestCase):
    def test_negative_sum(self):
        self.assertEqual(negative_sum("-12 13%14&-11"), -23)
        self.assertEqual(negative_sum("-12 13%14&-2 0 12 -4"), -18)
        self.assertEqual(negative_sum("33%14&-1 12 a 21 -2 b c"), -3)
        self.assertEqual(negative_sum("22 13%14&-11-22 13 12"), -33)
        self.assertEqual(negative_sum("-12 -8"), -20)


if __name__ == '__main__':
    unittest.main()