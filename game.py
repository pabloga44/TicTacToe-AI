# Test game
from classes import *


def main():

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
        player_team = 1
        player_turn = True
    else: 
        print("Great, then I will start.")
        player_team = 2
        player_turn = False


    # Start the game
    # n = 3
    board = Board()
    board.show()

    winner = 0
    count = 1
    while ((winner == 0) and count <= 9):
        if player_turn:

            valid_move = False
            while (not valid_move):
                # Ask the player to choose their square
                i, j = GameCommunication.input_coordinates()  
                try:
                    board.move(i, j) 
                    valid_move = True
                except OccupiedSquare as ex: # We only catch if the square is occupied, not the other error, that is worse
                    print(f"  {ex} Please enter your square again.")

        else: 
            print("My turn:")
            board.random_move()
            
        board.show()
        winner = board.get_winner()
        count += 1

        player_turn = not player_turn
        # End of while

    GameCommunication.show_winner_end(winner, player_team=player_team, name=name)



if __name__ == "__main__":
    main()