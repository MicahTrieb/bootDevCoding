def remove_duplicates(nums):
    returnList = []
    for currentNum in nums:
        if currentNum not in returnList:
            returnList.append(currentNum)

    return returnList
        

