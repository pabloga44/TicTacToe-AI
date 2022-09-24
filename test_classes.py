# Classes tests
from classes import *
import sys
import game

def test_board_creation():
    """Check the that the instatiation of a board,
     and the two ways of visualization don't crash"""

    board = Board()
    print(board)
    board.show()
    return


def test_input_coordinates():
    """Test the inputation of coordinates by the user"""

    sys.stdin = open("test_inputs/test_input_coordinates.txt") # We choose the same name for organization
    i,j =  GameCommunication.input_coordinates()
    assert i in [0,1,2]
    assert j in [0,1,2]
    return


def test_move():
    """Test a couple of movements in the board, check that it doesn't crash
    when selecting an occupied square"""

    # Create board and first move
    board = Board()
    board.move(1,1)
    
    # Check that it doesn't accept other indexes
    try:
        board.move(0,4)
        raise Exception("Error in test move: move(0,4) did not fail.")
    except IndexError:
        pass

    # Check that it doesn't allow me to rewrite a square
    try:
        board.move(1,1)
        raise Exception("Error in test move: didn't fail when trying to rewrite a square.")
    except OccupiedSquare:
        pass

    # Another normal move
    board.move(1,2)
    return


def test_set():
    """Test the function set_board."""

    # Create board
    board = Board()

    # Check it doesn't allow other values
    try:
        board.set_board(np.array([[8,1,1],[0,2,0],[2,3,2]]))
        raise Exception("Test_set: it accepted a wrong value.")
    except WrongBoard:
        pass

    # Check it doesn't accept other shapes
    try:
        board.set_board(np.array([[8,1],[0,2],[2,2]]))
        raise Exception("Test_set: it accepted a wrong value.")
    except WrongBoard:
        pass

    # Check it doesn't accept random things
    try:
        board.set_board("this is a test")
        raise Exception("Test_set: it accepted something that was not an array.")
    except WrongBoard:
        pass

    # Check that it does the assignation correctly
    board.set_board(np.array([[0,2,1],[0,2,0],[2,0,2]]))
    assert (board.board == np.array([[0,2,1],[0,2,0],[2,0,2]])).all()


def test_winner():
    """Test the function that evaluates a board and return its winner (X or O)"""

    board = Board()
    board.set_board(np.array([[1,1,1],[0,2,0],[1,2,2]]))
    assert board.get_winner() == 1

    board.set_board(np.array([[2,1,1],[0,2,0],[1,2,2]]))
    assert board.get_winner() == 2

    board.set_board(np.array([[0,1,1],[0,2,0],[1,0,2]]))
    assert board.get_winner() == 0

    # 2 lines different winner
    try:
        board.set_board(np.array([[1,1,1],[0,2,0],[2,2,2]]))
        w = board.get_winner()
        raise Exception("Test_winner: it accepted a wrong board.")
    except WrongBoard:
        pass

    # 2 lines of the same winner
    board.set_board(np.array([[1,1,1],[0,2,1],[1,0,1]]))
    assert board.get_winner() == 1

    return


def test_full_auto_game():
    """Run a full game of the machine against itself, just to check that nothing crashes."""
    
    sys.stdin = open("test_inputs/args.txt")
    game.main()
    return