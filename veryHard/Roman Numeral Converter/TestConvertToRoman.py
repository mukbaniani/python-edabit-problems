import unittest
from convert_to_roman import convert_to_roman


class TestConvertToRoman(unittest.TestCase):
    def test_convert_to_roman(self):
        self.assertEqual(convert_to_roman(2), "II")
        self.assertEqual(convert_to_roman(12),"XII")
        self.assertEqual(convert_to_roman(16), "XVI")
        self.assertEqual(convert_to_roman(44), "XLIV")
        self.assertEqual(convert_to_roman(68), "LXVIII")
        self.assertEqual(convert_to_roman(400), "CD")
        self.assertEqual(convert_to_roman(798), "DCCXCVIII")
        self.assertEqual(convert_to_roman(1000), "M")
        self.assertEqual(convert_to_roman(3999),"MMMCMXCIX")
        self.assertEqual(convert_to_roman(649), "DCXLIX")


if __name__ == '__main__':
    unittest.main()