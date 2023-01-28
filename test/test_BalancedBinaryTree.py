import unittest

from app.data_structures.tree import BinaryNode
from app.algorithms.trees import BalancedBinaryTree

class TestBalancedBinaryTree(unittest.TestCase):

    def test_balanced_tree_find_node_recursivly_success(self):
        
        expected_node = BinaryNode(5)
        balanced_tree = BalancedBinaryTree(BinaryNode(2))
        balanced_tree.insert_to_leaf_node(expected_node)
        
        actual_node = balanced_tree.find_node_recursively(expected_node)
        
        self.assertEqual(actual_node, expected_node)
        
    def test_balanced_tree_find_node_recursivly_not_found(self):
        
        balanced_tree = BalancedBinaryTree(BinaryNode(2))
        insert_node = BinaryNode(5)
        balanced_tree.insert_to_leaf_node(insert_node)
        
        actual_node = balanced_tree.find_node_recursively(BinaryNode((4)))
        
        self.assertEqual(actual_node, None)

if __name__ == '__main__':
    unittest.main()