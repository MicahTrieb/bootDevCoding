#Lesson Link: https://www.boot.dev/lessons/6d67c2b9-e92a-4df2-ad2e-d0536176461e

class Trie:
    def find_matches(self, document):
        newSet = set()
        stringIndices = []
        for currentIndex in document:
            tempLevel = self.root
            currentNumber = 0
            for currentNestedIndex in currentIndex:
                currentNumber += 1
                stringIndices.append(currentNumber)
                if currentNestedIndex not in tempLevel:
                    stringIndices = []
                    break
                tempLevel = tempLevel[currentNestedIndex]
                if "*" in tempLevel:
                    valueA, valueB = stringIndices[0], stringIndices[-1]
                    newSet.add(currentIndex[valueA:valueB])
        return newSet
                
        

    # don't touch below this line

    def __init__(self):
        self.root = {}
        self.end_symbol = "*"

    def add(self, word):
        current = self.root
        for letter in word:
            if letter not in current:
                current[letter] = {}
            current = current[letter]
        current[self.end_symbol] = True
