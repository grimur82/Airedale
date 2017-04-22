from Node import Node 
# BinarySearchTree.
class BinarySearchTree:
	# initialize a source node.
	def __init__(self,newNode):
		self.source = newNode
	# Insert a new value to BinarySearchTree.
	def insert(self,data):
		current = self.source
		if(current.number is None):
			current.number = data
		else:
			self.insertHelper(current,data)
	# Traverse tree to find correct position for a new node.
	def insertHelper(self,getNode,data):
		if(getNode.number < data):
			if(getNode.left != None):
				self.insertHelper(getNode.left,data)
			else:
				getNode.left = Node()
				getNode.left.number = data
		if(getNode.number > data):
			if(getNode.right != None):
				self.insertHelper(getNode.right,data)
			else:
				getNode.right = Node()
				getNode.right.number = data
		return 
	# Get source node.
	def getNode(self):
		return self.source
	def findValue(self,node,num):
		# If node is a leaf stop.
		if(node == None):
			return 
		if(node.number == num):
			print("Found it")
			return
		if(node.number < num):
			self.findValue(node.left,num)
		else:
			self.findValue(node.right,num)
	# Recrusion to find height of tree.
	def height(self,tree):
		left = None;
		right = None;
		# Stop traversal of tree when a leaf is reached.
		if(tree is None):
			return 0;
		else:
			# check left or right node. Add one for height
			left =  self.height(tree.left) + 1;
			right = self.height(tree.right) + 1;
		# If left node's height is greater than right. return left.
		if(left >= right):
			return left
		# return right if height is greater than left.
		else:
			return right
	# Output left, parent, right nodes
	def inOrder(self,tree):
		if(tree is None):
			return
		else:
			self.inOrder(tree.left)
			print(tree.number);
			self.inOrder(tree.right)
	# Output parent nodes, left, right
	def preOrder(self,tree):
		if(tree is None):
			return
		else:
			print(tree.number);
			self.inOrder(tree.left)
			self.inOrder(tree.right)
	# Output left, right, parent nodes
	def postOrder(self,tree):
		if(tree is None):
			return
		else:
			self.inOrder(tree.left)
			self.inOrder(tree.right)
			print(tree.number);