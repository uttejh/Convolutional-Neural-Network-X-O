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
		lenf = len(filt)
		z = self.padding(x)
		s = z.shape
		# size = len(z)
		endx = s[0] - 2
		endy = s[1] - 2
		# print(z.shape)
		# print(endx)
		for i in range(endx):
			conv = []
			for j in range(endy):
				c = 0.0
				con = 0
				for k in range(lenf):
					for l in range(lenf):
						a = 0
						# c += numpy.prod(z[i][j]*filt[k][l])
						a = z[i][j]*filt[k][l]
						# print(str(i) + " " + str(j))
						c = numpy.sum([c, a])
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
		newarr = numpy.random.choice([1.,-1.],(3,3))
		return newarr

	@staticmethod
	def reLu(x):
		# return x.clip(min=0)
		return  numpy.clip(x,0,float("inf"))

	@staticmethod
	def pooling(x):
		# size = len(x)
		s = x.shape
		endx = s[0] - 1
		endy = s[1] - 1
		# end = size-1
		# maxy = []
		pool=[]
		for i in range(endx):
			if (i%2) == 0:
				pooler = []
				for j in range(endy):
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
