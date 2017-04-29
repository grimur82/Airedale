# Set parent from a given node.
def setParent(p,child):
	child.parent = p;
# Get parents height an increment by one to set height for node.
def setHeight(node):
	node.setHeight(node.getParent().getHeight()+1);
# Get height of current node.
def getHeight(node):
	return node.getHeight();
# Set number in node.
def setNumber(node,num):
	node.number = num;
# Find the lowest common ancestor of two given values.
def lowestCommonAncestor(node,num,num2):
	lst = [];
	lst.append(node);
	fNode = None;
	lNode = None;
	while(len(lst) >0):
		temp = lst[0];
		if(temp.number == num):
			fNode = temp;
		if(temp.number == num2):
			lNode = temp;
		if(temp.left is not None):
			temp.left.parent = temp;
			lst.append(temp.left);
		if(temp.right is not None):
			temp.right.parent = temp;
			lst.append(temp.right);
		lst.remove(temp);
	while(fNode is not None and lNode is not None):
		if(fNode.getParent() is not None and fNode.getParent().number == lNode.number):
			print("Common Ancestor: " + str(lNode.number));
			break;
		if(lNode.getParent() is not None and lNode.getParent().number == fNode.number):
			print("Common Ancestor: " + str(fNode.number));
			break;			
		if(fNode.number == lNode.number):
			print("Common Ancestor: " + str(fNode.number));
			break;
		if(fNode.getParent() is not None):
			fNode = fNode.getParent();
		if(lNode.getParent() is not None):
			lNode = lNode.getParent();
# Post Tree output.
def postOrderTraverse(node):
		if(node is None):
			return None
		else:
			postOrderTraverse(node.left);
			postOrderTraverse(node.right);
			print(node.number);
# Pre Tree output.
def preOrderTraverse(node):
		if(node is None):
			return None
		else:
			print(node.number);
			preOrderTraverse(node.left);
			preOrderTraverse(node.right);
# Inverse Tree output.
def innOrderTraverse(node):
		if(node is None):
			return None
		else:
			if(node is not None):
				if(node.left is not None):
					node.left.parent = node;
				if(node.right is not None):
					node.right.parent = node;
			innOrderTraverse(node.left);
			print(node.number);
			innOrderTraverse(node.right);
# Bread First Search output of the tree.
def BFS(node):
	BFSlst = [];
	BFSlst.append(node);
	while(len(BFSlst) != 0):
		temp = BFSlst[0];
		BFSlst.remove(temp);
		print(temp.number);
		if(temp.left is not None):
			BFSlst.append(temp.left);
		if(temp.right is not None):
			BFSlst.append(temp.right);