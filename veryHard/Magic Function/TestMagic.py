import unittest
from Magic import Magic


class TestMagic(unittest.TestCase):
    def test_TestMagic(self):
        magic = Magic()
        self.assertEqual(magic.trim("  python is awesome  "), "python is awesome")
        self.assertEqual(magic.str_length("Hello world!"), 12)
        self.assertEqual(magic.list_slice([1, 2, 3, 4, 5], (2, 4))[0], 2)
        self.assertEqual(magic.list_slice([1, 2, 3, 4, 5], (-1, 4)), [4])
        self.assertEqual(magic.replace("AzErty-QwErty", 'E','e'), "Azerty-Qwerty")


if __name__ == '__main__':
    unittest.main()