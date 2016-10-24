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

def sigmoid(z):
    sig = 1/(1+np.exp(-z))
    return sig
def NN_randInitWeights(Lin,Lout):
    epsilon_init = np.sqrt(6)/np.sqrt(Lin+Lout)
    theta = np.random.rand(Lout,Lin + 1) # generate random theta weights from 0-1
    theta = theta*2*epsilon_init - epsilon_init
    return theta

def NN_predict(Theta1,Theta2,X):
    ## hacking to only predict on a single X vec for now, change to handle matrix or vec later
    X = np.asarray(X)
    print('len x:',len(X))
    X = np.reshape(X,(1,len(X)))
    print('shape x:',np.shape(X))
    print('x:',X)
    
    m=len(X[:,0])
    print('m',m)
##    m = np.size(X[:,0])
    num_classes = len(Theta2[:,0]) # number of nodes in the output layer
    pred = np.zeros((num_classes,1)) # defaults to dtype np float 64

    # check if the data set had bias units already added, add them if not
##    if not np.all(X[:,0]==1): 
##        X = np.concatenate((np.ones((m,1)),X),1)
    # hack job here
    
    if np.size(X[0,:]) == 9:
        X = np.insert(X,0,1) # inserts 1 into position 0 of X
        print("added bias unit, X:",X)
##    print('theta1 shape:',np.shape(Theta1))
##    print('Xt shape:',np.shape(np.transpose(X)))
    z2 = np.dot(Theta1,np.transpose(X))
    print('z2 shape:',np.shape(z2)) # 9x15
##    a2 = np.concatenate((np.ones((1,m)),sigmoid(z2)),0) # hack
    a2 = np.insert(sigmoid(z2),0,1)
    print('a2 shape:',np.shape(a2)) # 10x15 since added bias node j0
    z3 = np.dot(Theta2,a2)
    print('z3 shape:',np.shape(z3)) #
    a3 = class_conf = sigmoid(z3)
    predict = np.where( class_conf == np.amax(class_conf))
    pred_conf = np.amax(class_conf)
    return predict, pred_conf, class_conf

## load training data (just good for now)
if os.path.isfile('positive_memories.npy'):
    good_data = np.load('positive_memories.npy')
    print("success loading good data")
    print(good_data)

# splitting inputs and outputs
m = len(good_data[:,0]) # number of training examples
X = good_data[:,:-1]
##X = np.concatenate((np.ones((m,1)),X),1) # add ones for bias units
y = good_data[:,len(good_data[0,:])-1]
y = np.reshape(y,(m,1)) # reshape to a column


## corresponds to a NN architecure with 3 layers
input_layer_size = 9
hidden_layer_size = 9
num_labels = 9

Theta1 = NN_randInitWeights(input_layer_size,hidden_layer_size) 
##print("theta1",Theta1)
Theta2 = NN_randInitWeights(hidden_layer_size, num_labels)
##print("theta2",Theta2)

# func has a hack to only work for a vec X input currently
pred_label, pred_confidence, all_confidences = NN_predict(Theta1,Theta2,X[2,:])
print('prediction:',pred_label)
print('prediction confidence:', pred_confidence)
print('Full class predictions:', all_confidences)


