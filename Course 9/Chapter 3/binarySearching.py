#Lesson link: https://www.boot.dev/lessons/ce043580-186d-4ab1-a045-672fd56ac152

def binary_search(target, arr):
    if arr:
        if len(arr) > 2:
            currentLow = 0
            currentHigh = len(arr) - 1
            currentMedian = (currentLow + currentHigh) // 2
            while currentMedian != currentLow and currentMedian != currentHigh:
                currentMedian = (currentLow + currentHigh) // 2
                if arr[currentMedian] == target:
                    return True
                elif arr[currentMedian] > target:
                    currentHigh = currentMedian - 1
                elif arr[currentMedian] < target:
                    currentLow = currentMedian + 1
        elif len(arr) == 1:
            return(arr[0] == target)
        else:
            for currentNum in arr:
                if currentNum == target:
                    return True
    return False