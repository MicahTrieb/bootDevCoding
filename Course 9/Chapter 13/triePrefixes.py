class Trie:
    def search_level(self, current_level, current_prefix, words):
        if self.end_symbol in current_level:
            words += current_prefix
        allKeys = current_level.keys().sorted()
        for currentKey in allKeys:
            if currentKey is not self.end_symbol:
                search_level(currentKey, current_prefix + currentKey, words)

        return words
    def words_with_prefix(self, prefix):
        newList = []
        copyDict = self
        for currentLetter in prefix:
            if currentLetter in copyDict:
                copyDict = copyDict[currentLetter]
        search_level(copyDict, prefix, newList)
        return newList

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
