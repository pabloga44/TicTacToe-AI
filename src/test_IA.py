# IA tests
from classes import *

def test_IA_1():
    board = Board()
    #board.set_board(np.array([[1,0,2],[0,2,1],[1,0,0]]))
    board.set_board(np.array([[1,1,0],[0,1,2],[2,0,2]]))
    board.set_board(np.array([[0,0,0],[0,0,0],[0,0,1]]))
    board.show()

    IA = TicTacTocIA()
    i,j = IA.best_move(board, max_depth=6)
    #print(IA.best_move(board))
    board.move(i,j)
    

    print("Best move:")
    board.show()

if __name__ == "__main__":
    test_IA_1()