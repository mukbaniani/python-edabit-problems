import unittest
from tic_tac_toe import tic_tac_toe


class TestTicTacToe(unittest.TestCase):
    def test_tic_tac_toe(self):
        self.assertEqual(tic_tac_toe([
            ["X", "O", "X"],
            ["O", "X", "O"],
            ["O", "X", "X"]
        ]), "X")

        self.assertEqual(tic_tac_toe([
            ["O", "O", "O"],
            ["O", "X", "X"],
            ["E", "X", "X"]
        ]), "O")

        self.assertEqual(tic_tac_toe([
            ["X", "X", "O"],
            ["O", "O", "X"],
            ["X", "X", "O"]
        ]), "Draw")

        self.assertEqual(tic_tac_toe([
            ["X", "O", "O"],
            ["X", "O", "O"],
            ["X", "X", "X"]
        ]), "X")

        self.assertEqual(tic_tac_toe([
            ["X", "X", "O"],
            ["O", "O", "X"],
            ["X", "X", "O"]
        ]), "Draw")

        self.assertEqual(tic_tac_toe([
            ["X", "O", "X"],
            ["O", "X", "O"],
            ["E", "E", "X"]
        ]), "X")

        self.assertEqual(tic_tac_toe([
            ["X", "O", "E"],
            ["X", "O", "E"],
            ["E", "O", "X"]
        ]), "O")


if __name__ == '__main__':
    unittest.main()