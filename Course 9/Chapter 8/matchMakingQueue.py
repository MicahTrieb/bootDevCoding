#Lesson Link: https://www.boot.dev/lessons/cd2268ff-f75b-4e02-ae47-148818efced1

from queue import Queue
    

def matchmake(queue, user):
    if user[1] == 'leave':
        queue.search_and_remove(user[0])
    if user[1] == 'join':
        queue.push(user[0])
    if queue.size() >= 4:
        firstPop, secondPop = queue.pop(), queue.pop()
        return (f"{firstPop} matched {secondPop}!")
    elif queue.size() < 4:
        return "No match found"
