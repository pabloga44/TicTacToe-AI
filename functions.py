# Functions
import numpy as np
import random as rand

def create_board():
    # Generate empty board (3x3) full of 0s
    return np.zeros((3,3), np.int8)
    

def print_board(board):
    # Print board (only for 3x3)
    A = [[".",".","."],[".",".","."],[".",".","."]]

    for i in range(3):
        for j in range(3):
            if (board[i,j] == 1): A[i][j] = "X"
            elif (board[i,j] == 2): A[i][j] = "O"
    
    print(f"    {A[0][0]} | {A[0][1]} | {A[0][2]}")
    print("   ___________")
    print(f"    {A[1][0]} | {A[1][1]} | {A[1][2]}")
    print("   ___________")
    print(f"    {A[2][0]} | {A[2][1]} | {A[2][2]}")

    return


def move(board, i, j):
    # Takes one board and a square and executes the correspondand move

    # First check that square is avaliable
    if (board[i,j] != 0):
        raise Exception("Error in move: selected square is already filled.")

    # Calculate whose turn is it
    nX = sum(sum(board == 1))
    nO = sum(sum(board == 2))

    if ( (nX - nO) == 1 ): turn = 2 # Turn for Os
    elif ( nX == nO ): turn = 1 # Turn for Xs
    else: raise Exception("Error in move: incorrect board.")

    # Fill square
    board[i,j] = turn

    return board


def random_move(board):
    # Select a random empty square of the board

    while(True):
        # Generate random square
        i = rand.randint(0,2)
        j = rand.randint(0,2)

        # If its empty we return it
        if (board[i,j] == 0): 
            return i,j