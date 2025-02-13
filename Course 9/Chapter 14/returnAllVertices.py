#Lesson Link: https://www.boot.dev/lessons/7ed9bd88-b5be-473d-9e4b-8d92a0874c3c

class Graph:
    def adjacent_nodes(self, node):
        return list(self.graph[node])

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
