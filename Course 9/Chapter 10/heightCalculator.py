#Lesson Link: https://www.boot.dev/lessons/59717501-d833-4c2c-a0e1-1938eaf97326

class BSTNode:
    def height(self):
        leftHeight = 1
        rightHeight = 1
        if self.val is None:
            return 0
        if self.left is None and self.right is None:
            return 1
        if self.left:
            leftHeight += self.left.height()
        if self.right:
            rightHeight += self.right.height()
        return max([leftHeight, rightHeight])
            
        