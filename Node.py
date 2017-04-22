# Basic node class with a left and right node reference and a integer value.
class Node:
	# Initialize for left, right, and integer values.
	def __init__(self):
		self.left = None
		self.right = None
		self.number = None
	# get integer value.
	def getValue(self):
		return self.number
	# get right node.
	def getRight(self):
		return self.right
	# get left node.
	def getLeft(self):
		return self.left