#Lesson Link: https://www.boot.dev/lessons/77eead15-82c9-4047-b303-f93c1ac6af2d

from stack import Stack

def is_balanced(input_str):
    leftCount = 0
    rightCount = 0
    stackClass = Stack()
    if input_str:
        if len(input_str) == 1:
            return False
        for currentItem in list(input_str):
            stackClass.push(currentItem)
        while stackClass.items:
            currentPop = stackClass.items.pop(-1)
            if currentPop == ")":
                for currentIndex in range(stackClass.size() - 1, -1, -1):
                    pass
        
    else:
        return False










#Full rewrite, misunderstood lesson
'''def is_balanced(input_str):
    leftCount = 0
    rightCount = 0
    if input_str:
        if len(input_str) == 1:
            return False
        for currentIndex in range(len(input_str) - 1, -1, -1):
            if input_str[currentIndex] == ")":
                rightCount += 1
            elif input_str[currentIndex] == "(":
                leftCount += 1
        if rightCount == leftCount:
            return True
        return False
    else:
        return False'''
