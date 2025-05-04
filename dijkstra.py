import sys
def dijkstra(graph, start_vertex):
    n = len(graph)
    visited = [False] * n
    distance = [sys.maxsize] * n
    distance[start_vertex] = 0

    for _ in range(n):
        min_distance = sys.maxsize
        min_index = -1
        for i in range(n):
            if not visited[i] and distance[i] < min_distance:
                min_distance = distance[i]
                min_index = i

        u = min_index
        visited[u] = True

        for v in range(n):
            if graph[u][v] > 0 and not visited[v]:
                new_dist = distance[u] + graph[u][v]
                if new_dist < distance[v]:
                    distance[v] = new_dist

    print("\nVertex \tDistance from Source")
    for i in range(n):
        print(f"{i} \t{distance[i]}")

graph = [
    [0, 4, 0, 0, 0, 0, 0, 8, 0],
    [4, 0, 8, 0, 0, 0, 0, 11, 0],
    [0, 8, 0, 7, 0, 4, 0, 0, 2],
    [0, 0, 7, 0, 9, 14, 0, 0, 0],
    [0, 0, 0, 9, 0, 10, 0, 0, 0],
    [0, 0, 4, 14, 10, 0, 2, 0, 0],
    [0, 0, 0, 0, 0, 2, 0, 1, 6],
    [8, 11, 0, 0, 0, 0, 1, 0, 7],
    [0, 0, 2, 0, 0, 0, 6, 7, 0]
]

source = 0

dijkstra(graph, source)
