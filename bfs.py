from collections import deque


def bfs(graph, start):
    visited = set()
    queue = deque([start])

    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            print(vertex, end=' ')
            visited.add(vertex)
            for neighbor in graph[vertex]:
                if neighbor not in visited:
                    queue.append(neighbor)


vertices = int(input("Enter number of vertices: "))
edges = int(input("Enter number of edges: "))


graph = {i: [] for i in range(vertices)}

print("Enter edges (format: src dest):")
for _ in range(edges):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)  


start = int(input("Enter starting vertex: "))


print("BFS Traversal:")
bfs(graph, start)
