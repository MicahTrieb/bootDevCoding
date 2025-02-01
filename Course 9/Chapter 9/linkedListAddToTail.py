#Lesson Link: https://www.boot.dev/lessons/83776963-56ab-4a4d-acc6-301f284b916a

from node import Node


class LinkedList:
    def add_to_tail(self, node):
        if self.head == None:
            self.head = node
            return
        else:
            for currentNode in self:
                lastNode = currentNode
            lastNode.next = node
                
            

    # don't touch below this line

    def __init__(self):
        self.head = None

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def __repr__(self):
        nodes = []
        for node in self:
            nodes.append(node.val)
        return " -> ".join(nodes)
