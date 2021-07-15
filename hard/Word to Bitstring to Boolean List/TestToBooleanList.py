import unittest
from to_boolean_list import to_boolean_list

class TestToBooleanList(unittest.TestCase):
    def test_to_boolean_list(self):
        actual_param = [
        "charming", "exquisite", "admire", "deep", "loves", "tesh",
        "xavier", "adores", "tesha", "esquire", "randomize", "exotic"
        ]
        expected_param = [
        [True, False, True, False, True, True, False, True],
        [True, False, True, True, True, True, True, False, True],
        [True, False, True, True, False, True],
        [False, True, True, False],
        [False, True, False, True, True],
        [False, True, True, False],
        [False, True, False, True, True, False],
        [True, False, True, False, True, True],
        [False, True, True, False, True],
        [True, True, True, True, True, False, True],
        [False, True, False, False, True, True, True, False, True],
        [True, False, True, False, True, True]
        ]
        for i, x in enumerate(actual_param): self.assertEqual(to_boolean_list(x), expected_param[i])


if __name__ == '__main__':
    unittest.main()