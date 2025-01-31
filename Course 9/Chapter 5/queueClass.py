#Lesson Link: https://www.boot.dev/lessons/73289433-96a5-4468-a977-7bbe3e731767


class Queue:
    def __init__(self):
        self.items = []

    def push(self, item):
        if self.items:
            self.items.insert(0, item)
        else:
            self.items.append(item)

    def pop(self):
        if self.items:
            return self.items.pop(-1)

    def peek(self):
        if self.items:
            return self.items[-1]

    def size(self):
        if self.items:
            return len(self.items)

