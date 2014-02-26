import unittest
from BinarySearchTree import bTree

class TestBinarySearchTree(unittest.TestCase):
    
    def setUp(self):
        self.tree = bTree.fromValue(8)
        
    def test_initialization(self):
        self.assertNotEqual(self.tree, None)
        self.assertNotEqual(self.tree.root, None)
        self.assertEqual(self.tree.root.key, 8)
        
    def setUpTree1(self):
        """
        sets up the following tree after the inital setUp function:
                         8
                      /     \
                    /         \
                   3            10
                 /   \           \
                1     6          14
                     / \        /
                    4   7     13
        """
        self.tree.insertValues([3, 1, 6, 4, 7, 10, 14, 13])
        
    def test_insert(self):
        self.tree.insert(3)
        self.assertEqual(self.tree.root.left.key, 3)
        self.assertEqual(self.tree.root.right, None)
        self.tree.insert(10)
        self.assertEqual(self.tree.root.right.key, 10)
        self.tree.insert(1)
        self.assertEqual(self.tree.root.left.left.key, 1)
        self.tree.insert(5)
        self.assertEqual(self.tree.root.left.right.key, 5)
        self.tree.insert(9)
        self.assertEqual(self.tree.root.right.left.key, 9)
        self.assertEqual(self.tree.root.left.left.left, None)
        self.assertEqual(self.tree.root.right.right, None)
        self.tree.insert(13)
        self.assertEqual(self.tree.root.right.right.key, 13)
        self.tree.insert(15)
        self.assertEqual(self.tree.root.right.right.right.key, 15)
        
    def test_Duplicates(self):
        self.tree.insert(8)
        self.assertEqual(self.tree.root.key, 8)
        self.assertEqual(self.tree.root.right.key, 8)
        self.tree.remove(8)
        self.assertEqual(self.tree.root.key, 8)
        self.assertEqual(self.tree.root.right, None)
        
    def test_findMin(self):
        self.setUpTree1()
        self.assertEqual(self.tree.findMinLeaf(self.tree.root).key, 1)
        self.assertEqual(self.tree.findMinLeaf(self.tree.root.left.right).key, 4)
        self.assertEqual(self.tree.findMinLeaf(self.tree.root.right).key, 10)
        self.assertEqual(self.tree.findMinLeaf(self.tree.root.right.right).key, 13)
        
    def test_remove(self):
        self.setUpTree1()
        self.tree.remove(10)
        self.assertEqual(self.tree.root.right.key, 14)
        self.tree.remove(3)
        self.assertEqual(self.tree.root.left.key, 4)
        self.assertEqual(self.tree.root.left.right.left, None)
        self.tree.remove(8)
        self.assertEqual(self.tree.root.key, 13)
        
    def test_removeAndAddRoot(self):
        self.tree.remove(8)
        self.assertEqual(self.tree.root, None)
        self.tree.insert(7)
        self.assertEqual(self.tree.root.key, 7)
        
    def test_sortedValues(self):
        self.setUpTree1()
        self.assertEqual(list(self.tree.getSortedValues()), list([1, 3, 4, 6, 7, 8, 10, 13, 14]))
        
unittest.main()