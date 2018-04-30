# Image Processing Project

标签（空格分隔）： python ComputerVision 

---

## Wrong window size showing images
```python
c = cv2.imread('ketil.jpg')
height, width = c.shape[:2]
cv2.namedWindow('jpg', cv2.WINDOW_NORMAL)
cv2.resizeWindow('jpg', width, height)
cv2.imshow('jpg', c)
r = cv2.waitKey(0)
```

## matplot.imshow show pictures in wrong color

OpenCV uses BGR as its default colour order for images, matplotlib uses RGB. When you display an image loaded with OpenCv in matplotlib the channels will be back to front.

The easiest way of fixing this is to use OpenCV to explicitly convert it back to RGB, much like you do when creating the greyscale image.

`RGB_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)`

And then use that in your plot.

## PROBLEMS: cannot find current directory after moving files
edit configuration, reset script path to current project


## [openCV 2D framework][1]
## numpy.array
```python
>>> c.shape
(2,)
>>> c = np.array([[1,2]])
>>> c.shape
(1, 2)
```

## rotating image
![rotated image](https://raw.githubusercontent.com/gywhitel/Image-Processing/master/Photos/image.png)

Images would be cropped (losing pixels) after rotation and the centroid would translate.

- resize(expand) the canvas
- translation compensation
```
def rotation(img, degree):
	'''

	:param img: source image
	:param degree:rotation degree
	:return: the rotated image; a 2x2 rotation matrix; new Centre after rotation

	'''
	height, width = img.shape[:2]
	oriCentre = numpy.array([width/2, height/2]).reshape(2,1)
	##size = [height, width]
	roM = cv2.getRotationMatrix2D((width / 2, height / 2), degree, 1)
	sin = abs(roM[1][0])
	cos = abs(roM[0][0])
	newHeight = int(width * sin + height * cos)
	newWidth = int(width * cos + height * sin)
	newSize = (newWidth, newHeight)
	newCentre = numpy.array([newWidth / 2, newHeight / 2]).reshape(2, 1)
	# translation compensate instead of equal
	roM[0][2] = roM[0][2] + (newWidth - width) / 2
	roM[1][2] = roM[1][2] + (newHeight - height) / 2
	roImg = cv2.warpAffine(img, roM, dsize=newSize)
	rotM = numpy.array([[roM[0][0], roM[0][1]], [roM[1][0], roM[1][1]]])

	return roImg, rotM, oriCentre, newCentre
```

## insufficient memory
use a smaller size image and it works.
Seems something wrong with the allocate cpp file, but cannot find the directory.

## Function package
if you want to call some functions in other python file, just build function in that file. DO NOT include executable codes in the same file. Otherwise, it would execuate those codes.

  [1]: https://docs.opencv.org/3.4.1/da/d9b/group__features2d.html
  [2]: Image-Processing/Photos/image.png
  
# Project 2 Image retrieval

find I can install packages in Ubuntu, just like in Windows
`pip install packageName`
NO need to use`sudo`, which is not authorised

## Extracting features(descriptors)
- use`glob.glob` from `glob` package to traverse all the images in a folder. Just use `cv2.imread()`  for reading images, do not use PIL function.
- Use `os.path.dirname(os.path.abspath(__file__))` to obtain the full name of current directory, otherwise python cannot find the correct directory `'/afs/kth.se/home/y/i/yinghao/Documents/python/imageProcess/pro2/Data2/server/*.JPG'`.
It would be without`/afs/kth.se`
- The format `jpg` should be capital!
- Python 2 and 3 coexist, the openCV is automatically installed under python 2. Python 3 cannot import openCV. The difference between 2 and 3 is avoidable, so I use python 2 to write python-3-style code.
[The difference between python 2 and 3][3]

[3]: https://docs.python.org/3/whatsnew/3.0.html
### Regular expression
Use regular expression to extract the index of the object. But it's not necessary now, since I use depth to represent the index
```python

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
```
### The biggest problem is how to organize the data structure
We have 50 objects and 3 images for each object. We need to store the descriptor(2D $226\times 128$ Matrix) for each image. And we also need to label or index each object.
After try a few structures, I built a $50 \times 3 $Lists for the data storage.
- I've tried to use a $50\times 3$ numpy.array, but the elements cannot be a matrix. That's why I use a list.
- In this case, the depth (row number) is identical to the index, so I don't have to label them.
- It's a little tricky to think of the index of the list [int(division)][remainder]
```python
rows, columns = 50, 3
descriptors = [[0 for i in range(columns)] for j in range(rows)]
index = 1
for i in range(len(objects)):
	# index = objects[i].index
	descriptors[i // 3][i % 3] = objects[i].descriptor

```
  
  
  
  
