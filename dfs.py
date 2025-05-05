
def dfs(graph, vertex, visited):
    visited.add(vertex)
    print(vertex, end=' ')
    for neighbor in graph[vertex]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)
 

vertices = int(input("Enter number of vertices: "))
edges = int(input("Enter number of edges: "))


graph = {i: [] for i in range(vertices)}

print("Enter edges (format: src dest):")
for _ in range(edges):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)  


start = int(input("Enter starting vertex: "))


print("DFS Traversal:")
visited = set()
dfs(graph, start, visited)

