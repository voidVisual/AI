# Adjacency Matrix of the Graph
G = [
    [0, 1, 1, 0, 1, 0],
    [1, 0, 1, 1, 0, 1],
    [1, 1, 0, 1, 1, 0],
    [0, 1, 1, 0, 0, 1],
    [1, 0, 1, 0, 0, 1],
    [0, 1, 0, 1, 1, 0]
]

# Node labels
nodes = "abcdef"

# Create mapping from node label to index
node_index = {}
for i in range(len(G)):
    node_index[nodes[i]] = i

# Count degree of all nodes
degree = []
for i in range(len(G)):
    degree.append(sum(G[i]))

# Available colors
colors = ["Blue", "Red", "Yellow", "Green"]

# Initialize color dictionary for each node
colorDict = {}
for i in range(len(G)):
    colorDict[nodes[i]] = colors.copy()

# Sort nodes based on descending degree
sortedNode = []
used_indices = []

for _ in range(len(degree)):
    max_deg = -1
    idx = -1
    for j in range(len(degree)):
        if j not in used_indices and degree[j] > max_deg:
            max_deg = degree[j]
            idx = j
    used_indices.append(idx)
    sortedNode.append(nodes[idx])

# Main coloring process
theSolution = {}
for n in sortedNode:
    current_color = colorDict[n][0]  # pick the first available color
    theSolution[n] = current_color
    # Remove this color from adjacent nodes
    for j in range(len(G[node_index[n]])):
        if G[node_index[n]][j] == 1:
            neighbor = nodes[j]
            if current_color in colorDict[neighbor]:
                colorDict[neighbor].remove(current_color)

# Print the solution
print("Node Coloring Result:")
for t in sorted(theSolution):
    print("Node", t, "=", theSolution[t])
