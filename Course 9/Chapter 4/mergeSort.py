#Lesson Link: https://www.boot.dev/lessons/5066e081-58bf-4d24-a218-cd267f04948b

def merge_sort(nums):
    if len(nums) < 2:
        return nums
    else:
        middleOfList = len(nums) // 2
        sortedSideOne = merge_sort(nums[middleOfList:])
        sortedSideTwo = merge_sort(nums[:middleOfList])
        return merge(sortedSideOne, sortedSideTwo)


def merge(first, second):
    print(f"First: {first} \nSecond: {second}")
    returnList = []
    i = 0
    j = 0
    if first and second:
        while i < len(first) and j < len(second):
            print(f"First list at index: {i} is {first[i]}\n")
            print(f"Second list at index: {j} is {second[j]}")
            if first[i] <= second[j]:
                returnList.append(first[i])
                i += 1
            else:
                returnList.append(second[j])
                j += 1
            if i == len(first) or j == len(second):
                if len(first) > len(second):
        if len(first) > len(second):
            returnList.append(first[:i])
        elif len(second) > len(first):
            returnList.append(second[:j])
    elif first:
        returnList.append(first)
    elif second:
        returnList.append(second)
    return returnList
    
