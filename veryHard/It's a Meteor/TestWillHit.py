import unittest
from will_hit import will_hit


class TestWillHit(unittest.TestCase):
    def test_will_hit(self):
        self.assertEqual(will_hit("y = 2x - 5", (0, 0)), False)
        self.assertEqual(will_hit("y = -4x + 6", (1, 2)), True)
        self.assertEqual(will_hit("y = -4x + 6", (2, 2)), False)
        self.assertEqual(will_hit("y = 3x - 8", (4, 4)), True)
        self.assertEqual(will_hit("y = 2x + 6", (3, 2)), False)
        self.assertEqual(will_hit("y = -3x + 15", (5, 0)), True)


if __name__ == '__main__':
    unittest.main()