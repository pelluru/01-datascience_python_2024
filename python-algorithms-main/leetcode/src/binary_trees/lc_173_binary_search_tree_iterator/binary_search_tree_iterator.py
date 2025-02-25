from collections import deque
class BSTIterator:
    def __init__(self, root):
        self.data = []
        self.inorder(root)
        self.position = 0 if len(self.data) > 0 else -1
        
    def next(self) -> int:
        if self.hasNext():
            next_val = self.data[self.position]
            self.position += 1
            return next_val
        
    def hasNext(self) -> bool:
        if self.data and self.position < len(self.data):
            return True
        return False

    def inorder(self, root):
        if root is None: return 
        
        self.inorder(root.left)
        self.data.append(root.val)
        self.inorder(root.right)



# Solution 2 - Using Queue
class BSTIterator2:
    def __init__(self, root):
        self.data = deque()
        self.inorder(root)
        
    def next(self) -> int:
        if self.hasNext():
            next_val = self.data.pop()
            return next_val
        
    def hasNext(self) -> bool:
        if self.data:
            return True
        return False

    def inorder(self, root):
        if root is None: return 
        
        self.inorder(root.left)
        self.data.appendleft(root.val)
        self.inorder(root.right)