# Functions
import numpy as np
import random as rand


class WrongBoard(Exception):
    """A board that is impossible was reached."""
    pass

# We create a custom exception for when the player chooses one filled box
# We don't want the other possible error, that the board is wrong, 
#   beacuse that error is much worse and must be studied
class OccupiedSquare(Exception):
    # The selected squared has been already filled
    pass


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
        raise OccupiedSquare("Error in move: selected square is already filled.")

    # Calculate whose turn is it
    nX = sum(sum(board == 1))
    nO = sum(sum(board == 2))

    if ( (nX - nO) == 1 ): turn = 2 # Turn for Os
    elif ( nX == nO ): turn = 1 # Turn for Xs
    else: raise WrongBoard("Error in move: incorrect board.")

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
        except ValueError: # If we enter not integer to int it raises ValueError
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

def show_team_winner_end(winner):
    # Ends the game by showing which team won and the credits
    
    if (winner == 1): print("X wins -- TO DO Say who won")
    elif (winner == 2): print("O wins -- TO DO Say who won")
    elif (winner == 0): print("Tie!")
    else:
        raise Exception("Winner is undefined")
    print("\nBy Pablo Gallego Adrián.")

def show_winner_end(winner, player_team, name):
    # Ends the game by showing who won and the credits
    
    if(winner == 0): print("It's a tie!")
    elif (winner == player_team): print("Congratulations "+name+", you won!")
    else: print("I'm sorry "+name+ ", but I won!")    

    print("\nBy Pablo Gallego Adrián.")


def board_winner(A):
    # Return the winner of the board 1 o 2 (X o O)
    
    # Also check that there is no 2 or more lines
    count = 0
    winner = 0

    # Columns and rows
    for i in range(3):
        
        # Rows
        if ((A[i,0] == A[i,1] == A[i,2]) & (A[i,0] != 0)): 
            count += 1
            winner = A[i,0]
        # Columns
        if((A[0,i] == A[1,i] == A[2,i]) & (A[0,i] != 0)): 
            count += 1
            winner = A[0,i]
            
    # Diagonals
    if ((A[0,0] == A[1,1] == A[2,2]) & (A[1,1] != 0)): 
            count += 1
            winner = A[1,1]
    if ((A[0,2] == A[1,1] == A[2,0]) & (A[1,1] != 0)): 
            count += 1
            winner = A[1,1]

    # Check only one line
    if count > 1: 
        raise WrongBoard("Error in board_winner - more than one winner line.")
    else:
        return winner
