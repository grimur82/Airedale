import unittest

from app.data_structures.tree import BinaryNode
from app.algorithms.trees.BinaryTreeUtils import calculate_node_depth, calculate_node_height, \
    is_balanced_binary_tree_recursive, lowest_common_ancestor_iterative, lowest_common_ancestor_recursive, \
    post_order_traverse, pre_order_traverse


class TestBinaryTreeServices(unittest.TestCase):

    def test_lowest_common_ancestor_iterative_node_found_on_left(self):
        new_node = BinaryNode('A')
        new_node.left = BinaryNode('B')
        new_node.right = BinaryNode('C')
        new_node.left.left = BinaryNode('D')
        new_node.left.right = BinaryNode('E')
        new_node.right.left = BinaryNode('F')
        new_node.right.right = BinaryNode('G')
        self.assertEqual(vars(lowest_common_ancestor_iterative(new_node, new_node.left.left, new_node.left.right)),
                         vars(new_node.left))

    def test_lowest_common_ancestor_iterative_node_found_on_right(self):
        new_node = BinaryNode('A')
        new_node.left = BinaryNode('B')
        new_node.right = BinaryNode('C')
        new_node.left.left = BinaryNode('D')
        new_node.left.right = BinaryNode('E')
        new_node.right.left = BinaryNode('F')
        new_node.right.right = BinaryNode('G')
        self.assertEqual(vars(lowest_common_ancestor_iterative(new_node, new_node.right.left, new_node.right.left)),
                         vars(new_node.right.left))

    def test_lowest_common_ancestor_iterative_node_found_on_a_node_itself(self):
        new_node = BinaryNode('A')
        new_node.left = BinaryNode('B')
        new_node.right = BinaryNode('C')
        new_node.left.left = BinaryNode('D')
        new_node.left.right = BinaryNode('E')
        new_node.right.left = BinaryNode('F')
        new_node.right.right = BinaryNode('G')
        self.assertEqual(vars(lowest_common_ancestor_iterative(new_node, new_node.right.left, new_node.right)),
                         vars(new_node.right))

    def test_lowest_common_ancestor_iterative_node_found_on_root(self):
        new_node = BinaryNode('A')
        new_node.left = BinaryNode('B')
        new_node.right = BinaryNode('C')
        new_node.left.left = BinaryNode('D')
        new_node.left.right = BinaryNode('E')
        new_node.right.left = BinaryNode('F')
        new_node.right.right = BinaryNode('G')
        self.assertEqual(vars(lowest_common_ancestor_iterative(new_node, new_node.left.left, new_node.right.left)),
                         vars(new_node))

    def test_lowest_common_ancestor_iterative_node_failed_not_found(self):
        new_node = BinaryNode('A')
        new_node.left = BinaryNode('B')
        new_node.right = BinaryNode('C')
        new_node.left.left = BinaryNode('D')
        new_node.left.right = BinaryNode('E')
        new_node.right.left = BinaryNode('F')
        new_node.right.right = BinaryNode('G')
        with self.assertRaises(Exception):
            lowest_common_ancestor_iterative(new_node, new_node.left.left, BinaryNode('X'))

    def test_lowest_common_ancestor_recursivly_node_found_on_left(self):
        new_node = BinaryNode('A')
        new_node.left = BinaryNode('B')
        new_node.right = BinaryNode('C')
        new_node.left.left = BinaryNode('D')
        new_node.left.right = BinaryNode('E')
        new_node.right.left = BinaryNode('F')
        new_node.right.right = BinaryNode('G')
        self.assertEqual(vars(lowest_common_ancestor_recursive(new_node, new_node.left.left, new_node.left.right)),
                         vars(new_node.left))

    def test_lowest_common_ancestor_recursivly_node_found_on_right(self):
        new_node = BinaryNode('A')
        new_node.left = BinaryNode('B')
        new_node.right = BinaryNode('C')
        new_node.left.left = BinaryNode('D')
        new_node.left.right = BinaryNode('E')
        new_node.right.left = BinaryNode('F')
        new_node.right.right = BinaryNode('G')
        self.assertEqual(vars(lowest_common_ancestor_recursive(new_node, new_node.right.left, new_node.right.left)),
                         vars(new_node.right.left))

    def test_lowest_common_ancestor_recursivly_node_found_on_a_node_itself(self):
        new_node = BinaryNode('A')
        new_node.left = BinaryNode('B')
        new_node.right = BinaryNode('C')
        new_node.left.left = BinaryNode('D')
        new_node.left.right = BinaryNode('E')
        new_node.right.left = BinaryNode('F')
        new_node.right.right = BinaryNode('G')
        self.assertEqual(vars(lowest_common_ancestor_recursive(new_node, new_node.right.left, new_node.right)),
                         vars(new_node.right))

    def test_lowest_common_ancestor_recursivly_node_found_on_root(self):
        new_node = BinaryNode('A')
        new_node.left = BinaryNode('B')
        new_node.right = BinaryNode('C')
        new_node.left.left = BinaryNode('D')
        new_node.left.right = BinaryNode('E')
        new_node.right.left = BinaryNode('F')
        new_node.right.right = BinaryNode('G')
        self.assertEqual(vars(lowest_common_ancestor_recursive(new_node, new_node.left.left, new_node.right.left)),
                         vars(new_node))

    def test_lowest_common_ancestor_recursivly_node_failed_not_found(self):
        new_node = BinaryNode('A')
        new_node.left = BinaryNode('B')
        new_node.right = BinaryNode('C')
        new_node.left.left = BinaryNode('D')
        new_node.left.right = BinaryNode('E')
        new_node.right.left = BinaryNode('F')
        new_node.right.right = BinaryNode('G')
        with self.assertRaises(Exception):
            lowest_common_ancestor_recursive(new_node, new_node.left.left, BinaryNode('X'))

    def test_post_order_traverse(self):
        new_node = BinaryNode('A')
        new_node.left = BinaryNode('B')
        new_node.right = BinaryNode('C')
        new_node.left.left = BinaryNode('D')
        new_node.left.right = BinaryNode('E')
        new_node.right.left = BinaryNode('F')
        new_node.right.right = BinaryNode('G')
        self.assertEqual(post_order_traverse(new_node), ['D', 'E', 'B', 'F', 'G', 'C', 'A'])

    def test_pre_order_traverse(self):
        new_node = BinaryNode(7)
        new_node.left = BinaryNode(4)
        new_node.right = BinaryNode(8)
        new_node.left.left = BinaryNode(2)
        new_node.left.right = BinaryNode(5)
        self.assertEqual(pre_order_traverse(new_node), [7, 4, 2, 5, 8])

    def test_height(self):
        new_node = BinaryNode(7)
        new_node.left = BinaryNode(4)
        new_node.right = BinaryNode(8)
        new_node.left.left = BinaryNode(2)
        new_node.left.right = BinaryNode(5)
        new_node.right.right = BinaryNode(5)
        new_node.right.right.left = BinaryNode(5)
        self.assertEqual(calculate_node_height(new_node), 3)

    def test_height_one_node(self):
        new_node = BinaryNode(7)
        self.assertEqual(calculate_node_height(new_node), 0)

    def test_calculate_node_depth(self):
        new_node = BinaryNode(7)
        new_node.left = BinaryNode(4)
        new_node.right = BinaryNode(8)
        new_node.left.left = BinaryNode(2)
        new_node.left.right = BinaryNode(5)
        self.assertEqual(calculate_node_depth(new_node, new_node.left.left), 2)

    def test_calculate_node_depth_one_node(self):
        new_node = BinaryNode(7)
        self.assertEqual(calculate_node_depth(new_node, new_node), 0)

    def test_balanced_binary_tree_not_valid(self):
        new_node = BinaryNode(7)
        new_node.left = BinaryNode(4)
        new_node.right = BinaryNode(8)
        new_node.left.left = BinaryNode(2)
        new_node.left.right = BinaryNode(5)
        new_node.right.right = BinaryNode(5)
        new_node.right.right.left = BinaryNode(5)
        self.assertEqual(is_balanced_binary_tree_recursive(new_node), False)

    def test_balanced_binary_tree_valid(self):
        new_node = BinaryNode(7)
        new_node.left = BinaryNode(4)
        new_node.right = BinaryNode(8)
        new_node.left.left = BinaryNode(2)
        new_node.left.right = BinaryNode(5)
        new_node.right.left = BinaryNode(5)
        new_node.right.right = BinaryNode(5)
        new_node.right.right.left = BinaryNode(5)
        self.assertEqual(is_balanced_binary_tree_recursive(new_node), True)

    def test_post_order_traverse(self):
        new_node = BinaryNode('A')
        new_node.left = BinaryNode('B')
        new_node.right = BinaryNode('C')
        new_node.left.left = BinaryNode('D')
        new_node.left.right = BinaryNode('E')
        new_node.right.left = BinaryNode('F')
        new_node.right.right = BinaryNode('G')
        self.assertEqual(post_order_traverse(new_node), ['D', 'E', 'B', 'F', 'G', 'C', 'A'])

    def test_pre_order_traverse(self):
        new_node = BinaryNode(7)
        new_node.left = BinaryNode(4)
        new_node.right = BinaryNode(8)
        new_node.left.left = BinaryNode(2)
        new_node.left.right = BinaryNode(5)
        self.assertEqual(pre_order_traverse(new_node), [7, 4, 2, 5, 8])

    def test_height(self):
        new_node = BinaryNode(7)
        new_node.left = BinaryNode(4)
        new_node.right = BinaryNode(8)
        new_node.left.left = BinaryNode(2)
        new_node.left.right = BinaryNode(5)
        new_node.right.right = BinaryNode(5)
        new_node.right.right.left = BinaryNode(5)
        self.assertEqual(calculate_node_height(new_node), 3)

    def test_height_one_node(self):
        new_node = BinaryNode(7)
        self.assertEqual(calculate_node_height(new_node), 0)

    def test_calculate_node_depth(self):
        new_node = BinaryNode(7)
        new_node.left = BinaryNode(4)
        new_node.right = BinaryNode(8)
        new_node.left.left = BinaryNode(2)
        new_node.left.right = BinaryNode(5)
        self.assertEqual(calculate_node_depth(new_node, new_node.left.left), 2)

    def test_calculate_node_depth_one_node(self):
        new_node = BinaryNode(7)
        self.assertEqual(calculate_node_depth(new_node, new_node), 0)

    def test_balanced_binary_tree_not_valid(self):
        new_node = BinaryNode(7)
        new_node.left = BinaryNode(4)
        new_node.right = BinaryNode(8)
        new_node.left.left = BinaryNode(2)
        new_node.left.right = BinaryNode(5)
        new_node.right.right = BinaryNode(5)
        new_node.right.right.left = BinaryNode(5)
        self.assertEqual(is_balanced_binary_tree_recursive(new_node), False)

    def test_balanced_binary_tree_valid(self):
        new_node = BinaryNode(7)
        new_node.left = BinaryNode(4)
        new_node.right = BinaryNode(8)
        new_node.left.left = BinaryNode(2)
        new_node.left.right = BinaryNode(5)
        new_node.right.left = BinaryNode(5)
        new_node.right.right = BinaryNode(5)
        new_node.right.right.left = BinaryNode(5)
        self.assertEqual(is_balanced_binary_tree_recursive(new_node), True)


if __name__ == '__main__':
    unittest.main()
