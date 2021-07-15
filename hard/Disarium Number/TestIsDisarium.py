import unittest
from is_disarium import is_disarium


class TestIsDisarium(unittest.TestCase):
    def test_is_disarium(self):
        num_vector, res_vector = [
        [6, 75, 135, 466, 372, 175, 1, 696, 876, 89, 518, 598],
        [True, False, True, False, False, True, True, False, False, True, True, True]
        ]
        for i, n in enumerate(num_vector): self.assertEqual(is_disarium(n), res_vector[i])

if __name__ == '__main__':
    unittest.main()