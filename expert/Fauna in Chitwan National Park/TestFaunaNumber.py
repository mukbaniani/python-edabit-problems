import unittest
from fauna_number import fauna_number


class TestFaunaNumber(unittest.TestCase):
    def test_fauna_number(self):
        self.assertEqual(fauna_number("There are 24 one-hornedrhino,50 python and 20000 bees."),[('one-hornedrhino', '24'), ('python', '50')])
        self.assertEqual(fauna_number("There are 244 bengaltiger,200 monitorlizard and 5000 apples."),[('bengaltiger', '244'), ('monitorlizard', '200')])
        self.assertEqual(fauna_number("There are 2444 saltrees,2000 cobra and 5000 mangotrees."),[])
        self.assertEqual(fauna_number("There are 180 muggercrocodile,20 krait and 500 taipan."),[('muggercrocodile', '180')])


if __name__ == '__main__':
    unittest.main()