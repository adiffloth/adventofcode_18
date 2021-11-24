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
max_dist = 10000

# For every cell in the grid, add up the distances to all the nodes
grid = []
for curr_x in range(min_x, max_x + 1):
    for curr_y in range(min_y, max_y + 1):
        distances = 0
        for node in nodes:
            distances += dist(curr_x, curr_y, node[0], node[1])
        if distances < max_dist:
            grid.append((curr_x, curr_y))

print(len(grid))
