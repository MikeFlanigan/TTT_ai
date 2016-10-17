import TTT_UX_and_Graphics as UG
import TTT_referee as ref
import TTT_brain as brain
import random
import numpy as np


Running = True
Stop = False

GameMode = 0

while not Stop:
    if GameMode == 0:
        UG.Init_Board() # draw board and setup game
        brain.ClearTmp()
        OldBoard = np.zeros((3,3),dtype=np.int)
        board = np.zeros((3,3),dtype=np.int)
        GameMode = UG.ChooseMode()
        print("GameMode:",GameMode)
        InPlay = True
        P1Turn = True
        
    if GameMode == 2: # replace nums with vars
        aiP1 = random.choice([True, False]) # returns T/F for if ai is Player 1
    while InPlay:
        
        if GameMode == 1:
            OldBoard = board
            if P1Turn:
                move, board, Stop = UG.HumanMove(P1Turn,board)
                brain.SaveTmp(P1Turn,move,OldBoard)
                P1Turn = False 
            else:
                move, board, Stop = UG.HumanMove(P1Turn,board)
                brain.SaveTmp(P1Turn,move,OldBoard)
                P1Turn = True
            
##        if GameMode == 2:
##            if P1Turn:
##                if aiP1:
##                    move, board = ai.move(P1Turn,OldBoard)
##                else:   
##                    move, board = UG.HumanMove(P1Turn,OldBoard)
##                brain.SaveTmp(P1Turn,move,OldBoard)
##                P1Turn = False 
##            else:
##                if not aiP1:
##                    move, board = ai.move(P1Turn,OldBoard)
##                else:   
##                    move, board = UG.HumanMove(P1Turn,OldBoard)
##                brain.SaveTmp(P1Turn,move,OldBoard)
##                P1Turn = True
                
        UG.Update_Board(board) # draw
        
        Win, Loss, Tie = ref.CheckScore(board) # returns wrt P1
        if Win or Loss or Tie:
##            brain.Label_and_Remember(Win, Loss, Tie, board)
            brain.ClearTmp()
            GameMode = 0
            InPlay = False
            print(Win,Loss,Tie)

        if Stop:
            InPlay = False

            

        
        




