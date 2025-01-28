#Lesson Link: https://www.boot.dev/lessons/10d15e9c-3d8e-4b12-a4ac-c7fbed095222

def num_possible_orders(num_posts):
    returnValue = 1
    for i in range(1,num_posts + 1):
        returnValue = returnValue * i

    return returnValue
        