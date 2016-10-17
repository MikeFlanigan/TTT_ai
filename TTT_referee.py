import numpy as np

def CheckScore(board):
    Win = Loss = Tie = False
    zeros = np.where(board == 0)
    if np.all(board[0,0:3] == 1) or np.all(board[1,0:3] == 1) or np.all(board[2,0:3] == 1):
        Win = True
    elif np.all(board[0:3,0] == 1) or np.all(board[0:3,1] == 1) or np.all(board[0:3,2] == 1):
        Win = True
    elif board[0,0] == 1 and board[1,1] == 1 and board[2,2] == 1:
        Win = True
    elif board[2,0] == 1 and board[1,1] == 1 and board[0,2] == 1:
        Win = True
        
    elif np.all(board[0,0:3] == 2) or np.all(board[1,0:3] == 2) or np.all(board[2,0:3] == 2):
        Loss = True
    elif np.all(board[0:3,0] == 2) or np.all(board[0:3,1] == 2) or np.all(board[0:3,2] == 2):
        Loss = True
    elif board[0,0] == 2 and board[1,1] == 2 and board[2,2] == 2:
        Loss = True
    elif board[2,0] == 2 and board[1,1] == 2 and board[0,2] == 2:
        Loss = True
    elif len(zeros[0]) == 0:
        Tie = True
    else: print("board:",board)
    return Win, Loss, Tie
