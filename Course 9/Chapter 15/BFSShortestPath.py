#Lesson Link:https://www.boot.dev/lessons/c0803659-7811-44fd-a532-3baf926fe435



#Meant to find the shortest path between start and end node in a graph
class Graph:
    def bfs_path(self, start, end):
        totalRouteTime = {}
        found = False
        toVisit = [start]
        visited = []
        rootNeighbours = sorted(list(self.graph[start]))
        for currentRootNeighbour in rootNeighbours:
            totalRouteTime[currentRootNeighbour] = set()
        
        while toVisit and found == False:
            currentVisitingNeighbours = sorted(list(self.graph[toVisit[0]]))
            if end in currentVisitingNeighbours:
                found = True
                continue
            visited.append(toVisit.pop(0))
            
        




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
