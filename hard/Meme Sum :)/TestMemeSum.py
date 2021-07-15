import unittest
from meme_sum import meme_sum


class TestMemeSum(unittest.TestCase):
    def test_meme_sum(self):
        self.assertEqual(meme_sum(2, 11), 13)
        self.assertEqual(meme_sum(0, 1), 1)
        self.assertEqual(meme_sum(0, 0), 0)
        self.assertEqual(meme_sum(16, 18), 214)
        self.assertEqual(meme_sum(26, 39), 515)
        self.assertEqual(meme_sum(122, 81), 1103)
        self.assertEqual(meme_sum(1222, 30277), 31499)
        self.assertEqual(meme_sum(38810, 1383), 391193)
        self.assertEqual(meme_sum(1236, 30977), 31111013)
        self.assertEqual(meme_sum(49999, 49999), 818181818)


if __name__ == '__main__':
    unittest.main()