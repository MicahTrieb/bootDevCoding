#Lesson Link:https://www.boot.dev/lessons/c0803659-7811-44fd-a532-3baf926fe435



#Meant to find the shortest path between start and end node in a graph
class Graph:
    def bfs_path(self, start, end):
        visited = []
        tempValue = start
        currentShortestPath = float("inf")
        currentValue = 0
        #while currentShortestPath < currentValue and len(visited) + 1 != len(self.graph) * len(self.graph):



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
