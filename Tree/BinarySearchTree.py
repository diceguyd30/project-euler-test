class Node:
    left, right = None, None
    
    def __init__(self, n):
        self.key = n
    
class bTree:
    
    def __init__(self):
        self.root = None
        
    @classmethod
    def fromValues(cls, values):
        tree = cls()
        tree.insertValues(values)
        return tree
        
    @classmethod
    def fromValue(cls, value):
        tree = cls()
        tree.insert(value)
        return tree
        
    def insert(self, n):
        self._insertHelper(n, self.root)
        
    def _insertHelper(self, n, node):
        if node:
            if n < node.key:
                if node.left:
                    self._insertHelper(n, node.left)
                else:
                    node.left = Node(n)
            else:
                if node.right:
                    self._insertHelper(n, node.right)
                else:
                    node.right = Node(n)
        else:
            self.root = Node(n)
            
    def insertValues(self, values):
        for x in values:
            self.insert(x)
                
    def remove(self, n):
        self._removeHelper(n, self.root, None)
    
    def _removeHelper(self, n, node, parent):
        if node:
            if node.key > n:
                self._removeHelper(n, node.left, node)
            elif node.key < n:
                self._removeHelper(n, node.right, node)
            else:
                if node.right and node.left:
                    newNode = self.findMinLeaf(node.right)
                    node.key = newNode.key
                    self._removeHelper(newNode.key, node.right, node)
                elif node.right:
                    self._replaceNodeInParent(parent, node.right)
                elif node.left:
                    self._replaceNodeInParent(parent, node.left)
                else:
                    if parent:
                        if parent.key > node.key:
                            parent.left = None
                        else:
                            parent.right = None
                    else:
                        self.root = None
                    
    def _replaceNodeInParent(self, parent, node):
        if parent.key > node.key:
            parent.left = node
        else:
            parent.right = node
            
    def findMinLeaf(self, n):
        if n.left:
            return self.findMinLeaf(n.left)
        return n