# This file mainly implement the construction of a vocabulary tree with K-means clustering as cluster method

import pickle
import numpy
import pdb
from sklearn.cluster import KMeans
from pro2_1 import point

# the problem is each node stores the informatin belonging to its child. The centre info
# of each node should be the center of itself. c1->5 are like pointer to their child.
class treeNode(object):
	def __init__(self, center=None, data=None, c1=None, c2=None, c3=None, c4=None, c5=None):
		'''

		# :param data: it should be 4/5 centroids, it does not have to store all the data
		:param center: the coordinate of the cluster( a descriptor vector). No center for root node
		c1 -> 5: pointer to children
		'''
		self.data = data
		self.center = center
		self.c1 = c1
		self.c2 = c2
		self.c3 = c3
		self.c4 = c4
		self.c5 = c5


class Tree(object):
	'''
	a four-branch tree class
	'''


	def __init__(self, root=None, nodes=[]):
		'''
		This tree has 4 branches at each node
		:param root: the root node of this tree
		:param nodes: the nodes of the tree
		'''
		self.root = root
		self.nodes = nodes


	def addNode(self, data, k, depth, currentDepth=0):
		'''
		Add nodes at next layer
		:param data: data to be clustered
		:param k: the number of branches
		:param depth: the depth of the tree
		:param currentDepth: the round of current iteration

		:return:
		'''
		# the tree has not been completely constructed, so continue to add node
		if currentDepth < depth:


			# node = treeNode(data=data)

			if self.root is None:   # storing data is useless
				self.root = treeNode(center=1)  # just to identify root. Anything except None is fine.
				self.nodes.append(self.root)
				Tree(root=self.root, nodes=self.nodes).addNode(data=data, k=k, depth=depth)

			else:
				parent = self.nodes[0]

				child = [parent.c1, parent.c2, parent.c3, parent.c4, parent.c5]
				centroid, cluster = kmeans(data, k)
				for i in range(k):
					child[i] = treeNode(center=centroid[i], data=cluster[i])
					self.nodes.append(child[i])
				self.nodes.pop(0)
				currentTree = Tree(root=self.root, nodes=self.nodes)
				currentTree.addNode(data=self.nodes[0].data, k=k, depth=depth, currentDepth=currentDepth+1)


		else:
			return print('Construction complete')


def kmeans(data, k):
	'''

	:param data: the data to be classified into k clusters, in the form of class(descriptor, index)
	:param k: the number of clusters
	:return: a list of centroids, and a list of clusters with corresponding data
	'''

	# extract the descriptor vector from the point class
	desVector = numpy.ndarray(shape=(len(data), 128))
	for i in range(len(data)):
		desVector[i] = numpy.array(data[i].descriptor)
	# pdb.set_trace()
	classifier = KMeans(n_clusters=k).fit(desVector)  # the input of fit should be descriptors!
	centroids = classifier.cluster_centers_
	cluster = classifier.labels_

	# Use the index obtained by clustering desVector. The index in the pointList is the same with in the desVector
	childrenCluster = []
	for j in range(k):
		# singleCluster = numpy.ndarray(shape=(1, 128))
		singleCluster = []
		# j = True # substitute singleCluster[0]
		for i in range(len(data)):
			if cluster[i] == j:
				# if j:
				# 	singleCluster = data[i]
				# 	j = False
				# else:
				singleCluster.append(data[i])
		childrenCluster.append(singleCluster)

	return centroids, childrenCluster


if __name__ == '__main__':
	depth = [3, 5, 7]
	branch = [4, 5]
	# need to import class defined in other files
	tree = Tree()
	txtPath = 'F:\KTH\pro2\descriptorVector.pkl'
	with open(txtPath, 'rb') as data:
		pointList = pickle.load(data)
		tree.addNode(data=pointList, k=branch[0], depth=depth[0])

# pro2_tree.py
