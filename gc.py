
G = [
    [0, 1, 1, 0, 1, 0],
    [1, 0, 1, 1, 0, 1],
    [1, 1, 0, 1, 1, 0],
    [0, 1, 1, 0, 0, 1],
    [1, 0, 1, 0, 0, 1],
    [0, 1, 0, 1, 1, 0]
]


nodes = "abcdef"


node_index = {}
for i in range(len(G)):
    node_index[nodes[i]] = i


degree = []
for i in range(len(G)):
    degree.append(sum(G[i]))


colors = ["Blue", "Red", "Yellow", "Green"]


colorDict = {}
for i in range(len(G)):
    colorDict[nodes[i]] = colors.copy()


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


theSolution = {}
for n in sortedNode:
    current_color = colorDict[n][0]  
    theSolution[n] = current_color
    
    for j in range(len(G[node_index[n]])):
        if G[node_index[n]][j] == 1:
            neighbor = nodes[j]
            if current_color in colorDict[neighbor]:
                colorDict[neighbor].remove(current_color)


print("Node Coloring Result:")
for t in sorted(theSolution):
    print("Node", t, "=", theSolution[t])
