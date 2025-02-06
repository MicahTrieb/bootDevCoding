#Lesson Link: https://www.boot.dev/lessons/27eef24f-7b9a-41b2-81e1-d84e13eb919a

class HashMap:
    def key_to_index(self, key):
        returnValue = 0
        for currentIndex in key:
            returnValue += ord(currentIndex)
        return (returnValue % len(self.hashmap))
        
    # don't touch below this line

    def __init__(self, size):
        self.hashmap = [None for i in range(size)]

    def __repr__(self):
        buckets = []
        for v in self.hashmap:
            if v != None:
                buckets.append(v)
        return str(buckets)
