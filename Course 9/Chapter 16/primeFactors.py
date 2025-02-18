#Lesson Link: https://www.boot.dev/lessons/7b3d9eae-bf21-4dcd-8ca3-264f70e60cef

import math


def prime_factors(n):
    remainder = 0
    returnList = []
    while n % 2 == 0:
        remainder = n % 2
        if remainder == 0:
            returnList.append(2)
        else:
            break
        if n == 2:
            break
        n = n / 2
    for i in range(3, math.ceil((math.sqrt(n) + 1)), 2):
        while n % i == 0:
            returnList.append(i)
            n = n / i
    if n > 2:
        returnList.append(int(n))
    return returnList
