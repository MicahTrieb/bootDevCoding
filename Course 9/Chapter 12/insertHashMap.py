#Lesson Link: https://www.boot.dev/lessons/fe0bc417-69dc-435e-95c8-79cd8dde04a0

class HashMap:
    def insert(self, key, value):
        self.hashmap[self.key_to_index(key)] = (key, value)

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
                final += f" - {i}: {str(v)}\n"
            else:
                final += f" - {i}: None\n"
        return final
