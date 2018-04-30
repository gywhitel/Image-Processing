# from PIL import Image
import glob
import cv2
import re

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
path = 'F:/KTH/pro2/test/*.jpg'
for imgName in glob.glob(path):
	img = cv2.imread(imgName)
	# use regular expression to filter the object index
	idx = re.search(r'\d', re.split(r'\\', imgName)[1]).group()
	kp, des = sift.detectAndCompute(img, None)
	objects.append(object(descriptor=des, keypoint=kp, index=idx))

# if not such file, establish a new one
descriptor  = open('F:\KTH\pro2\descriptor.txt', 'w')
for i in range(len(objects)):
	descriptor.write(str([objects[i].descriptor, objects[i].index]))