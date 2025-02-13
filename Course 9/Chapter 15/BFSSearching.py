#Lesson Link: https://www.boot.dev/lessons/a607653a-92c2-4898-b19f-e5469384a1c6

class Graph:
    def bfs_path(self, start, end):
        if self.does_end_exist(start,end):
            print("1")
            toVisit = [start]
            visited = []
            print("2")
            layerDict = {}
            layer = 0
            layerDict[self.graph[start]] = layer
            print("3")
            while toVisit:
                print("4")
                currentNeighbors = sorted(list(self.graph[start]))
                visited.append(toVisit.pop(0))
                if end in currentNeighbors:
                    layer += 1
                    layerDict[end] = layer
                    break
                for current in currentNeighbors:
                    if current not in visited and current not in toVisit:
                        toVisit.append(current)
            return None
            print(layerDict)
        else:
            return None
    
    def does_end_exist(self, start, end):
        found = False
        toVisit = [start]
        visited = []
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
