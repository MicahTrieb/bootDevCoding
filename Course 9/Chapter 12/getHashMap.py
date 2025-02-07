#Lesson Link: https://www.boot.dev/lessons/cabe4b06-1ee2-4654-9650-fb17eb0adab1

class HashMap:
    def get(self, key):
        try:
            return self.hashmap[self.key_to_index(key)][1]
        except:
            raise Exception("sorry, key not found")
    # don't touch below this line

    def __init__(self, size):
        self.hashmap = [None for i in range(size)]

    def key_to_index(self, key):
        sum = 0
        for c in key:
            sum += ord(c)
        return sum % len(self.hashmap)

    def insert(self, key, value):
        i = self.key_to_index(key)
        self.hashmap[i] = (key, value)

    def __repr__(self):
        final = ""
        for i, v in enumerate(self.hashmap):
            if v != None:
                final += f" - {str(v)}\n"
        return final
