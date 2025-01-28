#Lesson Link: https://www.boot.dev/lessons/4179f293-d58a-4382-8ffa-edf6baacf97c

def find_max(nums):
    if nums:
        currentMax = float('-inf')
        for currentNum in nums:
            if currentNum > currentMax:
                currentMax = currentNum
        return currentMax
    return None

