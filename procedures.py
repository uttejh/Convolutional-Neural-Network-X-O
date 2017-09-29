import numpy

class Procedures:
	def __init__(self):
		self.bla = []

	# @staticmethod
	# Adds a padding of 2 all around the matrix
	def padding(self, x):
		x = numpy.pad(x,(2,2), 'constant')
		return x

	# @staticmethod
	def convolution(self, x):
		convoluted_array = []
		z = self.padding(x)
		return z
		for img_patch in z:
			w = numpy.dot(z,newarr)
			v = (numpy.sum(w,axis=None))/numpy.prod(newarr.size)
			retuern v
	
	# Creates an array with random values of 1,-1 in a 3*3 matrix
	@staticmethod
	def InitFilter():
		newarr = []
		newarr = numpy.random.choice([1,-1],(3,3))
		return newarr

	@staticmethod
	def reLu(x):
		return x.clip(min=0)

	@staticmethod
	def pooling(x):
		stride = 2
		window_size=[2,2]
		for window_size in reLu(x):
			numpy.matrix.max()
			window_size + stride #dont think thats how its done..
			
