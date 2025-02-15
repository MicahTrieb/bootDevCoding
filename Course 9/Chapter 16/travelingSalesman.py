#Lesson Link: https://www.boot.dev/lessons/64877fbc-b634-4b11-8b8e-1ba6460adcf6

def tsp(cities, paths, dist):
    permutationList = permutations(paths)
    for currentPermutation in permutationList:
        currentSum = 0 
        for currentIndex in range(0, len(currentPermutation):
            currentSum += currentPermutation
        if currentSum < dist:
            return True
    return False

# don't touch below this line


def permutations(arr):
    res = []
    res = helper(res, arr, len(arr))
    return res


def helper(res, arr, n):
    if n == 1:
        tmp = arr.copy()
        res.append(tmp)
    else:
        for i in range(n):
            res = helper(res, arr, n - 1)
            if n % 2 == 1:
                arr[n - 1], arr[i] = arr[i], arr[n - 1]
            else:
                arr[0], arr[n - 1] = arr[n - 1], arr[0]
    return res
