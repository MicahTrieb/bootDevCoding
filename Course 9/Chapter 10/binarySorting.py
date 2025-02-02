#Lesson Link: https://www.boot.dev/lessons/8b49e869-e92f-472b-82ea-c845ef635f88

class BSTNode:
    def delete(self, val):
        if not self.val:
            return None
        if val > self.val:
            if self.right:
                self.right = BSTNode.delete(self.right, val)
                return self
        if val < self.val:
            if self.left:
                self.left = BSTNode.delete(self.left, val)
                return self
        if self.val == val:
            if self.right and not self.left:
                return self.right
            elif self.left and not self.right:
                return self.left
            elif self.left and self.right:
                minNode = self.right.min_larger_node()
                self.val = minNode.val
                self.right = self.right.right
        return self
                

    def min_larger_node(self, val):
        if self.left and self.left.val > val:
            return min_larger_node(self.left, val)
        elif not self.left:
            return self
        return self
        
    # don't touch below this line

    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.val = val

    def insert(self, val):
        if not self.val:
            self.val = val
            return

        if self.val == val:
            return

        if val < self.val:
            if self.left:
                self.left.insert(val)
                return
            self.left = BSTNode(val)
            return

        if self.right:
            self.right.insert(val)
            return
        self.right = BSTNode(val)

            
