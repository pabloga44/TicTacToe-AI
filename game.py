# Game script
from classes import *
import sys


def main(argv, arc):

    if (arc > 1):
        print(argv[1])
        if(argv[1] == "auto"): user = False
        else:
            raise Exception("Invalid argument.")
    else:
        user = True

    # Introduction to the game
    if user:
        name, player_team, player_turn = GameCommunication.user_introduction()
    else:
        name, player_team, player_turn = GameCommunication.auto_introduction()

    # Start the game
    board = Board()
    board.show()

    winner = 0
    count = 1
    while ((winner == 0) and count <= 9):
        if player_turn:

            valid_move = False

            if user: # User moves
                while (not valid_move):
                    # Ask the player to choose their square
                    i, j = GameCommunication.input_coordinates()  
                    try:
                        board.move(i, j) 
                        valid_move = True
                    except OccupiedSquare as ex: # We only catch if the square is occupied, not the other error, that is worse
                        print(f"  {ex} Please enter your square again.")

            else: # Play against itself (user also machine)
                print("My turn:")
                board.random_move()

        else: # Machine moves
            print("My turn:")
            board.random_move()
            
        board.show()
        winner = board.get_winner()
        count += 1

        player_turn = not player_turn
        # End of while

    GameCommunication.show_winner_end(winner, player_team=player_team, name=name)



if __name__ == "__main__":
    main(sys.argv, len(sys.argv))