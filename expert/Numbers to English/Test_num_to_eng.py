import unittest
from num_to_eng import num_to_eng

class Test_num_to_eng(unittest.TestCase):
    def test_num_to_eng(self):
        self.assertEqual(num_to_eng(0), "zero")
        self.assertEqual(num_to_eng(26), "twenty six")
        self.assertEqual(num_to_eng(519), "five hundred nineteen")
        self.assertEqual(num_to_eng(106), "one hundred six")
        self.assertEqual(num_to_eng(999), "nine hundred ninety nine")

if __name__ == '__main__':
    unittest.main()
