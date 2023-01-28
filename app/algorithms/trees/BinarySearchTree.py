from app.data_structures.tree import BinaryNode


class BinarySearchTree:

    def __init__(self):
        self.root = None

    def insert_recursion(self, val):
        if not self.root:
            self.root = BinaryNode(val)
        else:
            self.root = self._insert_recursion_helper(self.root, val)

    def insert_all_recursion(self, lst):
        for i in lst or []:
            self.root = self._insert_recursion_helper(self.root, i)
  
    def _insert_recursion_helper(self, root, val):
        if root is None:
            return BinaryNode(val)
        if root.val == val:
            raise Exception("Value already exists in binary search tree")
        if val < root.val:
            root.left = self._insert_recursion_helper(root.left, val)
        else:
            root.right = self._insert_recursion_helper(root.right, val)
        return root

    def find_value_node_recursive(self, val):
        if self.root is None:
            raise Exception("No value exists in binary search tree")
        result = self._find_value_helper(self.root, val)
        if result is None:
            raise Exception("Could not find value in binary search tree")
        return result

    def _find_value_helper(self, root, val):
        if root is None:
            return None
        if root.val == val:
            return root
        if val < root.val:
            return self._find_value_helper(root.left if val < root.val else root.right, val)
        elif val > root.val:
            return self._find_value_helper(root.right, val)
        return None if root.val is not val else root
