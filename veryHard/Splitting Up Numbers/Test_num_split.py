import unittest
from num_split import num_split


class MyTestCase(unittest.TestCase):
    def test_num_split(self):
        self.assertEqual(num_split(39), [30, 9])
        self.assertEqual(num_split(-434), [-400, -30, -4])
        self.assertEqual(num_split(100), [100, 0, 0])
        self.assertEqual(num_split(3929), [3000, 900, 20, 9])
        self.assertEqual(num_split(10293), [10000, 0, 200, 90, 3])
        self.assertEqual(num_split(900), [900, 0, 0])
        self.assertEqual(num_split(-100), [-100, 0, 0])


if __name__ == '__main__':
    unittest.main()
