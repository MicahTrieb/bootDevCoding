#Lesson Link: https://www.boot.dev/lessons/b21312a0-9422-423f-a7f2-2b847efcb0fe

import math
def log_scale(data, base):
    returnList = []
    if data:
        for currentDataPoint in data:
            returnList.append(math.log(currentDataPoint, base))

    return returnList
