import unittest
from uncensor import uncensor


class TestUncensor(unittest.TestCase):
    def test_uncensor(self):
        self.assertEqual(uncensor('Wh*r* d*d my v*w*ls g*?', 'eeioeo'), 'Where did my vowels go?')
        self.assertEqual(uncensor('abcd', ''), 'abcd', 'Works with no vowels.')
        self.assertEqual(uncensor('*PP*RC*S*', 'UEAE'), 'UPPERCASE', 'Works with uppercase')
        self.assertEqual(uncensor('Ch**s*, Gr*mm*t -- ch**s*', 'eeeoieee'), 'Cheese, Grommit -- cheese', 'Works with * at the end')
        self.assertEqual(uncensor('*l*ph*nt', 'Eea'), 'Elephant', 'Works with * at the start')


if __name__ == '__main__':
    unittest.main()