from app.algorithms.trees.BinaryTreeUtils import find_first_half_leaf_node_recursively, find_first_leaf_node_recursively


class BalancedBinaryTree:
    def __init__(self, root=None):
        self.root = root

    def insert_to_half_leaf_node(self, node):
        half_leaf_node = find_first_half_leaf_node_recursively(self.root)
        if half_leaf_node is None:
            raise Exception('Could not find a half leaf node')
        if half_leaf_node.left is None:
            half_leaf_node.left = node
        else:
            half_leaf_node.right = node

    def insert_to_leaf_node(self, node):
        leaf_node = find_first_leaf_node_recursively(self.root)
        if leaf_node is None:
            raise Exception('Could not find a leaf node')
        leaf_node.left = node

    def find_node_recursively(self, node):
        return self._find_node_recursively_helper(self.root, node)

    def _find_node_recursively_helper(self, root, node):
        if root is None:
            return None
        if root is node:
            return root
        left = self._find_node_recursively_helper(root.left, node)
        right = self._find_node_recursively_helper(root.right, node)
        if left == node:
            return left
        if right == node:
            return right
        return None
