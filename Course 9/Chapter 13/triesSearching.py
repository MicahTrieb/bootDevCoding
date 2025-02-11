#Lesson Link: https://www.boot.dev/lessons/aa5dc9d4-5286-4adf-a8c5-03e738a781a6


#Redid this for practice
class Trie:
    def exists(self, word):
        tempValue = self.root
        for currentLetter in word:
            if currentLetter in tempValue:
                tempValue = tempValue[currentLetter]
            else:
                return False
        if "*" in tempValue:
            return True
        return False

#-------------------------------------------
class Trie:
    def exists(self, word):
        currentDict = self.root
        for currentLetter in word:
            if currentLetter in currentDict:
                if currentDict[currentLetter] == {"*": True}:
                    return True
                currentDict = currentDict[currentLetter]
        return False

    # don't touch below this line

    def add(self, word):
        current = self.root
        for letter in word:
            if letter not in current:
                current[letter] = {}
            current = current[letter]
        current[self.end_symbol] = True

    def __init__(self):
        self.root = {}
        self.end_symbol = "*"
