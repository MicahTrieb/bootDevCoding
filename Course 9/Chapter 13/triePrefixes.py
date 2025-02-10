class Trie:
    def search_level(self, current_level, current_prefix, words):
        if self.end_symbol in current_level:
            words += current_prefix
        allKeys = current_level.keys()
        allKeys = allKeys.sorted()
        for currentKey in allKeys:
            if currentKey != self.end_symbol:
                search_level(currentKey, current_prefix + currentKey, words)
        return words
    def words_with_prefix(self, prefix):
        emptyList = []
        

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
