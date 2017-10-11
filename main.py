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
	errr = []
	length = len(filt)
	# size = length*length

	for i in range(length):
		err = []
		for j in range(length):
			e = error*gradient(filt[i][j])
			err.append(e)
		errr.append(err)

	return errr  



# Takes image as input and coverts it into required input of pixels (either 1 or -1)
def ProcessImage(numb):
	im = './img3/'+str(numb)+'.jpg'
	#B/W image , called as monogram not grayscale (i did not choose grayscale)
	image = Image.open(im)
	# Converts image into array of pixels
	arr = array(image)
	# sizeimg = len(arr)
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
# numOfWeights = len(SecondPooling)


p = Procedures()

# Creating 2 filters for First Convolution layer
FilterOne = p.InitFilter()
FilterTwo = p.InitFilter()

# Creating 4 filters for Second Convolution layer 
# (No. of filters needs to increased inorder to focus on more complex features)
FilterThree = p.InitFilter()
FilterFour = p.InitFilter()
FilterFive = p.InitFilter()
FilterSix = p.InitFilter()

for iterat in range(87):
	# Calculates execution time
	start = time.clock()

	# input
	input_data = ProcessImage(iterat)
	# input_data = process[0]
	# imgsize = process[1]

	if (iterat%2) == 0:
		label = 1
		ans = 'O'
	else:
		label = 0
		ans = 'X'

	# First Iteration
	# Convloution
	FirstConv1 = p.convolution(input_data, FilterOne)
	FirstConv2 = p.convolution(input_data, FilterTwo)

	# ReLu
	FirstReLu1 = p.reLu(FirstConv1)
	FirstReLu2 = p.reLu(FirstConv2)

	# Pooling
	FirstPooling1 = p.pooling(FirstReLu1)
	FirstPooling2 = p.pooling(FirstReLu2)


	# Second Iteration
	# Convloution
	SecondConv11 = p.convolution(FirstPooling1, FilterThree)
	SecondConv12 = p.convolution(FirstPooling1, FilterFour)
	SecondConv13 = p.convolution(FirstPooling1, FilterFive)
	SecondConv14 = p.convolution(FirstPooling1, FilterSix)
	SecondConv21 = p.convolution(FirstPooling2, FilterThree)
	SecondConv22 = p.convolution(FirstPooling2, FilterFour)
	SecondConv23 = p.convolution(FirstPooling2, FilterFive)
	SecondConv24 = p.convolution(FirstPooling2, FilterSix)


	# ReLu
	SecondReLu11 = p.reLu(SecondConv11)
	SecondReLu12 = p.reLu(SecondConv12)
	SecondReLu13 = p.reLu(SecondConv13)
	SecondReLu14 = p.reLu(SecondConv14)
	SecondReLu21 = p.reLu(SecondConv21)
	SecondReLu22 = p.reLu(SecondConv22)
	SecondReLu23 = p.reLu(SecondConv23)
	SecondReLu24 = p.reLu(SecondConv24)

	# Pooling
	SecondPooling11 = p.pooling(SecondReLu11)
	SecondPooling12 = p.pooling(SecondReLu12)
	SecondPooling13 = p.pooling(SecondReLu13)
	SecondPooling14 = p.pooling(SecondReLu14)
	SecondPooling21 = p.pooling(SecondReLu21)
	SecondPooling22 = p.pooling(SecondReLu22)
	SecondPooling23 = p.pooling(SecondReLu23)
	SecondPooling24 = p.pooling(SecondReLu24)

	temp = numpy.concatenate((SecondPooling11, SecondPooling12, SecondPooling13, SecondPooling14, SecondPooling21, SecondPooling22, SecondPooling23, SecondPooling24))

	# Fully Connected Layer
	FC = temp.flatten()

	output = []

	if (iterat) == 0:
		numOfWeights = len(FC)

		fan_in = (num_inp_featuremaps*filter_height*filter_width)
		fan_out = (num_out_featuremaps*filter_height*filter_width)/pooling_size

		w_bound = numpy.sqrt(6./(fan_in+fan_out))
		
		# Weights creates a matrix of numOfWeights*2 size
		w_fc = numpy.random.uniform(-w_bound,w_bound,(numOfWeights,2))

		# Initialising weight update array
		deltaW_fc = numpy.zeros_like(w_fc)

		# print(w_fc)


	# Dot product b/w FullyConnected Layer and Weigths (1*n)(n*2) = (1*2)
	output = numpy.dot(FC,w_fc)

	# Error from X and O
	error_X = 0 - output[0]
	error_O = 1 - output[1]

	absErrX = numpy.absolute(error_X)
	absErrO = numpy.absolute(error_O)

	# Total Error
	error = ( absErrX + absErrO)

	deltaW_fc = numpy.dot(FC, error)
	dw = deltaW_fc*alpha
	dw = dw.reshape(dw.size,1)
	# updating the weight
	w_fc = w_fc - dw


	FilterOne_update = numpy.dot(FilterOne, error_filter(FilterOne, error)) 
	FilterTwo_update = numpy.dot(FilterTwo, error_filter(FilterTwo, error)) 
	FilterThree_update = numpy.dot(FilterThree, error_filter(FilterThree, error)) 
	FilterFour_update = numpy.dot(FilterFour, error_filter(FilterFour, error))
	FilterFive_update = numpy.dot(FilterFive, error_filter(FilterFive, error))
	FilterSix_update = numpy.dot(FilterSix, error_filter(FilterSix, error))

	# print(FilterOne_update)

	# updating the filter weights
	FilterOne -= FilterOne_update
	FilterTwo -= FilterTwo_update
	FilterThree -= FilterThree_update
	FilterFour-= FilterFour_update
	FilterFive -= FilterFive_update
	FilterSix -= FilterSix_update 

	tt = time.clock() - start

	# Results
	print("Prediction: \t\t| Error: \tfor Image: "+ans+ " img:"+str(iterat))
	print('-----------------------------------------------------------------')
	print('X: ' + str(numpy.absolute(output[0])) + '\t\t| ERR: ' + str(absErrX*100))
	# print('O: ' + str(100 -numpy.absolute(output[1]*100)) + '%\t\t| ERR: ' + str(absErrO*100))
	print('O: ' + str(numpy.absolute(output[1])) + '\t\t| ERR: ' + str(absErrO*100))
	print('Total Error: ' + str(error))
	print('Time Taken: ' + str(tt))
	print('-----------------------------------------------------------------')
