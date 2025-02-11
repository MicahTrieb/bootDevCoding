#Lesson Link: https://www.boot.dev/lessons/6d67c2b9-e92a-4df2-ad2e-d0536176461e

class Trie:
    def find_matches(self, document):
        newSet = set()
        

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
