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
        newNode.left = self.nil
        newNode.right = self.nil
        newNode.red = True
        newNode.parent = None
        parent = newNode.parent
        currentVal = self.root
        while currentVal != self.nil:
            print("In")
            parent = currentVal
            if newNode.val < currentVal.val:
                currentVal = currentVal.left
            elif newNode.val > currentVal.val:
                currentVal = currentVal.right
            elif newNode.val == currentVal.val:
                return currentVal
        newNode.parent = parent
        if newNode.parent == None:
            print("In2")
            self.root = newNode
        else:
            print("In3")
            if newNode.val > newNode.parent.val:
                newNode.parent.left = newNode
            else:
                newNode.parent.right = newNode
