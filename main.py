# from __future__ import print_function
from PIL import Image
from numpy import array
from procedures import *
import numpy

# numpy.set_printoptions(threshold=numpy.nan)

# # Learning rate
# alpha = 0.1

# # Weights initialisation
# num_inp_featuremaps = 2
# num_out_featuremaps = 4
# filter_height = 3
# filter_width = 3
# pooling_size = 4
# numOfWeights = len(SecondPooling)

# fan_in = (num_inp_featuremaps*filter_height*filter_width)
# fan_out = (num_out_featuremaps*filter_height*filter_width)/pooling_size

# w_bound = numpy.sqrt(6./(fan_in+fan_out))
# # Weights creates a matrix of numOfWeights*2 size
# w = numpy.random.uniform(-w_bound,w_bound,(numOfWeights,2))

# # Initialising weight update array
# deltaW = numpy.zeros_like(w)

# Gradient
def gradient(x):
	if x > 0:
		return 1
	else:
		return 0 


# Takes image as input and coverts it into required input of pixels (either 1 or -1)
def ProcessImage():
	#B/W image , called as monogram not grayscale (i did not choose grayscale)
	image = Image.open("conv1.jpg")
	# Converts image into array of pixels
	arr = array(image)
	# label = x or o
	# Pre-processing
	# converts 255 (white) to -1 and 0 (black) to 1
	data = []
	for p in arr:
		temp = []
		for q in p:
			x = float(q)/255
			y = int(round(x))
			if y == 0:
				temp.append(1)
			elif y == 1:
				temp.append(-1)
		data.append(temp)
	return data

# p = Procedures()

# # Creating 2 filters for First Convolution layer
# FilterOne = p.InitFilter()
# FilterTwo = p.InitFilter()

# Creating 4 filters for Second Convolution layer 
# (No. of filters needs to increased inorder to focus on more complex features)
# FilterThree = p.InitFilter()
# FilterFour = p.InitFilter()
# FilterFive = p.InitFilter()
# FilterSix = p.InitFilter()

# # input
# input_data = ProcessImage()

# # First Iteration
# # Convloution
# FirstConv = p.convolution(input_data)

# # ReLu
# FirstReLu = p.reLu(FirstConv)

# # Pooling
# FirstPooling = p.pooling(FirstReLu)


# # Second Iteration
# # Convloution
# SecondConv = p.convolution(FirstPooling)

# # ReLu
# SecondReLu = p.reLu(SecondConv)

# # Pooling
# SecondPooling = p.pooling(SecondReLu)

# Fully Connected Layer
# FC = 1d array of SecondPooling

# Dot product b/w FullyConnected Layer and Weigths (1*n)(n*2) = (1*2)
output = numpy.dot(FC,W)

# Error from X and O
error_X = 0 - output[0]
error_O = 1 - output[1]

# Total Error
error = (numpy.absolute(error_X) + numpy.absolute(error_O))*gradient()

# updating the weight
w = w + (deltaW*alpha)