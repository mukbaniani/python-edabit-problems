import numpy as np


def tic_tac_toe(board):
	array_board = np.array(board)
	array_board_T = array_board.T
	for i, j in zip(array_board, array_board_T):
		if len(set(i)) == 1:
			return i[0]
		elif len(set(array_board.diagonal())) == 1:
			return array_board.diagonal()[0]
		elif len(set(j)) == 1:
			return j[0]
	return 'Draw'