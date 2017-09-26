#forward pass
def relu_activation_fn

def local_gradient

# Hyper Parameters

# 2 Filters
def filter

def Padding

# Procedure Functions
def Convolution

# This is same as relu activation_fn
# def ReLu

def Pooling

def FullyConnectedLayer



x = input image

#Weight init
W = random.range[-1/sqrt(No. of neurons),1/sqrt(No. of neurons)] # Xavier initialisation

# bias 
b = 0 or 1




#Training

Convolution(x)
reLu(x)
Convolution(x)
reLu(x)
Pooling(x)
FullyConnectedLayer(x)

# error at 2 output neurons
deltaW_FOR_X = [1  - output1] 
# 1 is label for X,
# Output1 is the output after dot product of neurons in FullyConnected layer and respective synapes
deltaW_FOR_O = [0  - output2]
# 0 is label for O,
# Output2 is the output after dot product of neurons in FullyConnected layer and respective synapes

#backward pass
def gradient

def Backprop

# Total error
deltaW = [deltaW_FOR_X + mod(deltaW_FOR_O)]*gradient
Backprop()
W = W + (deltaW*alpha)

#Testing
# Show reduction in  error while providing the label as we did in RNN


