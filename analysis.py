# Performance analysis
from tkinter import N
from classes import *
import game
import time

import os, sys

class HiddenPrints:
    def __enter__(self):
        self._original_stdout = sys.stdout
        sys.stdout = open(os.devnull, 'w')

    def __exit__(self, exc_type, exc_val, exc_tb):
        sys.stdout.close()
        sys.stdout = self._original_stdout


def main():

    N_dummy = 2000
    duration = 0

    
    winners = np.array([])
    start = time.time()

    with HiddenPrints(): # Supress the screen paints as they are the main loss of time
        for i in range(N_dummy): winners = np.append(winners, game.main(user = False, AI = False) )
            
    end = time.time()
    duration = end-start

    print("\nDUMMY\n")
    print(f"Total time {N_dummy} games: {duration} s.")
    print(f"Mean time per game: {duration/N_dummy} s.\n")

    print(f"  X wins: {np.sum(winners == 1)} -> ({100* np.sum(winners == 1)/N_dummy}%).")
    print(f"  O wins: {np.sum(winners == 2)} -> ({100* np.sum(winners == 2)/N_dummy}%).")
    print(f"  Ties: {np.sum(winners == 0)} -> ({100* np.sum(winners == 0)/N_dummy}%).")


    N_IA = 10
    duration = 0

    
    winners = np.array([])
    start = time.time()

    with HiddenPrints(): # Supress the screen paints as they are the main loss of time
        for i in range(N_IA): winners = np.append(winners, game.main(user = False, AI = True) )
            
    end = time.time()
    duration = end-start

    print("\nIA GAMES\n")
    print(f"Total time {N_IA} games: {duration} s.")
    print(f"Mean time per game: {duration/N_IA} s.\n")

    print(f"  X wins: {np.sum(winners == 1)} -> ({100* np.sum(winners == 1)/N_IA}%).")
    print(f"  O wins: {np.sum(winners == 2)} -> ({100* np.sum(winners == 2)/N_IA}%).")
    print(f"  Ties: {np.sum(winners == 0)} -> ({100* np.sum(winners == 0)/N_IA}%).")
    
    return


if __name__ == "__main__":
    main()