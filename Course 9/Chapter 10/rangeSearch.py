#Lesson Link: https://www.boot.dev/lessons/386b4010-be66-4790-8eb0-1bdf485dd5df

class BSTNode:
    def search_range(self, lower_bound, upper_bound, returnList=None):
        if returnList == None:
            returnList = []
        if self.val >= lower_bound and self.val <= upper_bound:
            if self.left:
                print(f"{self.val} has a left {self.left.val}")
                self.left.search_range(lower_bound, upper_bound, returnList)
            returnList.append(self.val)
            if self.right:
                print(f"{self.val} has a right {self.right.val}")
                self.right.search_range(lower_bound, upper_bound, returnList)
                        
        return returnList
              

    # don't touch below this line

    def exists(self, val):
        if val == self.val:
            return True

        if val < self.val:
            if self.left is None:
                return False
            return self.left.exists(val)

        if self.right is None:
            return False
        return self.right.exists(val)

    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.val = val

    def insert(self, val):
        if not self.val:
            self.val = val
            return

        if self.val == val:
            return

        if val < self.val:
            if self.left:
                self.left.insert(val)
                return
            self.left = BSTNode(val)
            return

        if self.right:
            self.right.insert(val)
            return
        self.right = BSTNode(val)
