import unittest
from has_friday_13 import has_friday_13


class TestHasFriday13(unittest.TestCase):
    def test_has_friday_13(self):
        self.assertEqual(has_friday_13(3, 2020), True)
        self.assertEqual(has_friday_13(10, 2017), True)
        self.assertEqual(has_friday_13(1, 1985), False)
        self.assertEqual(has_friday_13(5, 1619), False)
        self.assertEqual(has_friday_13(6, 1614), True)
        self.assertEqual(has_friday_13(8, 1767), False)
        self.assertEqual(has_friday_13(6, 1589), False)
        self.assertEqual(has_friday_13(2, 2015), True)
        self.assertEqual(has_friday_13(3, 2015), True)
        self.assertEqual(has_friday_13(11, 2015), True)
        self.assertEqual(has_friday_13(2, 1759), False)
        self.assertEqual(has_friday_13(8, 1612), False)
        self.assertEqual(has_friday_13(8, 1612), False)
        self.assertEqual(has_friday_13(10, 2029), False)
        self.assertEqual(has_friday_13(1, 1590), False)
        self.assertEqual(has_friday_13(7, 1812), False)
        self.assertEqual(has_friday_13(1, 1785), False)
        self.assertEqual(has_friday_13(11, 1961), False)
        self.assertEqual(has_friday_13(9, 1706), False)
        self.assertEqual(has_friday_13(5, 2016), True)
        self.assertEqual(has_friday_13(11, 2020), True)
        self.assertEqual(has_friday_13(1, 2023), True)
        self.assertEqual(has_friday_13(10, 2023), True)
        self.assertEqual(has_friday_13(2, 2043), True)
        self.assertEqual(has_friday_13(4, 2043), False)
        self.assertEqual(has_friday_13(3, 2043), True)
        self.assertEqual(has_friday_13(11, 2043), True)


if __name__ == '__main__':
    unittest.main()