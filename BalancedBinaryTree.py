from Node import Node 
import TreeServices
# Basic BinaryTree written in python.
class BalancedBinaryTree:
	# initialize a source node.
	def __init__(self):
		self.source = None
		self.lst = [];
		self.depth = 0;
	# Set max depth in tree.
	def setDepth(self,num):
		if(num > self.depth):
			self.depth = num;
	# Get depth of tree.
	def getDepth(self):
		return self.depth;
	# insert a new value into tree.
	def insert(self,num):
		if(self.source is None):
			self.source = Node();
			self.source.number = num;
			self.lst.append(self.source);
		elif(self.source.left is None):
			self.source.left = Node();
			TreeServices.setParent(self.source,self.source.left);
			TreeServices.setNumber(self.source.left,num);
			TreeServices.setHeight(self.source.left);
			self.setDepth(TreeServices.getHeight(self.source.left));
			self.lst.append(self.source.left);
		elif(self.source.right is None):
			self.source.right = Node();
			TreeServices.setParent(self.source,self.source.right);
			TreeServices.setNumber(self.source.right,num);
			TreeServices.setHeight(self.source.right);
			self.setDepth(TreeServices.getHeight(self.source.right));
			self.lst.append(self.source.right);
		else:
			while(True):
				temp = self.lst[0];
				if(temp.left is None):
					temp.left = Node();
					temp.left.number = num;
					TreeServices.setParent(temp,temp.left);
					TreeServices.setHeight(temp.left);
					self.setDepth(temp.left.getHeight());
					self.lst.append(temp.left);
					break;
				elif(temp.right is None):
					temp.right = Node();
					temp.right.number = num;
					TreeServices.setParent(temp,temp.right);
					TreeServices.setHeight(temp.right);
					self.setDepth(temp.right.getHeight());
					self.lst.append(temp.right);
					break;
				else:
					self.lst.remove(temp);
	# Get tree.
	def getNode(self):
		return self.source