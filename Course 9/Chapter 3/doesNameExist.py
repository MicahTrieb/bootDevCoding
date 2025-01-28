#Lesson Link: https://www.boot.dev/lessons/0a8c6304-93a1-451d-a7c0-d2f87f652472

def does_name_exist(first_names, last_names, full_name):
    splitName = full_name.split(" ")
    print(splitName)
    for currentName in first_names:
        if currentName == splitName[0]:
            for currentLastName in last_names:
                if currentLastName == splitName[1]:
                    return True
    return False
