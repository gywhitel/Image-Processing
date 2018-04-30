# from PIL import Image
import glob
import cv2
import re
# import pickle
import numpy

from matplotlib import pyplot as plt


class object:
	'data structure for each object(building)'

	def __init__(self, descriptor, keypoint, index):
		self.descriptor = descriptor
		self.keypoint = keypoint
		self.index = index
	
sift = cv2.xfeatures2d.SIFT_create(contrastThreshold=0.16, edgeThreshold=9)

# store data in an object-class list
objects = []
imgPath = 'F:/KTH/pro2/server/*.jpg'
for imgName in glob.glob(imgPath):
	img = cv2.imread(imgName)
	# use regular expression to filter the object index
	idx = re.search(r'\d+', re.split(r'\\', imgName)[1]).group()
	kp, des = sift.detectAndCompute(img, None)
	objects.append(object(descriptor=des, keypoint=kp, index=idx))

# ------------------building data structure------------------
# 50(row = index) x 3( 3 images for each object) list, each element is a descriptor matrix,
# establish a 4D matrix [
# [[obj1_1],[obj1_2],[obj1_3]],
# [[obj2_123],[],[]]
# ], whose depth is identical to the index

rows, columns = 50, 3
descriptors =  [[0 for i in range(columns)] for j in range(rows)]
index = 1
for i in range(len(objects)):
	# index = objects[i].index
	descriptors[i//3][i%3] = objects[i].descriptor

	# if objects[i].index == index:
	# 	sameObject.append(objects[i].descriptor)
	# else:
	# 	sameObject = []
	# 	sameObject.append(objects[i].descriptor)



# if no such file, establish a new one
txtPath = 'F:\KTH\pro2\descriptor'
descriptor = open(txtPath, 'a')
# for i in range(len(objects)):
	# pickle.dump([objects[i].descriptor, objects[i].index], descriptor)
numpy.save(txtPath, descriptors, allow_pickle=True)


'''test

txtPath = 'F:\KTH\pro2\descriptor.npy'
data = numpy.load(txtPath)
print(data)
'''
