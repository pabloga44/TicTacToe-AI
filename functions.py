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
    
    print("\n")
    print(f"    {A[0][0]} | {A[0][1]} | {A[0][2]}")
    print("   ___________")
    print(f"    {A[1][0]} | {A[1][1]} | {A[1][2]}")
    print("   ___________")
    print(f"    {A[2][0]} | {A[2][1]} | {A[2][2]}")
    print("\n")

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


def input_coordinates():
    # Ask the user for a row and column to move

    valid_i = False
    while (not valid_i):
        try: # In case the user doesn't introduce an integer
            i = int(input("Enter your row: ")) - 1  # We already change it to 0-2 format
            if (i in [0,1,2]): # In case the user introduces a different integer
                valid_i = True
            else:
                print("Please enter a valid row (1,2,3)")
        except ValueError:
            print("Please enter a valid row (1,2,3)")  
            
    valid_j = False
    while (not valid_j):
        try:
            j = int(input("Enter your column: ")) - 1  # We already change it to 0-2 format
            if (j in [0,1,2]):
                valid_j = True
            else:
                print("Please enter a valid column (1,2,3)")
        except ValueError:
            print("Please enter a valid column (1,2,3)")

    return i, j

def show_winner_end(winner):
    # Ends the game by showing who won and the credits
    # ---- TO DO: Specify who won------
    if (winner == 1): print("X wins -- TO DO Say who won")
    elif (winner == 2): print("O wins -- TO DO Say who won")
    elif (winner == 0): print("Tie!")
    else:
        raise Exception("Winner is undefined")
    print("\nBy Pablo Gallego Adrián.")


def board_winner():
    return