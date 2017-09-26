def relu_activation_fn

def gradient

# Hyper Parameters

# 2 Filters
def filter

def Padding

# Procedure Functions
def Convolution

def ReLu

def Pooling

def FullyConnectedLayer

def Backprop

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

#error
deltaW = label(0/1) - (???)
Backprop()
W = w + (deltaW*alpha)

#Testing
# Show reduction in  error while providing the label as we did in RNN


