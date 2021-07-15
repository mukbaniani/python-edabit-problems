import unittest
from ones_threes_nines import ones_threes_nines


class TestOnesThreesNines(unittest.TestCase):
    def test_ones_threes_nines(self):
        n1 = ones_threes_nines(1)
        self.assertEqual(n1.answer, 'nines:0, threes:0, ones:1')
        n2 = ones_threes_nines(5)
        self.assertEqual(n2.answer, 'nines:0, threes:1, ones:2')
        n3 = ones_threes_nines(7)
        self.assertEqual(n3.answer, 'nines:0, threes:2, ones:1')
        n4 = ones_threes_nines(10)
        self.assertEqual(n4.answer, 'nines:1, threes:0, ones:1')
        n5 = ones_threes_nines(12)
        self.assertEqual(n5.answer, 'nines:1, threes:1, ones:0')
        n6 = ones_threes_nines(15)
        self.assertEqual(n6.answer, 'nines:1, threes:2, ones:0')
        n7 = ones_threes_nines(22)
        self.assertEqual(n7.answer, 'nines:2, threes:1, ones:1')
        n8 = ones_threes_nines(25)
        self.assertEqual(n8.answer, 'nines:2, threes:2, ones:1')


if __name__ == '__main__':
    unittest.main()