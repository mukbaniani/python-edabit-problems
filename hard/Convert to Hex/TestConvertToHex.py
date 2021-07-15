import unittest
from convert_to_hex import convert_to_hex


class TestConvertToHex(unittest.TestCase):
    def test_convert_to_hex(self):
        self.assertEqual(convert_to_hex("Big Boi"), "42 69 67 20 42 6f 69")
        self.assertEqual(convert_to_hex("Marty Poppinson"), "4d 61 72 74 79 20 50 6f 70 70 69 6e 73 6f 6e")
        self.assertEqual(convert_to_hex("abcdefghi"), "61 62 63 64 65 66 67 68 69")
        self.assertEqual(convert_to_hex("oh dear"), "6f 68 20 64 65 61 72")
        self.assertEqual(convert_to_hex("i hate C#"), "69 20 68 61 74 65 20 43 23")
        self.assertEqual(convert_to_hex("i love C++ , not really"), "69 20 6c 6f 76 65 20 43 2b 2b 20 2c 20 6e 6f 74 20 72 65 61 6c 6c 79")


if __name__ == '__main__':
    unittest.main()