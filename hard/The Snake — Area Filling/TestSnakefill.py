import unittest
from snakefill import snakefill


class TestSnakefill(unittest.TestCase):
    def test_snakefill(self):
        self.assertEqual(snakefill(8), 6)
        self.assertEqual(snakefill(18), 8)
        self.assertEqual(snakefill(555), 18)
        self.assertEqual(snakefill(2), 2)
        self.assertEqual(snakefill(1), 0)
        self.assertEqual(snakefill(900), 19)


if __name__ == '__main__':
    unittest.main()