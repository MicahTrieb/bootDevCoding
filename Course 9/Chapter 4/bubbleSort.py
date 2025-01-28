#Lesson Link: https://www.boot.dev/lessons/ad175094-e40d-4d49-baf7-d364da42216c

def bubble_sort(nums):
    swapping = True
    end = len(nums)
    print(nums)
    while swapping == True:
        swapping = False
        for currentIndex in range(0, end):
            if currentIndex + 1 < end:  
                if nums[currentIndex + 1] < nums[currentIndex]:
                    swapping = True
                    swappingNumOne = nums[currentIndex + 1]
                    swappingNumTwo = nums[currentIndex]
                    nums[currentIndex + 1] = swappingNumTwo
                    nums[currentIndex] = swappingNumOne
    return nums
                
