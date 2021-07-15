import unittest
from parse_code import parse_code


class TestParseCode(unittest.TestCase):
    def test_parse_code(self):
        self.assertEqual(parse_code('John000Doe000123'), {'first_name': 'John', 'last_name': 'Doe', 'id': '123'})
        self.assertEqual(parse_code('Michael0Smith004331'), {'first_name': 'Michael', 'last_name': 'Smith', 'id': '4331'})
        self.assertEqual(parse_code('Thomas0000Lee0000045553'), {'first_name': 'Thomas', 'last_name': 'Lee', 'id': '45553'})
        self.assertEqual(parse_code('a0b01'), {'first_name': 'a', 'last_name': 'b', 'id': '1'})


if __name__ == '__main__':
    unittest.main()