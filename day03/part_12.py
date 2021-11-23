from collections import defaultdict

lines = [x for x in open('day03/1.in').read().splitlines()]
fabric = defaultdict(set)

for line in lines:
    line = line.split()
    id = line[0]
    x, y = map(int, line[2].removesuffix(':').split(','))
    w, h = map(int, line[3].split('x'))
    for i in range(x, x + w):
        for j in range(y, y + h):
            fabric[(i, j)].add(id)

print(sum(len(a) > 1 for a in fabric.values()))


all_ids = set()
ids_that_overlap = set()
for ids in fabric.values():
    if len(ids) > 1:
        for id in ids:
            all_ids.add(id)
            ids_that_overlap.add(id)
    else:
        all_ids.add(ids.pop())

print((all_ids - ids_that_overlap))
