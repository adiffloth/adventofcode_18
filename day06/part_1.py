from collections import Counter


def dist(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)


lines = [x for x in open('day06/1.in').read().splitlines()]

# Parse the input nodes, figure out the bounds
nodes = []
for line in lines:
    nodes.append(tuple(map(int, line.split(', '))))
min_x = min([x[0] for x in nodes])
max_x = max([x[0] for x in nodes])
min_y = min([x[1] for x in nodes])
max_y = max([x[1] for x in nodes])

# Nodes on the edges will have infinite area and need to be excluded
edge_nodes = set()
for node in nodes:
    if (node[0] in [min_x, max_x]) or (node[1] in [min_y, max_y]):
        edge_nodes.add(node)

# For every cell in the grid, get the closest node, don't count ties
grid = []
for curr_x in range(min_x, max_x + 1):
    for curr_y in range(min_y, max_y + 1):
        distances = []
        for node in nodes:
            distances.append((node, dist(curr_x, curr_y, node[0], node[1])))
        distances.sort(key=lambda x: x[1])
        if distances[0][1] != distances[1][1]:
            grid.append(distances[0][0])

# Find the node to which the greatest number of cells belong, eliminate edge nodes
dist_counts = Counter(grid)
for edge_node in edge_nodes:
    dist_counts.pop(edge_node)
print(max(dist_counts.values()))
