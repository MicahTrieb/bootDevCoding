#Lesson Link: https://www.boot.dev/lessons/4991a909-8c8c-4971-9099-5b89788bce61

def count_names(list_of_lists, target_name):
    nameCounter = 0
    for currentList in list_of_lists:
        if target_name in currentList:
            for currentName in currentList:
                if currentName == target_name:
                    nameCounter += 1
    return nameCounter
                
