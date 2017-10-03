from numpy import array
from PIL import Image
def im():
	image = Image.open("conv1.jpg")
	arr = array(image)
	# print(len(arr))
	return len(arr),arr[0]

z = im()
print(z[0])