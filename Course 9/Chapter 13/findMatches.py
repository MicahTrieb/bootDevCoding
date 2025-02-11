#Lesson Link: https://www.boot.dev/lessons/6d67c2b9-e92a-4df2-ad2e-d0536176461e

class Trie:
    def find_matches(self, document):
        newSet = set()
        stringIndices = []
        currentNumber = 0
        tempLevel = self.root
        for currentIndex in document:
            for currentNestedIndex in currentIndex:
                stringIndices.append(currentNumber)
                currentNumber += 1
                #print(f"{currentNestedIndex in tempLevel} of {currentNestedIndex} in {tempLevel}")
                if currentNestedIndex not in tempLevel:
                    #print(f"Broken at {currentNestedIndex} with current string indices of {stringIndices}")
                    stringIndices = []
                    tempLevel = self.root
                    break
                tempLevel = tempLevel[currentNestedIndex]
                if "*" in tempLevel:
                    valueA, valueB = stringIndices[0], (stringIndices[-1] + 1)
                    #print(f"Successful with {document[valueA:valueB]}")
                    newSet.add(document[valueA:valueB])
                    tempLevel = self.root
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
