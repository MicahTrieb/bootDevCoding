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
    
