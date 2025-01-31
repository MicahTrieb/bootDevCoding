#Lesson Link: https://www.boot.dev/lessons/cfe7f6a4-aa8b-4669-bed2-93004e1eff3f

from stack import Stack


class DebounceStack(Stack):
    def __init__(self):
        self.items = []
    def push(self, item):
        currentStacked = None
        if Stack.size(self) >= 1:
            currentStacked = Stack.peek(self)
        if item == currentStacked:
            pass
        else:
            self.items.append(item)
        return None

