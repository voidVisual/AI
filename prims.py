INF = 9999999

# Take user input for number of vertices
V = int(input("Enter number of vertices: "))

# Create the graph as an adjacency matrix
print("Enter the adjacency matrix (use 0 if no edge):")
G = []
for i in range(V):
    row = list(map(int, input(f"Row {i+1}: ").split()))
    G.append(row)

# Track selected vertices
selected = [False] * V
no_edge = 0
selected[0] = True  # Start from the first vertex

print("\nEdge : Weight")
while no_edge < V - 1:
    minimum = INF
    x = 0
    y = 0

    for i in range(V):
        if selected[i]:
            for j in range(V):
                if not selected[j] and G[i][j]:
                    if minimum > G[i][j]:
                        minimum = G[i][j]
                        x = i
                        y = j

    print(f"{x} - {y} : {G[x][y]}")
    selected[y] = True
    no_edge += 1
