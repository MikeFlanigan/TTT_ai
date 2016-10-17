import TTT_UX_and_Graphics as UG
##from TTT_UX_and_Graphics import *

done = False
## draw board and setup game
UG.Init_Game()


## send and manage a control panel
# h-h,h-r,exit? (not needed immediatle, nicer than x button tho)
# X always goes first?

idle = 0
Choose_Mode = 1 
HvH = 2
HvR = 3
RvR = 4
NextMove = 10

done, ret_mode = UG.Uin(Choose_Mode)
if done:
    UG.Draw_Board()

done, ret_mode,  = UG.Uin(ret_mode)
if done:
    # next move

    

while state == Choose_Mode:
    
        state = 
while state == playing 
##    done = Uin(HvH)

    

# playing loop here yes, with states "while choosing mode" while "playing"

# NewMove = uin(next move   human? robot? both?) #add a return of the move played
# if hvr or rvr
# move = ai_move() # return move, good %s, bad %s
# game_mode = check_score(board) 


'''
remember(NewMove [0-8], P1Move[t/f], board, game_done[0-2])
need to ravel and save to a temporary buffer array every game state
and the resulting move (concatenate to the last row)
then when the game finishes 
'''

# quit always possible... clicking on quit

# check who won
 # if game mode != 0
     # displaywinner() graphics and ux func
     # maybe tally score at some point




