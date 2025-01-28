#Lesson Link: https://www.boot.dev/lessons/25edbe21-4f2a-4a18-853a-af4cb922df8a

def average_followers(nums):
    #Solving it without using sum(nums) & len(nums)
    sumValue = 0
    listLength = 0
    if nums:
        for currentNum in nums:
            sumValue += currentNum
            listLength += 1
        return sumValue / listLength
        

    else:
        return None
