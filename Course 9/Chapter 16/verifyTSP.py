#Lesson Link: https://www.boot.dev/lessons/024501ed-d7cd-472b-b98c-7059c7cce799

def verify_tsp(paths, dist, actual_path):
    currentSum = 0
    for i in range(0, len(actual_path)):
        if i + 1 >= len(actual_path):
            continue
        currentSum += paths[actual_path[i]][actual_path[i+1]]
    if currentSum < dist:
        return True
    return False