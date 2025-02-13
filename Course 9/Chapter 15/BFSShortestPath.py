#Lesson Link:https://www.boot.dev/lessons/c0803659-7811-44fd-a532-3baf926fe435


#----------------------------------------------------------------
    def bfs_path(self, start, end):
        if self.does_end_exist(start, end):
            toVisit = [start]
            visitedDict = {}
            visited = []
            returnVisited = []
            currentIndex = 0
            while toVisit:                
                endNeighbor = sorted(list(self.graph[toVisit[0]]))
                visited.append(toVisit.pop(0))
                if end in endNeighbor:
                    visited.append(end)
                    break
                for currentNeighbor in endNeighbor:
                    if currentNeighbor not in visited and currentNeighbor not in toVisit:
                        toVisit.append(currentNeighbor)
            while visited:
                currentLastIndex = visited.pop(-1)
                if len(self.graph[currentLastIndex]) == 1:
                    returnVisited.append(currentLastIndex)
                elif len(self.graph[currentLastIndex]) > 1:
                    for currentNeighbor in self.graph[currentLastIndex]:
                        if currentNeighbor not in visited:
                            continue
                        for i in self.graph[currentNeighbor]:
                            
                        
                    
        else:
            return None











#------------------------------------------------------------------------------------

#Redo part three:
class Graph:
    def bfs_path(self, start, end):
        if self.graph:
            if end in self.graph:
                toVisit, visited, pathTraversed, rootNeighbours = [start], [], {}, sorted(list(self.graph[start]))

                for currentNeighbour in rootNeighbours:
                    toVisit = [currentNeighbour]
                    pathTraversed[currentNeighbour] = [start]
                    while toVisit:
                        pathTraversed[currentNeighbour].append(toVisit[0])
                        sortedNeighbors = sorted(list(self.graph[toVisit[0]]))
                        visited.append(toVisit.pop(0))
                        if end in sortedNeighbors:
                            pathTraversed[currentNeighbour].append(end)
                            break
                        for currentVisitTarget in sortedNeighbors:
                            if currentVisitTarget not in visited and currentVisitTarget not in toVisit:
                                visited.append(currentVisitTarget)
                        if not toVisit:
                            pathTraversed[currentNeighbour] == None
                            break
                for currentTraversal in pathTraversed:
                    if pathTraversed[currentTraversal]:
                        while len(currentTraversal) >= 3:

                    else:
                        continue

                            
                '''for currentTraversal in pathTraversed:
                    if pathTraversed[currentTraversal]:
                        endNode = pathTraversed[currentTraversal].pop(-1)
                        newList = [endNode]
                        tempNode = endNode
                        for currentNeighbor in sorted(list(self.graph[endNode])):
                            tempNode = currentNeighbor
                            while tempNode != start:
                                checkList = sorted(list(self.graph[tempNode]))
                                if tempNode in visited:
                                    for currentNode in checkList:
                                        if currentNode in visited:'''





                        



                    
                                

            return None
        return None

    # don't touch below this line

    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u in self.graph.keys():
            self.graph[u].add(v)
        else:
            self.graph[u] = set([v])
        if v in self.graph.keys():
            self.graph[v].add(u)
        else:
            self.graph[v] = set([u])

    def __repr__(self):
        result = ""
        for key in self.graph.keys():
            result += f"Vertex: '{key}'\n"
            for v in sorted(self.graph[key]):
                result += f"has an edge leading to --> {v} \n"
        return result

#-------------------------------------------------------------
#Meant to find the shortest path between start and end node in a graph
#Yikes this went bad, restarting...

class Graph:
    def bfs_path(self, start, end):
        if self.does_end_exist(start, end):
            toVisit = [start]
            visited = []
            pathTraversed = {}
            rootNeighbours = sorted(list(self.graph[start]))
            for currentNeighbour in rootNeighbours:
                pathTraversed[currentNeighbour] = set()
            while True:
                for currentNeighbour in rootNeighbours:
                    
                
            
        else:
            return None


    def does_end_exist(self, start, end):
        found = False
        toVisit = [start]
        visited = []
        rootNeighbours = sorted(list(self.graph[start]))
        while True:
            currentVisitingNeighbours = sorted(list(self.graph[toVisit[0]]))
            if end in currentVisitingNeighbours:
                return True
            visited.append(toVisit.pop(0))
            for currentNeighbour in currentVisitingNeighbours:
                if currentNeighbour not in visited and currentNeighbour not in toVisit:
                    toVisit.append(currentNeighbour)
            if not toVisit:
                return False

    # don't touch below this line

    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u in self.graph.keys():
            self.graph[u].add(v)
        else:
            self.graph[u] = set([v])
        if v in self.graph.keys():
            self.graph[v].add(u)
        else:
            self.graph[v] = set([u])

    def __repr__(self):
        result = ""
        for key in self.graph.keys():
            result += f"Vertex: '{key}'\n"
            for v in sorted(self.graph[key]):
                result += f"has an edge leading to --> {v} \n"
        return result


        




    # don't touch below this line

    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u in self.graph.keys():
            self.graph[u].add(v)
        else:
            self.graph[u] = set([v])
        if v in self.graph.keys():
            self.graph[v].add(u)
        else:
            self.graph[v] = set([u])

    def __repr__(self):
        result = ""
        for key in self.graph.keys():
            result += f"Vertex: '{key}'\n"
            for v in sorted(self.graph[key]):
                result += f"has an edge leading to --> {v} \n"
        return result
