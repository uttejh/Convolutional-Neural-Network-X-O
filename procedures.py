import numpy

class Procedures:
	def __init__(self):
		self.bla = []

	# @staticmethod
	def padding(self, x):
		return x

	# @staticmethod
	def convolution(self, x):
		convoluted_array = []
		self.padding(x)
	
	# Creates an array with random values of 1,-1 in a 3*3 matrix
	@staticmethod
	def InitFilter():
		newarr = []
		newarr = numpy.random.choice([1,-1],(3,3))
		return newarr


