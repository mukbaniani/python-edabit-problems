import unittest
from simplify import simplify


class TestSimplify(unittest.TestCase):
    def test_simplify(self):
        self.assertEqual(simplify("5/7"), "5/7")
        self.assertEqual(simplify("4/6"), "2/3")
        self.assertEqual(simplify("11/10"), "11/10")
        self.assertEqual(simplify("8/4"), 2)
        self.assertEqual(simplify("7/4"), "7/4", 'should work for improper fractions')
        self.assertEqual(simplify("6/4"), "3/2")
        self.assertEqual(simplify("300/200"), "3/2")
        self.assertEqual(simplify("50/25"), 2)
        self.assertEqual(simplify("5/45"), "1/9")


if __name__ == '__main__':
    unittest.main()