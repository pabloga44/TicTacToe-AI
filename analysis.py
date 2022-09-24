# Performance analysis
from tkinter import N
from classes import *
import game
import time


def main():

    N = 5
    duration = 0

    for i in range(N):
        start = time.time()
        game.main(user = False, AI = True)
        end = time.time()
        duration += end-start

    print(f"Total time: {duration} s.")
    print(f"Mean time per game: {duration/N} s.")
    return


if __name__ == "__main__":
    main()