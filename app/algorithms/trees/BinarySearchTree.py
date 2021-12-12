class BinarySearchTree:
    
    def __init__(self, root):
        self.root = root
  
    def insert_recursion(self, node):
        if self.root is None:
            self.root = node
            return
        find_parent_node = self._insert_recursion_helper(self.root, node)
        
        if node.val < find_parent_node.val:
            find_parent_node.left = node
            return
        find_parent_node.right = node
  
    def _insert_recursion_helper(self, root, node):
        if root.val > node.val:
            if not root.left:
                return root
            return self._insert_recursion_helper(root.left, node)
        if not root.right:
            return root
        return self._insert_recursion_helper(root.right, node)
    def find_value_node_recursive(self, val):
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
            return self._find_value_helper(root.left, val)
        if val > root.val:
              return self._find_value_helper(root.right, val)
        return None if root.val is not val else root