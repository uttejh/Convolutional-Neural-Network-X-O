# from __future__ import print_function
from PIL import Image
from numpy import array
from procedures import *
import numpy
import time

# numpy.set_printoptions(threshold=numpy.nan)

# Gradient
def gradient(x):
	if x > 0:
		return 1
	else:
		return 0 

def error_filter(filt, error):
	err = []
	length = len(filt)
	size = length*length

	for i in range(size):
		for j in range(length):
			e = error*gradient(filt[i][j])
			err.append(e)

	return err  



# Takes image as input and coverts it into required input of pixels (either 1 or -1)
def ProcessImage(numb):
	im = 'conv'+str(numb)
	#B/W image , called as monogram not grayscale (i did not choose grayscale)
	image = Image.open(im)
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

# Learning rate
alpha = 0.1

# Weights initialisation
num_inp_featuremaps = 2
num_out_featuremaps = 4
filter_height = 3
filter_width = 3
pooling_size = 4
numOfWeights = len(SecondPooling)

fan_in = (num_inp_featuremaps*filter_height*filter_width)
fan_out = (num_out_featuremaps*filter_height*filter_width)/pooling_size

w_bound = numpy.sqrt(6./(fan_in+fan_out))
# Weights creates a matrix of numOfWeights*2 size
w_fc = numpy.random.uniform(-w_bound,w_bound,(numOfWeights,2))

# Initialising weight update array
deltaW_fc = numpy.zeros_like(w)


p = Procedures()

# Creating 2 filters for First Convolution layer
FilterOne = p.InitFilter()
FilterTwo = p.InitFilter()

# Creating 4 filters for Second Convolution layer 
(No. of filters needs to increased inorder to focus on more complex features)
FilterThree = p.InitFilter()
FilterFour = p.InitFilter()
FilterFive = p.InitFilter()
FilterSix = p.InitFilter()

for iterat in range(10):
	# Calculates execution time
	start = time.clock()

	# input
	input_data = ProcessImage(iterat)
	if (iterat%2) == 0:
		label = 1
		ans = 'O'
	else:
		label = 0
		ans = 'X'

	# First Iteration
	# Convloution
	FirstConv = p.convolution(input_data)

	# ReLu
	FirstReLu = p.reLu(FirstConv)

	# Pooling
	FirstPooling = p.pooling(FirstReLu)


	# Second Iteration
	# Convloution
	SecondConv = p.convolution(FirstPooling)

	# ReLu
	SecondReLu = p.reLu(SecondConv)

	# Pooling
	SecondPooling = p.pooling(SecondReLu)

	# Fully Connected Layer
	# FC = 1d array of SecondPooling

	output = []

	# Dot product b/w FullyConnected Layer and Weigths (1*n)(n*2) = (1*2)
	output = numpy.dot(FC,W)

	# Error from X and O
	error_X = 0 - output[0]
	error_O = 1 - output[1]

	absErrX = numpy.absolute(error_X)
	absErrO = numpy.absolute(error_O)

	# Total Error
	error = ( absErrX + absErrO)

	deltaW_fc = numpy.dot(FC, error)
	# updating the weight
	w_fc = w_fc + (deltaW_fc*alpha)


	FilterOne_update = numpy.dot(FilterOne, error_filter(FilterOne, error)) 
	FilterTwo_update = numpy.dot(FilterTwo, error_filter(FilterTwo, error)) 
	FilterThree_update = numpy.dot(FilterThree, error_filter(FilterThree, error)) 
	FilterFour_update = numpy.dot(FilterFour, error_filter(FilterFour, error))
	FilterFive_update = numpy.dot(FilterFive, error_filter(FilterFive, error))
	FilterSix_update = numpy.dot(FilterSix, error_filter(FilterSix, error))

	# updating the filter weights
	FilterOne += FilterOne_update
	FilterTwo += FilterTwo_update
	FilterThree += FilterThree_update
	FilterFour += FilterFour_update
	FilterFive += FilterFive_update
	FilterSix += FilterSix_update 

	tt = time.clock() - start

	# Results
	print("Prediction: \t\t| Error: \tfor Image: "+ans)
	print('-----------------------------------------------------------------')
	print('X: ' + str(numpy.absolute(output[0]*100)) + '%\t\t| ERR: ' + str(absErrX*100))
	print('O: ' + str(100 -numpy.absolute(output[1]*100)) + '%\t\t| ERR: ' + str(absErrO*100))
	print('Total Error: ' + error)
	print('Time Taken: ' + str(tt))
	print('-----------------------------------------------------------------')
