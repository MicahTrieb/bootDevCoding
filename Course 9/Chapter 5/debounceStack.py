#Lesson Link: https://www.boot.dev/lessons/cfe7f6a4-aa8b-4669-bed2-93004e1eff3f

from stack import Stack


class DebounceStack(Stack):

    
    def push(self, item):
        currentStacked = Stack.peek(self)
        if item == currentStacked:
            pass
        else:
            self.push(item)
        
