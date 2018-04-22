import cv2
# import pdb
from matplotlib import pyplot as plt
from pro1_b import square_match as sqmatch

def scale(img, scaleFactor):
	height, width = img.shape[:2]
	newHeight = int(scaleFactor * height)
	newWidth = int(scaleFactor * width)
	newSize = (newWidth, newHeight)
	return cv2.resize(img, dsize=newSize, fx=scaleFactor, fy=scaleFactor)

def scaleRobust(kp, scaleKp, scaleFactor):
	'''

	:param kp: the keypoints of original images
	:param scaleKp: the keypoints of scaled images
	:param scaleFactor:
	:return: the number of matched features / all features
	'''
	match = 0
	idealKp = scaleFactor * kp.pt
	for i in range(len(kp)):
		for j in range(len(scaleKp)):
			match = match + sqmatch(idealKp[i], scaleKp[j].pt)
	return match / len(kp)


# If use the original image, it would fail due to insufficient memory,
# use a smaller size source image and it works.




img = cv2.imread('kth.jpg', cv2.IMREAD_COLOR)
contrastT = 0.05
edgeT = 9
## create a SIFT(class)
sift = cv2.xfeatures2d.SIFT_create(contrastThreshold=contrastT, edgeThreshold=edgeT)
# kp, des = sift.detectAndCompute(img, None)
kp = sift.detect(img, None)
# sqrt(scaling factors)
scalfact = [1.2 ^ power/2 for power in range(9)]

repeatability = []
for scaleFactor in scalfact:
	scaleImg = scale(img, scaleFactor)
	scaleKp = sift.detect(scaleImg, None)
	repeatability.append(scaleRobust(kp, scaleKp, scaleFactor))

plt.plot(scalfact, repeatability)
plt.title('the robustness of SIFT against scaling')
plt.show()
