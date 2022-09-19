# Test game
from functions import *

# Introduction
print("\n\nWelcome to the TicTacToe AI test game.\n")

name = input("Introduce your name: ")
print("Hi " + name + ", I'm TicAI!")

print("To choose a square, write the number of the row and column (Ex: 1 3)\n")


# We choose if the player wants to play as X o O
xo = input("Do you want to play as X or O? (X always start): ")

while (xo not in ["X","O","x","o"]):
    xo = input("Sorry, I didn't understand. Please write X or O: ")

if (xo in ["X","x"]): 
    print("Great, then you will start.")
    player_turn = True
else: 
    print("Great, then I will start.")
    player_turn = False



# Start the game
# n = 3
board = create_board()
print_board(board)

end = False

while (end == False):
    if player_turn:


        while True:
            try:
                i = int(input("Enter your row: ")) - 1  # We already change it to 0-2 format
                break
            except ValueError:
                print("Please input integer only...")  
                continue
        while True:
            try:
                j = int(input("Enter your column: ")) - 1  # We already change it to 0-2 format
                break
            except ValueError:
                print("Please input integer only...")  
                continue

        print(f"Your square (in matrix notation) is ({i},{j})")

        board = move(board, i, j) # Information about who is the one that moves is redundant
        print_board(board)

    else: 
        i,j = random_move(board) # HERE IT WILL GO THE AI
        board = move(board, i, j)
        print_board(board)

    #if(winner(board) != 0): end = True -- TO DO

    player_turn = not player_turn
    # End of while



