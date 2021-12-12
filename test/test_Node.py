import unittest

from app.data_structures.tree import BinaryNode

class TestStringMethods(unittest.TestCase):

    def test_node_with_empty_value(self):
        new_node = BinaryNode(None)
        self.assertEqual(new_node.val, None)

    def test_node_with_value(self):
        new_node = BinaryNode(100)
        self.assertEqual(new_node.val, 100)

if __name__ == '__main__':
    unittest.main()