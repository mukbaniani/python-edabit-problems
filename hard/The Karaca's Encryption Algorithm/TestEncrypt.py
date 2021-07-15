import unittest
from encrypt import encrypt


class TestEncrypt(unittest.TestCase):
    def test_encrypt(self):
        self.assertEqual(encrypt("karaca"), "0c0r0kaca")
        self.assertEqual(encrypt("burak"), "k0r3baca")
        self.assertEqual(encrypt("banana"), "0n0n0baca")
        self.assertEqual(encrypt("alpaca"), "0c0pl0aca")
        self.assertEqual(encrypt("hello"), "2ll1haca")


if __name__ == '__main__':
    unittest.main()