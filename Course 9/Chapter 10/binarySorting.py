#Lesson Link: https://www.boot.dev/lessons/8b49e869-e92f-472b-82ea-c845ef635f88

class BSTNode:
    def delete(self, val):
        if not self.val:
            return None
        if val > self.val:
            if self.right:
                BSTNode.delete(self.right, val)
                return self
        if val < self.val:
            if self.left:
                BSTNode.delete(self.left, val)
                return self
        if self.val == val:
            if self.right and not self.left:
                return self.right
            elif self.left and not self.right:
                return self.left
            elif self.left and self.right:
                if self.right.left:
                    minNode = BSTNode.min_larger_node(self.right.left, val)
                    self.val = minNode.val
                    self.right = BSTNode.delete(self, val)
                elif not self.right.left:
                    self.val = self.right.val
                    
                    
            return self

    def min_larger_node(self, val):
        if self.left and self.left.val > val:
            min_larger_node(self, val)
        return self
        
            
