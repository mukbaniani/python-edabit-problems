import unittest
from split import split


class TestSplit(unittest.TestCase):
    def test_split(self):
        self.assertEqual(split("()()()"), ["()", "()", "()"])
        self.assertEqual(split(""), [])
        self.assertEqual(split("()()(())"), ["()", "()", "(())"])
        self.assertEqual(split("(())(())"), ["(())", "(())"])
        self.assertEqual(split("((()))"), ["((()))"])
        self.assertEqual(split("()(((((((((())))))))))"), ["()", "(((((((((())))))))))"])
        self.assertEqual(split("((())()(()))(()(())())(()())"), ["((())()(()))", "(()(())())", "(()())"])
        self.assertEqual(split("((()))(())()()(()())"), ["((()))", "(())", "()", "()", "(()())"])
        self.assertEqual(split("((())())(()(()()))"), ["((())())", "(()(()()))"])
        self.assertEqual(split("(()(()()))()(((()))()(()))(()((()))(())())"), ["(()(()()))", "()", "(((()))()(()))", "(()((()))(())())"])


if __name__ == '__main__':
    unittest.main()