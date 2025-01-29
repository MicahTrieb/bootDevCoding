#Lesson Link: https://www.boot.dev/lessons/83e64b78-29cd-4b5d-8fec-6f910475d4e5

def insertion_sort(nums):
    copyOfNums = nums
    for i in range(0,len(copyOfNums)):
        j = i
        while j > 0 and copyOfNums[j - 1] > copyOfNums[j]:
            numOne, numTwo = copyOfNums[j - 1], copyOfNums[j]
            copyOfNums[j] = numOne
            copyOfNums[j - 1] = numTwo
            j -= 1
    return copyOfNums
