import unittest
from get_domain import get_domain


class TestGetDomain(unittest.TestCase):
    def test_get_domain(self):
        self.assertEqual(get_domain("8.8.8.8"), "dns.google")
        self.assertEqual(get_domain("8.8.4.4"), "dns.google")

if __name__ == '__main__':
    unittest.main()
