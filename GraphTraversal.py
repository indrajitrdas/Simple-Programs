# Graph Traversal

from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        
    def addEdge(self, u, v):
        self.graph[u].append(v)
        
    def DFS(self, v):
        visited = [False]*(len(self.graph))
        self._DFS(v, visited)
        
    def _DFS(self, v, visited):
        visited[v] = True
        print(v)
        for i in self.graph[v]:
            if visited[i] == False:
                self._DFS(i, visited)
                
    def BFS(self, v):
        visited = [False]*(len(self.graph))
        queue = []
        queue.append(v)
        visited[v] = True
        while queue:
            v = queue.pop(0)
            print(v)
            for i in self.graph[v]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True
                
                
g = Graph() 
g.addEdge(0, 1) 
g.addEdge(0, 2) 
g.addEdge(1, 2) 
g.addEdge(2, 0) 
g.addEdge(2, 3) 
g.addEdge(3, 3)
g.DFS(2)
print(" ")
g.BFS(2)
        