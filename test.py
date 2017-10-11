from __future__ import print_function
# from PIL import Image
from numpy import array
from procedures import *
import numpy
import time
from PIL import Image
from resizeimage import resizeimage
# for i in range(88):
# 	name ='./img2/'+str(i+101)+'.jpg'
# 	j = i 
# 	name2 = './img3/'+str(j)+'.jpg'
# 	fd_img = open(name, 'r')
# 	img = Image.open(fd_img)
# 	img = resizeimage.resize_contain(img, [28, 28])
# 	img = img.convert('1')
# 	img.save(name2, 'JPEG')
# 	# rgb_im = im.convert('RGB')
# 	# rgb_im.save('colors.jpg')
# 	# print(img.format)
# 	fd_img.close()
im = './img3/0.jpg'
image = Image.open(im)
	# Converts image into array of pixels
arr = array(image)
numpy.set_printoptions(threshold=numpy.nan)
print(arr)

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
print('--------------------------------------------------------------')
print(len(arr))
print(len(data[0]))
print(data)