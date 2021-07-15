import unittest
from weekday_dutch import weekday_dutch

class TestWeekdayDutch(unittest.TestCase):
    def test_weekday_dutch(self):
        self.assertEqual(weekday_dutch("21 9 1970"), "maandag")
        self.assertEqual(weekday_dutch("22 9 1970"), "dinsdag")
        self.assertEqual(weekday_dutch("23 9 1970"), "woensdag")
        self.assertEqual(weekday_dutch("24 9 1970"), "donderdag")
        self.assertEqual(weekday_dutch("25 9 1970"), "vrijdag")
        self.assertEqual(weekday_dutch("26 9 1970"), "zaterdag")
        self.assertEqual(weekday_dutch("27 9 1970"), "zondag")
        self.assertEqual(weekday_dutch("10 12 2050"), "zaterdag")
        self.assertEqual(weekday_dutch("14 10 6010"), "donderdag")
        self.assertEqual(weekday_dutch("31 1 1000"), "vrijdag")
        self.assertEqual(weekday_dutch("8 12 2112"), "donderdag")
        self.assertEqual(weekday_dutch("12 12 1212"), "woensdag")


if __name__ == '__main__':
    unittest.main()