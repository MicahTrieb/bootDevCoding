#Lesson Link: https://www.boot.dev/lessons/10a39842-5bd3-40e9-946c-d066e2b206d5

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

    def rotate_left(self, pivot_parent):
        if pivot_parent == self.nil or pivot_parent.right == self.nil:
            return
        currentPivot = pivot_parent.right
        pivot_parent.right = currentPivot.left
        if currentPivot.left != self.nil:
            currentPivot.left.parent = pivot_parent
        currentPivot.parent = pivot_parent.parent
        if pivot_parent == self.root:
            self.root = currentPivot
        elif pivot_parent == pivot_parent.parent.left:
            pivot_parent.parent.left = currentPivot
        elif pivot_parent == pivot_parent.parent.right:
            pivot_parent.parent.right = currentPivot
        currentPivot.left = pivot_parent
        pivot_parent.parent = currentPivot
        

    def rotate_right(self, pivot_parent):
        if pivot_parent == self.nil or pivot_parent.left == self.nil:
            return
        currentPivot = pivot_parent.left
        pivot_parent.left = currentPivot.right
        if currentPivot.right != self.nil:
            currentPivot.right.parent = pivot_parent
        currentPivot.parent = pivot_parent.parent
        if pivot_parent == self.root:
            self.root = currentPivot
        elif pivot_parent == pivot_parent.parent.left:
            pivot_parent.parent.left = currentPivot
        elif pivot_parent == pivot_parent.parent.right:
            pivot_parent.parent.right = currentPivot
        currentPivot.right = pivot_parent
        pivot_parent.parent = currentPivot
        

        # don't touch below this line

    def insert(self, val):
        new_node = RBNode(val)
        new_node.parent = None
        new_node.left = self.nil
        new_node.right = self.nil
        new_node.red = True

        parent = None
        current = self.root
        while current != self.nil:
            parent = current
            if new_node.val < current.val:
                current = current.left
            elif new_node.val > current.val:
                current = current.right
            else:
                # duplicate, just ignore
                return

        new_node.parent = parent
        if parent is None:
            self.root = new_node
        elif new_node.val < parent.val:
            parent.left = new_node
        else:
            parent.right = new_node
