def quick_sort(nums, low, high):
    returnList = []
    if low < high:
        medianValue = len(nums) // 2
        currentPart = partition(nums, low, high)
        quick_sort(nums[:medianValue], low, medianValue - 1)
        quick_sort(nums[medianValue:], medianValue, high)
def partition(nums, low, high):
    pass



quickSortList = [2, 1, 3]
quick_sort(quickSortList,0, len(quick_sort) - 1)