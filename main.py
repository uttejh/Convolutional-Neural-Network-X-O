# from __future__ import print_function
from PIL import Image
from numpy import array
from procedures import *
import numpy

# numpy.set_printoptions(threshold=numpy.nan)

# Takes image as input and coverts it into required input of pixels (either 1 or -1)
def ProcessImage():
	#B/W image , called as monogram not grayscale (i did not choose grayscale)
	image = Image.open("conv1.jpg")
	# Converts image into array of pixels
	arr = array(image)

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

p = Procedures()

# Creating 4 filters
FilterOne = p.InitFilter()
FilterTwo = p.InitFilter()
FilterThree = p.InitFilter()
FilterFour = p.InitFilter()

# input
input_data = ProcessImage()

