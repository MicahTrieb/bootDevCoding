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
    returnList = []
    if first and second:
        while first and second:
            if first[0] >= second[0]:
                returnList.append(second.pop(0))
            elif second[0] > first[0]:
                returnList.append(first.pop(0))
        if first:
            returnList.extend(first)
        elif second:
            returnList.extend(second)
                  
    elif first:
        return first
    elif second:
        return second
    else:
        return None
    return returnList

    
