import numpy as np

x = np.ones((3,3))
it = np.nditer(x, flags=['multi_index'], op_flags=['readwrite'])

while not it.finished:
	q = it.multi_index
	print(q)
	print(x[q])
	it.iternext()