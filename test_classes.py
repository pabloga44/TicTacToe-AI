# Classes tests
from classes import Board

def test_board_creation():
    """Check the that the instatiation of a board,
     and the two ways of visualization don't crash"""

    board = Board()
    print(board)
    board.show()