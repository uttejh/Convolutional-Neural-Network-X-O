# from __future__ import print_function
from PIL import Image
from numpy import array
import numpy

# numpy.set_printoptions(threshold=numpy.nan)

#B/W image , called as monogram not grayscale (grayscale consists of noice)
image = Image.open("img/conv1.jpg")
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
		# temp.append(y)
		if y == 0:
			temp.append(1)
		elif y == 1:
			temp.append(-1)
	data.append(temp)

# print(data)