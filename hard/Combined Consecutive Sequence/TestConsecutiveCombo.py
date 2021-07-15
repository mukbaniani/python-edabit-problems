import unittest
from consecutive_combo import consecutive_combo

class TestConsecutiveCombo(unittest.TestCase):
    def test_consecutive_combo(self):
        self.assertEqual(consecutive_combo([1, 4, 5, 7], [2, 3, 6]), True)
        self.assertEqual(consecutive_combo([1, 4, 5, 6], [2, 7, 8, 9]), False)
        self.assertEqual(consecutive_combo([1, 4, 5, 6], [2, 3, 7, 8, 10]), False)
        self.assertEqual(consecutive_combo([7, 5, 4, 1], [2, 3, 6, 8]), True)
        self.assertEqual(consecutive_combo([33, 34, 40], [39, 38, 37, 36, 35, 32, 31, 30]), True)
        self.assertEqual(consecutive_combo([1, 4, 5, 6], [2, 3, 7, 8, 10]), False)
        self.assertEqual(consecutive_combo([44, 46], [45]), True)
        self.assertEqual(consecutive_combo([4, 3, 1], [2, 5]), True)
        self.assertEqual(consecutive_combo([4, 3, 1], [2, 5, 7, 6]), True)
        self.assertEqual(consecutive_combo([4, 3, 1], [7, 6, 5]), False)
        self.assertEqual(consecutive_combo([4, 3, 1], [0, 7, 6, 5]), False)
        self.assertEqual(consecutive_combo([44, 46], [45]), True)


if __name__ == '__main__':
    unittest.main()