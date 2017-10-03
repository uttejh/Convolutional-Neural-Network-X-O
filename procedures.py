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
	def convolution(self, x , filt):
		convoluted_array = []
		s = len(filt)
		z = self.padding(x)
		size = len(z)
		end = size-2
		for i in range(end):
			conv = []
			for j in range(end):
				c = 0.0
				con = 0
				for k in range(s):
					for l in range(s):
						# c += numpy.prod(z[i][j]*filt[k][l])
						c = numpy.sum([c, numpy.prod(z[i][j]*filt[k][l])])
				con = float(c)/9
				conv.append(con)
			convoluted_array.append(conv)
		# for i in range(end):
		# 	for j in range(s):
		# 		c+= 
		return convoluted_array


	# Creates an array with random values of 1,-1 in a 3*3 matrix
	@staticmethod
	def InitFilter():
		newarr = []
		newarr = numpy.random.choice([1,-1],(3,3))
		return newarr

	@staticmethod
	def reLu(x):
		# return x.clip(min=0)
		return  numpy.clip(x,0,float("inf"))

	@staticmethod
	def pooling(x):
		size = len(x)
		end = size-1
		# maxy = []
		pool=[]
		for i in range(end):
			pooler = []
			if (i%2) == 0:
				for j in range(end):
					if (j%2) == 0:
						m = 0 
						m = max(x[i][j],x[i][j+1],x[i+1][j+1],x[i+1][j+1])
						# k = int(i)/2
						# pool[k].append(m)
						pooler.append(m)
					else:
						pass
			else:
				pass
			pool.append(pooler)
		return pool
