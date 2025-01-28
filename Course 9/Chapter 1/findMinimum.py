#Lesson Link: https://www.boot.dev/lessons/b6e716d2-df64-487e-aa7b-d768e8a2c8fc
def find_minimum(nums):
    if nums:
        currentMinimum = float("inf")
    else:
        return None
    for currentNum in nums:
        if isinstance(currentNum, int):
            currentMinimum = min(currentNum, currentMinimum)

    return currentMinimum
