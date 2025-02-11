#Lesson Link: https://www.boot.dev/lessons/70432289-a136-4b2a-9d2b-962c60b95ba3

#Redid for practice
class Trie:
    def search_level(self, current_level, current_prefix, words):
        if self.end_symbol in current_level:
            words.append(current_prefix)
        currentKeys = sorted(current_level.keys())
        for currentKey in currentKeys:
            if currentKey != self.end_symbol:
                self.search_level(current_level[currentKey], current_prefix + currentKey, words)
        return words
                

    def words_with_prefix(self, prefix):
        emptyList = []
        tempValue = self.root
        for currentLetter in prefix:
            if currentLetter in tempValue:
                tempValue = tempValue[currentLetter]
            else:
                return []
        return self.search_level(tempValue, prefix, emptyList)

    # don't touch below this line

    def __init__(self):
        self.root = {}
        self.end_symbol = "*"

    def add(self, word):
        current_level = self.root
        for letter in word:
            if letter not in current_level:
                current_level[letter] = {}
            current_level = current_level[letter]
        current_level[self.end_symbol] = True

#---------------------------------------------------------
class Trie:
    def search_level(self, current_level, current_prefix, words):
        if self.end_symbol in current_level:
            words.append(current_prefix)
        for currentKey in sorted(current_level.keys()):
            if currentKey is not self.end_symbol:
                self.search_level(current_level[currentKey], current_prefix + currentKey, words)

        return words
    def words_with_prefix(self, prefix):
        newList = []
        current_level = self.root
        for letter in prefix:
            if letter not in current_level:
                return []
            current_level = current_level[letter]
        return self.search_level(current_level, prefix, newList)

    # don't touch below this line

    def __init__(self):
        self.root = {}
        self.end_symbol = "*"

    def add(self, word):
        current_level = self.root
        for letter in word:
            if letter not in current_level:
                current_level[letter] = {}
            current_level = current_level[letter]
        current_level[self.end_symbol] = True
