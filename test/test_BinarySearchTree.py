import unittest

from app.algorithms.trees.BinarySearchTree import BinarySearchTree
from app.data_structures.tree import BinaryNode


class TestBinarySearchTree(unittest.TestCase):

    def test_find_value_node_success(self):
        binary_search_tree = BinarySearchTree()
        binary_search_tree.insert_all_recursion([5, 2, 6])
        expected_value = 20
        binary_search_tree.insert_recursion(expected_value)
        
        result = binary_search_tree.find_value_node_recursive(20)
        self.assertEqual(result.val, expected_value)
        
    def test_find_value_node_fail(self):
        binary_search_tree = BinarySearchTree()
        binary_search_tree.insert_all_recursion([2, 6, 20])
        with self.assertRaises(Exception):
            binary_search_tree.find_value_node_recursive(3)

    def test_insert_value_duplicate_fail(self):
        binary_search_tree = BinarySearchTree()
        binary_search_tree.insert_all_recursion([2, 6, 20])
        with self.assertRaises(Exception):
            binary_search_tree.insert_recursion(2)


if __name__ == '__main__':
    unittest.main()
