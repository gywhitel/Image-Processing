# from PIL import Image
import glob
import cv2
import re
# import pickle
import numpy

from matplotlib import pyplot as plt


class visualWord(object):
	'data structure for each object(building)'

	def __init__(self, descriptor, keypoint, index, name):
		self.descriptor = descriptor
		self.keypoint = keypoint
		self.index = index
		self.name = name


# Tree construction


	
sift = cv2.xfeatures2d.SIFT_create(contrastThreshold=0.16, edgeThreshold=9)

# store data in an object-class list
objects = []
imgPath = 'F:/KTH/pro2/server/*.jpg'
for imgName in glob.glob(imgPath):
	img = cv2.imread(imgName)

	# use regular expression to filter the object index
	# no extra space in regular expression
	idx = re.search(r'\d{1,2}', re.split(r'\\', imgName)[1]).group()
	kp, des = sift.detectAndCompute(img, None)
	objects.append(visualWord(descriptor=des, keypoint=kp, index=str(idx).zfill(2), name=imgName))

# 	sort the lists in the order of index
objects = sorted(objects, key=lambda visualWord: visualWord.index)

# select the descriptors for the same object into single list, the index of the list = the index of the object - 1
descriptors = []
sameObject = []
index = 1
for i in range(len(objects)):
	if objects[i].index == index:
		sameObject.append(objects[i].descriptor)
	else:
		# when turn to a new object, store the descriptors for the last object in a list
		descriptors.append([sameObject])
		sameObject = []
		sameObject.append(objects[i].descriptor)
	index = objects[i].index



# if no such file, establish a new one
txtPath = 'F:\KTH\pro2\descriptor'
descriptor = open(txtPath, 'w')
# for i in range(len(objects)):
	# pickle.dump([objects[i].descriptor, objects[i].index], descriptor)
numpy.save(txtPath, descriptors, allow_pickle=True)



'''
txtPath = 'F:\KTH\pro2\descriptor.npy'
data = numpy.load(txtPath)
print(data[0])
'''
