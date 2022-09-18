# Test game

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
n = 3
# board = create_board(n) -- TO DO
end = False

while (end == False):
    if player_turn:
        i = input("Enter your row: ")
        j = input("Enter your column: ")
        print(f"Your square is ({i},{j})")

        board = move(board, i, j, "???")


    player_turn = not player_turn
    # End of while



