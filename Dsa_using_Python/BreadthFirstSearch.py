from collections import deque
class Graph:
    def __init__(self):
        self.adjacency_list = {}
    def add_edge(self,u,v):
        if u not in self.adjacency_list:
            self.adjacency_list[u] = []
        if v not in self.adjacency_list:
            self.adjacency_list[v] = []
            
        self.adjacency_list[u].append(v)
        self.adjacency_list[v].append(u)

    def bfs(self,start):
        visited = {start}
        queue = deque([start])
        while queue:
            vertex = queue.popleft()
            print(vertex,end =" ")
            for neighbour in self.adjacency_list[vertex]:
                if neighbour not in visited:
                    visited.add(neighbour)
                    queue.append(neighbour)

g = Graph()
g.add_edge(0,1)
g.add_edge(0,2)
g.add_edge(1,3)
g.add_edge(1,4)
g.add_edge(2,5)
g.add_edge(4,5)
print("The Bfs of the graph is:")
g.bfs(2)
