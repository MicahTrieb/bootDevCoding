#Lesson Link: https://www.boot.dev/lessons/e044c349-8b8f-4289-b1a6-a38963532adf

class RBNode:
    def __init__(self, val):
        self.red = False
        self.parent = None
        self.val = val
        self.left = None
        self.right = None


class RBTree:
    def __init__(self):
        self.nil = RBNode(None)
        self.nil.red = False
        self.nil.left = None
        self.nil.right = None
        self.root = self.nil

    def insert(self, val):
        newNode = RBNode(val)
        newNode.left = RBNode(None)
        newNode.right = RBNode(None)
        newNode.red = True
        newNode.parent = None
        currentVal = self.root
        while currentVal != self.nil:
            newNode.parent = currentVal
            if newNode.val < currentVal.val:
                currentVal.left = currentVal
            elif newNode.val > currentVal.val:
                currentVal.right = currentVal
            else:
                return currentVal
        newNode.parent = currentVal
        if newNode.parent == None:
            self.root = newNode
        else:
            if newNode.val > newNode.parent.val:
                newNode.parent.left = newNode
            else:
                newNode.parent.right = newNode
