import numpy as np

class Board:

    """The Board class holds all the functionality of the game itself.
    It contains the necesary methods to create, show and transform the board."""

    def __init__(self) -> None:
        """Generate empty board (3x3) full of 0s."""
        self.board = np.zeros((3,3), np.int8)


    def __repr__(self) -> str:
        """Return string description."""
        return f"{type(self).__name__}\n(board={self.board})"

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

    
