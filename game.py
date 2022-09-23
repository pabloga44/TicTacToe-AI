# Game script
from classes import *
import sys

def main(argv, arc):

    # Set game mode
    if (arc > 1):
        if(argv[1] == "auto"): user = False
        elif(argv[1] == "user"): user = True
        else: raise Exception("Invalid argument no 2.")
    else: user = True

    # Set IA machine
    if (arc > 2):
        if(argv[2] == "dummy"): AI = False
        else: raise Exception("Invalid argument no 3.")
    else: 
        AI = True
        IA = TicTacTocIA()


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
                if AI: 
                    i,j = IA.best_move(board, max_depth=6)
                    board.move(i,j)
                else: board.random_move()

        else: # Machine moves
            print("My turn, let me think...")
            if user and not AI: time.sleep(1.5)
            if AI: 
                i,j = IA.best_move(board, max_depth=6)
                board.move(i,j)
            else: board.random_move()
            
        board.show()
        if user: time.sleep(0.5)
        winner = board.get_winner()
        count += 1

        player_turn = not player_turn
        # End of while

    GameCommunication.show_winner_end(winner, player_team=player_team, name=name)



if __name__ == "__main__":
    main(sys.argv, len(sys.argv))