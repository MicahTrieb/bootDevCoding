#Lesson Link: https://www.boot.dev/lessons/820b7d02-52fd-4c94-8c62-d52242a9c438

#Rewriten for practice

class Trie:
    def add(self, word):
        tempVariable = self.root
        for currentLetter in word:
            if currentLetter not in tempVariable:
                tempVariable[currentLetter] = {}
            tempVariable = tempVariable[currentLetter]
        tempVariable["*"] = True

            
    # don't touch below this line

    def __init__(self):
        self.root = {}
        self.end_symbol = "*"







class Trie:
    def add(self, word):
        currentValue = self.root
        for currentLetter in word:
            if currentLetter not in currentValue.keys():
                currentValue[currentLetter] = {}
                currentValue = currentValue[currentLetter]
            else:
                currentValue = currentValue[currentLetter]
        currentValue[self.end_symbol] = True

    # don't touch below this line

    def __init__(self):
        self.root = {}
        self.end_symbol = "*"
