# Game script
from classes import *
import sys
import argparse

def main(user, AI):

    if AI: IA = TicTacTocIA()

    # Introduction to the game
    if user:
        name, player_team, player_turn = GameCommunication.user_introduction(AI)
    else:
        name, player_team, player_turn = GameCommunication.auto_introduction(AI)

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
                    i,j = IA.best_move(board, max_depth=8)
                    board.move(i,j)
                else: board.random_move()

        else: # Machine moves
            print("My turn, let me think...")
            if user and not AI: time.sleep(1.5)
            if AI: 
                i,j = IA.best_move(board, max_depth=8)
                board.move(i,j)
            else: board.random_move()
            
        board.show()
        if user: time.sleep(0.5)
        winner = board.get_winner()
        count += 1

        player_turn = not player_turn
        # End of while

    GameCommunication.show_winner_end(winner, player_team=player_team, name=name)
    return winner


if __name__ == "__main__":

    # Argument parser
    parser = argparse.ArgumentParser()
    parser.add_argument("-mode", type=str, default="user", help="Player mode: user (play against the machine), auto (machine against itself)")
    parser.add_argument("-level", type=str, default="IA", help="Machine level of dificulty: dummy (random moves), IA (perfect machine)")
    args = parser.parse_args()

    # Using the arguments
    if(args.mode == "auto"): user = False
    elif(args.mode == "user"): user = True
    else: raise Exception("Invalid argument mode.")

    if(args.level == "dummy"): AI = False
    elif(args.level == "IA"):  AI = True
    else: raise Exception("Invalid argument level.")

    main(user, AI)