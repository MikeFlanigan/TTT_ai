# TTT_brain 
import numpy as np
import os

P1TmpHist = np.zeros((1,9),dtype = np.int)
P2TmpHist = np.zeros((1,9),dtype = np.int)


def init_memory():
    if os.path.isfile('positive_memories.npy'):
        good_data = np.load('positive_memories.npy')
    if os.path.isfile('negative_memories.npy'):
        bad_data = np.load('negative_memories.npy')
    return


def SaveTmp(P1Turn,move,OldBoard):
    global P1TmpHist, P2TmpHist
    if P1Turn:
        if np.all(P1TmpHist[0,:]==0) and len(P1TmpHist[0,:]) == 9:
            P1TmpHist = np.reshape(np.append(np.ravel(OldBoard),move),(1,10))
        else:
            newVec = np.reshape(np.append(np.ravel(OldBoard),move),(1,10))
            P1TmpHist = np.concatenate((P1TmpHist,newVec),0) 
    else:
        if np.all(P2TmpHist[0,:]==0) and len(P2TmpHist[0,:]) == 9:
            P2TmpHist = np.reshape(np.append(np.ravel(OldBoard),move),(1,10))
        else:
            newVec = np.reshape(np.append(np.ravel(OldBoard),move),(1,10))
            P2TmpHist = np.concatenate((P2TmpHist,newVec),0)
    return


    
def Label_and_Remember(Win, Loss, Tie): # wrt P1
    if Win or Tie:
        try:
            np.save('positive_memories.npy',np.concatenate((good_data,P1TmpHist),0))
        except NameError:
            print('Good data undefined')
            good_data = P1TmpHist
            np.save('positive_memories.npy',good_data)
        try:
            buffer = np.zeros((len(P2TmpHist[:,0]),9),dtype=np.int)
            buffer[P2TmpHist[:,0:9]==1] = 2
            buffer[P2TmpHist[:,0:9]==2] = 1
            buffer = np.concatenate((buffer, np.reshape(P2TmpHist[:,9],(len(P2TmpHist[:,0]),1))),1)
            bad_data = np.concatenate((bad_data,buffer),0)
            np.save('negative_memories.npy',bad_data)
        except NameError:
            print('Bad data undefined')
            bad_data = buffer
            np.save('negative_memories.npy',bad_data)

    if Loss:
        try:
            np.save('negative_memories.npy',np.concatenate((bad_data,P1TmpHist),0))
        except NameError:
            print('Bad data undefined')
            bad_data = P1TmpHist
            np.save('negative_memories.npy',bad_data)
        try:
            buffer = np.zeros((len(P2TmpHist[:,0]),9),dtype=np.int)
            buffer[P2TmpHist[:,0:9]==1] = 2
            buffer[P2TmpHist[:,0:9]==2] = 1
            buffer = np.concatenate((buffer, np.reshape(P2TmpHist[:,9],(len(P2TmpHist[:,0]),1))),1)
            good_data = np.concatenate((good_data,buffer),0)
            np.save('positive_memories.npy',good_data)
        except NameError:
            print('Good data undefined')
            goodd_data = buffer
            np.save('positive_memories.npy',good_data)
    return

def ClearTmp():
    global P1TmpHist, P2TmpHist
    P1TmpHist = np.zeros((1,9),dtype = np.int)
    P2TmpHist = np.zeros((1,9),dtype = np.int)
    print("cleared temporary game history")
    return
