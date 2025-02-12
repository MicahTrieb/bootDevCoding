#Lesson Link: https://www.boot.dev/lessons/dd146e90-6275-448a-89c4-d148e52ab022

#Good thing I didn't delete it, ended up being EXACTLY what I needed

class Trie:
    def advanced_find_matches(self, document, variations):
        replacedString = document
        for currentVariation in variations:
            replacedString = replacedString.replace(currentVariation, variations[currentVariation])
        allMatches = self.find_matches(replacedString)
        matches = set()
        for currentMatch in allMatches:
            found = False
            currentWord = ""
            for currentLetter in currentMatch:
                if currentLetter in variations.values():
                    found = True
                    currentWord += variations[currentLetter]
                else:
                    currentWord += currentLetter
            if found == True:
                matches.add(currentWord)
        return matches
    # don't touch below this line

    def find_matches(self, document):
        matches = set()
        for i in range(len(document)):
            level = self.root
            for j in range(i, len(document)):
                ch = document[j]
                if ch not in level:
                    break
                level = level[ch]
                if self.end_symbol in level:
                    matches.add(document[i : j + 1])
        return matches

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





#-----------------------------------------------------------
#Wrote this but realized it doesn't work, keeping it here anyways


class Trie:
    def advanced_find_matches(self, document, variations):
        matches = set()
        matchesSet = self.find_matches(document)
        for currentMatch in matchesSet:
            found = False
            currentWord = ""
            print(currentMatch)
            for currentLetter in currentMatch:
                if currentLetter in variations:
                    print("Found")
                    found = True
                    currentWord += variations[currentLetter]
                else:
                    currentWord += currentLetter
            if found == True:
                matches.add(currentWord)
        return matches
                    

    # don't touch below this line

    def find_matches(self, document):
        matches = set()
        for i in range(len(document)):
            level = self.root
            for j in range(i, len(document)):
                ch = document[j]
                if ch not in level:
                    break
                level = level[ch]
                if self.end_symbol in level:
                    matches.add(document[i : j + 1])
        return matches

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
