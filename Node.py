# Basic node class with a left and right node reference and a integer value.
class Node:
	# Initialize for left, right, and integer values.
	def __init__(self):
		self.left = None
		self.right = None
		self.number = None
		self.parent = None
		self.height = 0
	def setHeight(self, height):
		self.height = height;
	def getHeight(self):
		return self.height;
	def setParent(self, node):
		self.parent = node;
	def getParent(self):
		return self.parent;
