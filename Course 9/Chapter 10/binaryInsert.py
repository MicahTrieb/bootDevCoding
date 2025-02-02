#Lesson Link: https://www.boot.dev/lessons/8b49e869-e92f-472b-82ea-c845ef635f88

class BSTNode:
    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.val = val

    def insert(self, val):
        if self.val == None:
            self.val = val
        if self.val == val:
            return
        if self.val < val and not self.right:
            self.right = BSTNode(val)
        elif self.val < val and self.right:
            BSTNode.insert(self.right, val)
        if self.val > val and not self.left:
            self.left = BSTNode(val)
        elif self.val > val and self.left:
            BSTNode.insert(self.left, val)
            
