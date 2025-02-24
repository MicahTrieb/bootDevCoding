#Lesson Link: https://www.boot.dev/lessons/64877fbc-b634-4b11-8b8e-1ba6460adcf6


def tsp(cities, paths, dist):
    perms = permutations(cities)
    for currentPerm in perms:
        total_dist = 0
        for i in range(1, len(currentPerm)):
            total_dist += paths[currentPerm[i - 1]][currentPerm[i]]
        if total_dist < dist:
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



#---------------------------------------------------
#Third official rewrite, I've lost track
def tsp(cities, paths, dist):
    permutationList = permutations(paths)
    totalSum = 0
    for j in range(0, len(permutationList)):
        for i in range(0, len(permutationList[0])):
            currentMinimum = float("inf")
            for currentPermutation in permutationList:
                currentMinimum = min(currentMinimum, currentPermutation[j][i])
            if currentMinimum != 0:
                totalSum += currentMinimum
        if totalSum < dist:
            return True
    return False
            
            


    #Grab every index, calculating minimum, add them up


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


#------------------------------------------
#I am so confused, rewriting....
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
