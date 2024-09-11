import heapq

def prim(graph):
    visited = set()
    minimum_spanning_tree = []
    
    # Starting with the first vertex in the graph
    start_vertex = list(graph.keys())[0]
    visited.add(start_vertex)
    
    # Initialize the priority queue with edges from the start vertex
    edges = [(weight, start_vertex, neighbour) for neighbour, weight in graph[start_vertex].items()]
    heapq.heapify(edges)
    
    while edges:
        (weight, vertex1, vertex2) = heapq.heappop(edges)
        
        if vertex2 in visited:
            continue
        
        minimum_spanning_tree.append((vertex1, vertex2, weight))
        visited.add(vertex2)
        
        for neighbour, weight in graph[vertex2].items():
            if neighbour not in visited:
                heapq.heappush(edges, (weight, vertex2, neighbour))
    
    return minimum_spanning_tree

graph = {
    'A': {'B': 2, 'C': 4},
    'B': {'A': 2, 'D': 3},
    'C': {'A': 4, 'D': 1, 'E': 5},
    'D': {'B': 3, 'C': 1, 'E': 1},
    'E': {'C': 5, 'D': 1}
}

minimum_spanning_tree = prim(graph)
print("The minimum spanning tree using Prim's algorithm is:", minimum_spanning_tree)
