#Lesson Link: https://www.boot.dev/lessons/61d52d19-05df-460c-821a-586a3257afe2

def get_num_guesses(length):
    returnValue = 26
    for i in range(1,length):
        returnValue = (returnValue + 1) * 26
    return returnValue
