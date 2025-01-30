#Lesson Link: https://www.boot.dev/lessons/54b128ea-626d-4cf7-be1d-b719d4a65787

def power_set(input_set):
    if not input_set:
        return []
    returnList = []
    currentVariable = input_set[0]
    weirdShenanigans = [currentVariable]
    returnList.append(powerSet(inputSet[0:])
