#Lesson Link: https://www.boot.dev/lessons/5f62f856-53bf-47aa-a5b0-ada9381e3e57

def quick_sort(nums, low, high):
    if low < high:
        currentPart = partition(nums, low, high)
        quick_sort(nums, low, currentPart - 1)
        quick_sort(nums, currentPart, high)

def partition(nums, low, high):
    pivot = nums[high]
    i = low
    for currentIndex in range(low, high):
        if nums[currentIndex] < pivot:
            swapOne, swapTwo = nums[i], nums[currentIndex]
            nums[i] = swapTwo
            nums[currentIndex] = swapOne
            i += 1
    swapOne, swapTwo = nums[i], nums[high]
    nums[i] = swapTwo
    nums[high] = swapOne
    return i


#Second copy rewritten for practice 

def quick_sort(nums, low, high):
    if low < high:
        current_part = partition(nums, low, high)
        quick_sort(nums, low, current_part - 1)
        quick_sort(nums, current_part, high)


def partition(nums, low, high):
    pivot = nums[high]
    i = low
    for currentIndex in range(low, high):
        if nums[currentIndex] < pivot:
            nums[currentIndex], nums[i] = nums[i], nums[currentIndex]
            i += 1
    
    nums[i], nums[high] = nums[high], nums[i]
    return i

    
