import numpy as np
import random as rand
import time

class WrongBoard(Exception):
    """A board that is impossible was reached."""
    pass


class OccupiedSquare(Exception):
    """The selected squared has been already filled"""
    pass


class Board:

    """The Board class holds all the functionality of the game itself.
    It contains the necesary methods to create, show and transform the board."""

    def __init__(self) -> None:
        """Generate empty board (3x3) full of 0s."""
        self.board = np.zeros((3,3), np.int8)


    def __repr__(self) -> str:
        """Return string description."""
        return f"{type(self).__name__}\n(board={self.board})"

    def set_board(self, new_board):
        """Set manually the values of all the board.
        This function should be private and never used by the user."""

        # Check that it is an array
        if (not isinstance(new_board, np.ndarray)):
            raise WrongBoard("In set board - new board is not an array.")
        # Check that it has the correct shape
        elif (new_board.shape != (3,3)):
            raise WrongBoard("In set board - wrong dimensions.")
        # Check that it only contains valid values
        elif (any(x not in [0,1,2] for x in np.nditer(new_board))):
            raise WrongBoard("In set board - incorrect values in new board.")
        # Assing the new board
        else:
            self.board = new_board


    def show(self):
        """Print board (only for 3x3)"""

        A = [[".",".","."],[".",".","."],[".",".","."]]

        for i in range(3):
            for j in range(3):
                if (self.board[i,j] == 1): A[i][j] = "X"
                elif (self.board[i,j] == 2): A[i][j] = "O"
        
        print("\n")
        print(f"    {A[0][0]} | {A[0][1]} | {A[0][2]}")
        print("   ___________")
        print(f"    {A[1][0]} | {A[1][1]} | {A[1][2]}")
        print("   ___________")
        print(f"    {A[2][0]} | {A[2][1]} | {A[2][2]}")
        print("\n")

    def move(self, i, j):
        """Takes one board and a square and executes the correspondand move"""

        # First check that square is avaliable
        if (self.board[i,j] != 0):
            raise OccupiedSquare("Error in move: selected square is already filled.")

        # Calculate whose turn is it
        nX = sum(sum(self.board == 1))
        nO = sum(sum(self.board == 2))

        if ( (nX - nO) == 1 ): turn = 2 # Turn for Os
        elif ( nX == nO ): turn = 1 # Turn for Xs
        else: raise WrongBoard("Error in move: incorrect board.")

        # Fill square
        self.board[i,j] = turn

    def random_move(self):
        """Move in a random empty square of the board. 
        Note: different that previous random_move function, because doesn't return coordinates, but it directly moves."""

        while(True):
            # Generate random square
            i = rand.randint(0,2)
            j = rand.randint(0,2)

            # If its empty we return it
            if (self.board[i,j] == 0): 
                self.move(i,j)
                return

    def get_winner(self):
        """Return the winner of the board 1 o 2 (X o O)"""
        
        # Also check that there are no 2 different winners
        winner = []

        # Columns and rows
        for i in range(3):
            
            # Rows
            if ((self.board[i,0] == self.board[i,1] == self.board[i,2]) & (self.board[i,0] != 0)): 
                winner.append(self.board[i,0])
            # Columns
            if((self.board[0,i] == self.board[1,i] == self.board[2,i]) & (self.board[0,i] != 0)): 
                winner.append(self.board[0,i])
                
        # Diagonals
        if ((self.board[0,0] == self.board[1,1] == self.board[2,2]) & (self.board[1,1] != 0)): 
                winner.append(self.board[1,1])
        if ((self.board[0,2] == self.board[1,1] == self.board[2,0]) & (self.board[1,1] != 0)): 
                winner.append(self.board[1,1])

        _len = len(winner)

        # Check only one winner
        if _len == 0: # If no winner
            return 0
        elif (_len == 1): # If just one winner with 1 line
            return winner[0]
        elif ((_len == 2) & (winner[0] == winner[1])): # The same winner with 2 lines
            return winner[0] 
        elif (_len == 2): # If two winner lines from different teams
            raise WrongBoard("Error in board_winner - more than 1 winner.")
        else: # 3 or more winner lines
            raise WrongBoard("Error in board_winner - more than 2 winner lines.")


class GameCommunication:
    """The GameCommunication class contains all the functions related with asking and showing information to the user during the game."""

    def input_coordinates():
        """Ask the user for a row and column to move"""

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
        """Ends the game by showing which team won and the credits"""
        
        if (winner == 1): print("X wins -- TO DO Say who won")
        elif (winner == 2): print("O wins -- TO DO Say who won")
        elif (winner == 0): print("Tie!")
        else:
            raise Exception("Winner is undefined")
        print("\nBy Pablo Gallego Adrián.")

    def show_winner_end(winner, player_team, name):
        """Ends the game by showing who won and the credits"""
        
        if(winner == 0): print("It's a tie!")
        elif (winner == player_team): print("Congratulations "+name+", you won!")
        else: print("I'm sorry "+name+ ", but I won!")    

        print("\nBy Pablo Gallego Adrián.")

    def user_introduction():
        """Introduce the game for the user, asking name and team."""

        _t = 1 # Waiting time between sentences in s
        print("\n\nWelcome to the TicTacToe AI test game.\n")
        time.sleep(_t)

        name = input("Introduce your name: ")
        print("Hi " + name + ", I'm TicAI!")
        time.sleep(_t)
        print("To choose a square, write the number of the row and column (Ex: 1 3)\n")


        # We choose if the player wants to play as X o O
        xo = input("Do you want to play as X or O? (X always start): ")

        while (xo not in ["X","O","x","o"]):
            xo = input("Sorry, I didn't understand. Please write X or O: ")

        if (xo in ["X","x"]): 
            print("Great, then you will start.")
            player_team = 1
            player_turn = True
        else: 
            print("Great, then I will start.")
            player_team = 2
            player_turn = False
        time.sleep(_t)

        return name, player_team, player_turn

    def auto_introduction():
        """Introduce the game without user. """

        print("Hello, this is an auto round of the game!\n")

        name = "me"
        player_team = 1
        player_turn = True
        return name, player_team, player_turn