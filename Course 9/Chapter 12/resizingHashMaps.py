#Lesson Link: https://www.boot.dev/lessons/63a168df-81ef-4b82-804a-1e9775428081

class HashMap:
    def insert(self, key, value):
        self.resize()
        index = self.key_to_index(key)
        self.hashmap[index] = (key, value)

    def resize(self):
        if len(self.hashmap) == 0:
            self.hashmap.append(None)
        loadPercentage = self.current_load()
        if loadPercentage < 0.05:
            return
        newHash = HashMap(len(self.hashmap) - 1 * 10)
        for currentValue in range(0,len(self.hashmap)):
            newHash.insert(self.hashmap[currentValue][0], self.hashmap[currentValue][1])
        
        self.hashmap = newHash.hashmap

    def current_load(self):
        if len(self.hashmap) == 0:
            return 1
        else:
            noneCount = 0
            for currentValue in self.hashmap:
                if currentValue is not None:
                    noneCount += 1
            return (noneCount / len(self.hashmap))

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
