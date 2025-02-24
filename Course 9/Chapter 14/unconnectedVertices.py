#Lesson Link: https://www.boot.dev/lessons/ea912181-9d34-4bd3-abe3-627db20ea7ea

class Graph:
    def unconnected_vertices(self):
        emptySet = set()
        returnList = []
        for currentKey in self.graph.keys():
            if self.graph[currentKey] == emptySet:
                returnList.append(currentKey)
        return returnList
        
                

    # don't touch below this line

    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u in self.graph:
            self.graph[u].add(v)
        else:
            self.graph[u] = {v}
        if v in self.graph:
            self.graph[v].add(u)
        else:
            self.graph[v] = {u}

    def add_node(self, u):
        if u not in self.graph:
            self.graph[u] = set()
