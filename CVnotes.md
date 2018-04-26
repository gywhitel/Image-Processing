# Image Processing

标签（空格分隔）： ComputerVision

---
# Image Features
**blob**
> a blob is a region of an image in which some properties are constant or approximately constant; all the points in a blob can be considered in some sense to be similar to each other. 

blob detection method:

- differential
- local extrema


**mapping**
![](https://upload.wikimedia.org/wikipedia/commons/thumb/b/bd/Injection_keine_Injektion_1.svg/330px-Injection_keine_Injektion_1.svg.png)
f maps x to y
## [SIFT(Scale Invariant Feature Transform)][1]
[1]:http://www.vlfeat.org/api/sift.html
**Steps:**    
### Scale-space exterma detection
Keypoints(giving information about the object in the image) -> edges of the object -> extrema points of the image

### Keypoint localization
### Orientation assignment
### Keypoint descriptor
---
# Skin 
## Nearest neighbor
## Data modeling(fitting)
### generative method(shape of clusters):
- histogram
- PCA
### Discriminative method(boundaries between clusters):
- perceptron
- neural network
### K-means cluster
## Probabilistic modeling(Bayesian classification)
posterior
$$ Posterior(P_{(class|observaition)}) = \frac{likelihood(measurement)\times prior(class)}{normalization-term(normalized to 1, after-division-by-prior)}$$
$$ P_{(Not skin|R)} < P_{(skin|R)} = \frac{skin pixel with color R}{skin pixel} $$
Doesn't work well in High D
### How to build Bayeisian model
- **Linera subspaces**(Machine Learning LEC11)

the variance along certain direction $v$ (eigenvector) which minimize the variance
$$ var(v) = \sum{((x - avg(x))* v)^2}$$

- **Principal Component Analysis(PCA)**
eigenvectors 

---
### Feature matching
The repeatability is the percentage of detected features that survive a viewpoint change or some other transformation or disturbance in going from IMAGEA to IMAGEB and is calculated only based on the frames overlap. 

[openCV decriptor matching][2]
[2]:https://docs.opencv.org/3.4.1/db/d39/classcv_1_1DescriptorMatcher.html#a378f35c9b1a5dfa4022839a45cdf0e89
radius match

# Classification
## K means clustering
cost function: expected error
### classical K means clustering
![](https://upload.wikimedia.org/wikipedia/commons/thumb/e/ea/K-means_convergence.gif/330px-K-means_convergence.gif)
### hierarchical clustering
choose a smaller K in each level, if data is organized in structure  
![raw data](https://upload.wikimedia.org/wikipedia/commons/thumb/b/b5/Clusters.svg/250px-Clusters.svg.png)  
**raw data**
![](https://upload.wikimedia.org/wikipedia/commons/thumb/a/ad/Hierarchical_clustering_simple_diagram.svg/418px-Hierarchical_clustering_simple_diagram.svg.png)
**hierarchical clustering**

## [K center clustering][3](greedy)
[3]:https://en.wikipedia.org/wiki/Metric_k-center
cost = the max distance between a point to its centroid in a cluster    

# Object recognition
## Approaches
### appearence-based
### feature-based
![](https://docs.opencv.org/2.4/_images/Feature_Description_BruteForce_Result.jpg)
## Bag of words
> The bag-of-words model is a simplifying representation used in natural language processing and information retrieval (IR). Also known as the vector space model[1]. In this model, a text (such as a sentence or a document) is represented as the bag (multiset) of its words, disregarding grammar and even word order but keeping multiplicity (frequency).

**Query image**
> The following picture shows an example of object representation, i.e. reference image in your collection (database), and a query image sent by an end-user for instance from your mobile app (to be searched).

**Image frame**
like `class image()` a type of data structure to organize image information
> This template creates a frame like those surrounding images. This template can be used to put two or more images into a frame together, or as a wrapper for more complicated templates like {{superimpose}}. 
${{Image frame|width=|content=|caption=|link=|align=|pos=}}$
