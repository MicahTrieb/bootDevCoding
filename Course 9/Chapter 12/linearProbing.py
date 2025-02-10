#Lesson Link: https://www.boot.dev/lessons/dc221d3a-2e1b-4231-8ae3-0c89f806130b
#Linear probing, causing infinite loop...
class HashMap:
    def insert(self, key, value):
        indexValue = self.key_to_index(key)
        originalIndex = indexValue
        firstIteration = True
        while self.hashmap[indexValue] is not None and self.hashmap[indexValue][0] != key:
            if firstIteration == False and indexValue == originalIndex:
                raise Exception("hashmap is full")
            indexValue += 1
            if indexValue % len(self.hashmap) == 0:
                indexValue = 0
            firstIteration = False
        self.hashmap[indexValue] = (key, value)
    def get(self, key):
        indexValue = self.key_to_index(key)
        originalIndex = indexValue
        firstIteration = True
        while self.hashmap[indexValue] is not None:
            if self.hashmap[indexValue][0] == key:
                return self.hashmap[indexValue][1]
            if firstIteration == False and indexValue == originalIndex:
                raise Exception("sorry, key not found")
            indexValue += 1
            if indexValue % len(self.hashmap) == 0:
                indexValue = 0
            firstIteration = False
        raise Exception("sorry, key not found")
                

    # don't touch below this line

    def __init__(self, size):
        self.hashmap = [None for i in range(size)]

    def key_to_index(self, key):
        sum = 0
        for c in key:
            sum += ord(c)
        return sum % len(self.hashmap)

    def __repr__(self):
        final = ""
        for i, v in enumerate(self.hashmap):
            if v != None:
                final += f" - {str(v)}\n"
        return final


    # don't touch below this line

    def __init__(self, size):
        self.hashmap = [None for i in range(size)]

    def key_to_index(self, key):
        sum = 0
        for c in key:
            sum += ord(c)
        return sum % len(self.hashmap)

    def __repr__(self):
        final = ""
        for i, v in enumerate(self.hashmap):
            if v != None:
                final += f" - {str(v)}\n"
        return final
