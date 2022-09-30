# TicTacToe-AI

UNDER DEVELOPMENT

## Welcome to the Pablo's TicTacToe AI project.
In this repository you will find a complete implementation of the TicTacToe game in Python that allows one user play against a machine with different levels of difficulty.

The game is displayed in a terminal, so in order to play you must run the script src/game.py
The game also allows different play modalities, that you can handle trough the arguments of the script:
- -mode: allows you to choose whether you want to play against the machine ("user") or if you want to watch a test game of the machine against itself ("auto").
The default value for this argument is "user".
- -level: allows you to choose the difficulty of the game. ("dummy") makes you play against a random mover machine that is not difficult to beat, while ("IA") makes you play against a complete Artificial Inteligence with 0% chances of loosing (don't believe me?)

In the *src* folder, next to the main script game.py you will also find the module _classes.py_ whith all the functionality of the game and the IA, the script _analysis.py_ that makes a brief study of the behavior of both agents, and several tests that you can run by using the _pytest_ library.

In the *doc* folder you will find documentation of the code, generated using the pdoc3 package.

In _requirements.txt_ you will find all the necessary packages to run the application, test it and update the documentation if needed.

*NOTE*: This version is still in process of being completed as the alpha-beta pruning is not fully implemented yet, causing the IA to work significantly slower than it should. We hope that we will be able to solve it soon.
