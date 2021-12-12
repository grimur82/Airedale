import unittest

from app.algorithms.trees import BinarySearchTree
from app.data_structures.tree import BinaryNode

class TestBinarySearchTree(unittest.TestCase):

    def test_find_value_node_success(self):
        binary_search_tree = BinarySearchTree(BinaryNode(5))
        binary_search_tree.insert_recursion(BinaryNode(2))
        binary_search_tree.insert_recursion(BinaryNode(6))
        expected_node = BinaryNode(20)
        binary_search_tree.insert_recursion(expected_node)
        
        result = binary_search_tree.find_value_node_recursive(20)
        self.assertEqual(result, expected_node)
        
    def test_find_value_node_fail(self):
        binary_search_tree = BinarySearchTree(BinaryNode(5))
        binary_search_tree.insert_recursion(BinaryNode(2))
        binary_search_tree.insert_recursion(BinaryNode(6))
        binary_search_tree.insert_recursion(BinaryNode(20))
        with self.assertRaises(Exception):
            binary_search_tree.find_value_node_recursive(3)

if __name__ == '__main__':
    unittest.main()