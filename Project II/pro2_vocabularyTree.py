# This file mainly implement the construction of a vocabulary tree with K-means clustering as cluster method

from sklearn.cluster import KMeans


class treeNode(object):
	def __init__(self, data=None, center=None, c1=None, c2=None, c3=None, c4=None, c5=None):
		'''

		:param data: it should be 4/5 centroids
		c1 -> 5: the centroids of 4/5 children clusters
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


	def __init__(self, root, nodes):
		'''
		This tree has 4 branches at each node
		:param root: the root node of this tree
		:param nodes: the nodes of the tree
		'''
		self.root = treeNode()
		self.nodes = []


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

			node = treeNode(data=data)

			if self.root is None:
				self.root = node
				self.nodes.append(self.root)
			else:
				parent = self.nodes[0]
				# 4-branch tree construction
				if k == 4:
					child = [parent.c1, parent.c2, parent.c3, parent.c4]
					centroid, cluster = kmeans(data, 4)
					for i in range(k):
						child[i] = treeNode(cluster[i], center=centroid[i])
						self.nodes.append(child[i])
					self.nodes.pop(0)

				# 5-branch tree construction
				if k == 5:
					child = [parent.c1, parent.c2, parent.c3, parent.c4, parent.c5]
					centroid, cluster = kmeans(data, 5)
					for i in range(k):
						child[i] = treeNode(cluster[i], center=centroid[i])
						self.nodes.append(child[i])
					self.nodes.pop(0)

				else:
					print('this algorithm only support the scenario that the tree has 4 or 5 branches')

			# Next layer,  currentDepth = currentDepth + 1
			# recursively call

			for i in range(k):
				Tree.addNode(data=child[i], k=k, depth=depth, currentDepth=currentDepth+1)



def kmeans(data, k):
	'''

	:param data: the data to be classified into k clusters
	:param k: the number of clusters
	:return: a list of centroids, and a list of clusters with corresponding data
	'''
	classifier = KMeans(n_clusters=k).fit(data)
	centroids = classifier.cluster_centers_
	cluster = classifier.labels_

	childrenCluster = []
	for j in k:
		singleCluster = []
		for i in range(len(data)):
			if cluster[i] == k:
				singleCluster.append(data[i])
		childrenCluster.append(singleCluster)

	return centroids, childrenCluster


if __name__ == '__main__':
	depth = [3, 5, 7]
