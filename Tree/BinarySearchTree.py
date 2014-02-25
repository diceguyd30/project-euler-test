class Node:
    left, right = None, None
    
    def __init__(self, n):
        self.key = n
    
class bTree:
    
    def __init__(self, n):
        self.root = Node(n)
        
    def insert(self, n):
        self._insertHelper(n, self.root)
        
    def _insertHelper(self, n, node):
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