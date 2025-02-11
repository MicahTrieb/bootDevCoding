#Lesson Link: https://www.boot.dev/lessons/f8a46c86-6c34-4f41-90f7-bb6f6a881b3c

class Trie:
    def longest_common_prefix(self):
        current = self.root
        prefix = ""
        while True:
            keys = current.keys()
            childrenAmount = len(current.keys())
            if "*" in current:
                break
            if childrenAmount == 1:
                prefix += current[keys[0]]
                current = current[keys[0]]
            else:
                break
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
