#Lesson Link: https://www.boot.dev/lessons/a901fb8e-f07c-43e1-9bf4-289a5f391667

from node import Node


class LLQueue:
    def remove_from_head(self):
        if self.head:
            temp = self.head
            self.head = self.head.next
            if self.head == None:
                self.tail = None
            return temp
        return self.head

    # don't touch below this line

    def add_to_tail(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
            return
        self.tail.set_next(node)
        self.tail = node

    def __init__(self):
        self.tail = None
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
        return " <- ".join(nodes)
