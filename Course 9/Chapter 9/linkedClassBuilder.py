#Lesson Link: https://www.boot.dev/lessons/6d49ab0d-1c58-44ba-9a78-22f22178f1ba

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    def set_next(self, node):
        self.next = node

    # don't touch below this line

    def __repr__(self):
        return self.val
