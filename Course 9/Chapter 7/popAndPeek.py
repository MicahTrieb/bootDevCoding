#Lesson Link: https://www.boot.dev/lessons/d148cd17-4fb1-47f3-9501-0fd9f433f54d

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def size(self):
        return len(self.items)

    def peek(self):
        if self.items:
            return self.items[-1]
        else:
            return None

    def pop(self):
        if self.items:
            return self.items.pop(-1)
        else:
            return None
