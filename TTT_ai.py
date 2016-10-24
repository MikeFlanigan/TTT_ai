import os
import numpy as np
# init ai will define architecture

## ooh this could get hard... was thinking would need to train between moves
# and got scared of processing time
''' actually can learn (train) between games. when click play again or
when click hvr or rvr ... pause where ai "learns from memory"
makes sense since it would n't change weights on current moves since doesn't
know if it will win or lose
this is a direct trait of a RL problem I believe.
'''
## Take one outline
'''
goal is to get this to run on it's own and first make predicitions
then write the code to train it


train all sets where will
define nueral net archit
    layout archi
learn-from-memo
    will def cost and gradients... octave checks
    will calculate theta weights is critical

ai_move
    then can use fp to predict probablility of a good move
    same for bad move
    good %s - bad %s (only if bads are grt 50? why)
    need catches at 0 prevent negatives

    choose maximum percent move
    return
'''

def NN_randInitWeights(Lin,Lout):
    epsilon_init = np.sqrt(6)/np.sqrt(Lin+Lout)
    theta = np.random.rand(Lout,Lin + 1) # generate random theta weights from 0-1
    theta = theta*2*epsilon_init - epsilon_init
    return theta

def NN_predict(Theta1,Theta2,X):
    m = len(X[:,0])
    num_classes = len(Theta2[:,0]) # number of nodes in the output layer
    pred = np.zeros((num_classes,1))
    return label

## load training data (just good for now)
if os.path.isfile('positive_memories.npy'):
    good_data = np.load('positive_memories.npy')
    print("success loading good data")
    print(good_data)
    
m = len(good_data[:,0]) # number of training examples

## corresponds to a NN architecure with 3 layers
input_layer_size = 9
hidden_layer_size = 9
num_labels = 9

Theta1 = NN_randInitWeights(input_layer_size,hidden_layer_size)
##print("theta1",Theta1)
Theta2 = NN_randInitWeights(hidden_layer_size, num_labels)
##print("theta2",Theta2)


