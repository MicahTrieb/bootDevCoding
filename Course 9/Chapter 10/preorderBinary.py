#Lesson Link: https://www.boot.dev/lessons/6a158883-5cba-4be8-85e4-66752ea4d469

class BSTNode:
    def preorder(self, visited):
        visited.append(self.val)
        currentNode = self
        while currentNode.left:
            if currentNode.right:
                visited.extend(currentNode.right.preorder(visited))
            visited.append(currentNode.left)
            currentNode = currentNode.left
        while currentNode.right:
            if currentNode.left:
                visited.extend(currentNode.left.preorder(visited))
            visited.append(currentNode.right)
            currentNode = currentNode.right
            
        return visited
                

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
