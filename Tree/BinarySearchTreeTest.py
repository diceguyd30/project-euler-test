import unittest
from BinarySearchTree import bTree

class TestBinarySearchTree(unittest.TestCase):
    
    def setUp(self):
        self.tree = bTree(7)
        
    def test_initialization(self):
        self.assertNotEqual(self.tree, None)
        self.assertNotEqual(self.tree.root, None)
        self.assertEqual(self.tree.root.key, 7)
        
    def test_insert(self):
        self.tree.insert(3)
        self.assertEqual(self.tree.root.left.key, 3)
        self.assertEqual(self.tree.root.right, None)
        self.tree.insert(9)
        self.assertEqual(self.tree.root.right.key, 9)
        self.tree.insert(1)
        self.assertEqual(self.tree.root.left.left.key, 1)
        self.tree.insert(5)
        self.assertEqual(self.tree.root.left.right.key, 5)
        self.tree.insert(8)
        self.assertEqual(self.tree.root.right.left.key, 8)
        self.assertEqual(self.tree.root.left.left.left, None)
        self.assertEqual(self.tree.root.right.right, None)
        
unittest.main()