import unittest
from arithmetic_operation import arithmetic_operation


class TestArithmeticOperation(unittest.TestCase):
    def test_arithmetic_operation(self):
        self.assertEqual(arithmetic_operation("12 + 12"), 24)
        self.assertEqual(arithmetic_operation("22 - 12"), 10)
        self.assertEqual(arithmetic_operation("100 * 12"), 1200)
        self.assertEqual(arithmetic_operation("120 // 10"), 12)
        self.assertEqual(arithmetic_operation("122 // 0"), -1)
        self.assertEqual(arithmetic_operation("10 * 20"), 200)
        self.assertEqual(arithmetic_operation("10 - 10"), 0)
        self.assertEqual(arithmetic_operation("10 - 12"), -2)

if __name__ == '__main__':
    unittest.main()
