import unittest
from pentagonal import pentagonal


class TestPentagonal(unittest.TestCase):
    def test_pentagonal(self):
        self.assertEqual(pentagonal(1), 1)
        self.assertEqual(pentagonal(3), 16)
        self.assertEqual(pentagonal(8), 141)
        self.assertEqual(pentagonal(10), 226)
        self.assertEqual(pentagonal(15), 526)
        self.assertEqual(pentagonal(33), 2641)
        self.assertEqual(pentagonal(43), 4516)
        self.assertEqual(pentagonal(13), 391)
        self.assertEqual(pentagonal(50), 6126)
        self.assertEqual(pentagonal(62), 9456)
        self.assertEqual(pentagonal(21), 1051)


if __name__ == '__main__':
    unittest.main()