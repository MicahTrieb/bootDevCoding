def count_names(list_of_lists, target_name):
    nameCounter = 0
    for currentList in list_of_lists:
        if target_name in currentList:
            for currentName in currentList:
                if currentName == target_name:
                    nameCounter += 1
    return nameCounter
                
