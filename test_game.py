import functions
import sys
import numpy as np

def test_input_coordinates():
    """Test the inputation of coordinates by the user"""

    sys.stdin = open("test_inputs/test_input_coordinates.txt") # We choose the same name for organization
    i,j = functions.input_coordinates()
    assert i in [0,1,2]
    assert j in [0,1,2]
    return


def test_move():
    """Test a couple of movements in the board, check that it doesn't crash
    when selecting an occupied square"""

    # Create board and first move
    board = functions.create_board()
    board = functions.move(board,1,1)
    
    # Check that it doesn't accept other indexes
    try:
        functions.move(board,0,4)
        raise Exception("Error in test move: move(0,4) did not fail.")
    except IndexError:
        pass

    # Check that it doesn't allow me to rewrite a square
    try:
        board = functions.move(board,1,1)
        raise Exception("Error in test move: didn't fail when trying to rewrite a square.")
    except functions.OccupiedSquare:
        pass

    # Another normal move
    board = functions.move(board,1,2)
    return


def test_winner():
    """Test the function that evaluates a board and return its winner (X or O)"""

    board1 = np.array([[1,1,1],[0,2,0],[1,2,2]])
    assert functions.board_winner(board1) == 1

    board2 = np.array([[2,1,1],[0,2,0],[1,2,2]])
    assert functions.board_winner(board2) == 2

    board3 = np.array([[0,1,1],[0,2,0],[1,0,2]])
    assert functions.board_winner(board3) == 0

    try:
        board4 = np.array([[1,1,1],[0,2,0],[2,2,2]])
        w = functions.board_winner(board4)
        raise Exception("Test_winner: it accepted a wrong board.")
    except functions.WrongBoard:
        pass

    return