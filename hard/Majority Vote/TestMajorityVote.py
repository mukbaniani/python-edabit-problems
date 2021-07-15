import unittest
from majority_vote import majority_vote


class TestMajorityVote(unittest.TestCase):
    def test_majority_vote(self):
        self.assertEqual(majority_vote(["A", "B", "B", "B", "A", "A"]), None)
        self.assertEqual(majority_vote(["B", "B", "B"]), "B")
        self.assertEqual(majority_vote(["A", "B", "B"]), "B")
        self.assertEqual(majority_vote(["A", "A", "B"]), "A")
        self.assertEqual(majority_vote(["A", "A", "A", "B", "C", "A"]), "A")
        self.assertEqual(majority_vote(["B", "A", "B", "B", "C", "A", "B", "B"]), "B")
        self.assertEqual(majority_vote(["A", "B", "B", "A", "C", "C"]), None)
        self.assertEqual(majority_vote(["A", "B"]), None)
        self.assertEqual(majority_vote(["A"]), "A")
        self.assertEqual(majority_vote([]), None)


if __name__ == '__main__':
    unittest.main()