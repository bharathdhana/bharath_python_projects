import heapq
def dijkstra(graph,start):
    distances = {vertex:float('inf') for vertex in graph}
    distances[start] = 0
    heap = [(0,start)]
    while heap:
        (current_distance,current_vertex) = heapq.heappop(heap)
        if current_distance > distances[current_vertex]:
            continue
        for neighbour,weight in graph[current_vertex].items():
            distance = current_distance + weight
            if distance < distances[neighbour]:
                distances[neighbour] = distance
                heapq.heappush(heap,(distance,neighbour))

        return distances


graph = {'A':{'B':2, 'C':4},
         'B':{'D':3},
         'C':{'D':1, 'E':5},
         'D':{'E':1},
         'E':{}
         }
start_vertex =  'A'
shortest_distances = dijkstra(graph,start_vertex)
print("The Shortest distance using Dijkstra's algorithm:",shortest_distances)
