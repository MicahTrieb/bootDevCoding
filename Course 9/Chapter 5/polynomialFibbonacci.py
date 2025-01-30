#Lesson Link: https://www.boot.dev/lessons/87a81b0e-e6e8-442e-b418-c077658c195a

def fib(n):
    copyOfN = n
    grandparent = 0
    parent = 1
    currentFib = 1
    for currentValue in range(0,n-2):
        #print(currentValue)
        #print(f"Before conversion: \nCurrent fib: {currentFib}\nGrandparent: {grandparent}\nParent: {parent}")
        parent, grandparent = currentFib, parent
        currentFib = parent + grandparent
        #print(f"After conversion: \nCurrent fib: {currentFib}\nGrandparent: {grandparent}\nParent: {parent}")
    return currentFib
        
        