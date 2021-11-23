from collections import Counter

lines = [x for x in open('day02/1.in').read().splitlines()]
twos = 0
threes = 0
for line in lines:
    cnt = Counter(line)
    twos += (2 in cnt.values())
    threes += (3 in cnt.values())

print(twos * threes)
