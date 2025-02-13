#Lesson Link: https://www.boot.dev/lessons/e2345ef4-f077-40b2-86ed-a30d911f50c8

class Graph:
    def __init__(self, num_vertices):
        self.graph = []
        for currentNumber in range(0, num_vertices):
            self.graph.append([])
            for currentNumberTwo in range(0, num_vertices):
                self.graph[currentNumber].append(False)

    def add_edge(self, u, v):
        self.graph[u][v] = True
        self.graph[v][u] = True

    # don't touch below this line

    def edge_exists(self, u, v):
        if u < 0 or u >= len(self.graph):
            return False
        if len(self.graph) == 0:
            return False
        row1 = self.graph[0]
        if v < 0 or v >= len(row1):
            return False
        return self.graph[u][v]
