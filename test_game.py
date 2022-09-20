from venv import create
import functions
import sys

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

    board = functions.create_board()
    board = functions.move(board,1,1)
    
    # Check that it doesn't accept other indexes
    try:
        functions.move(board,0,4)
        raise Exception("Error in test move: move(0,4) did not fail.")
    except IndexError:
        pass

    try:
        board = functions.move(board,1,1)
        raise Exception("Error in test move: didn't fail when trying to rewrite a square.")
    
    except functions.OccupiedSquare:
        pass
    board = functions.move(board,1,2)
    return