# Works, but many string copies and multiple passes make it slow.

from collections import defaultdict


def soln(unit):
    lines = [x for x in open('day05/1.in').read().splitlines()]
    line = lines[0]

    new_str = ''
    prev_len = len(line) + 1

    while prev_len > len(line):
        prev_len = len(line)
        new_str = ''
        i = 0
        while i < len(line) - 1:
            if (line[i].lower() == unit):
                i += 1
            elif ((line[i].lower() == line[i + 1].lower()) & (line[i] != line[i + 1])):
                i += 2
            else:
                new_str += line[i]
                i += 1
        if (line[-1].lower() != unit) & (line[-2].lower() != line[-1].lower()):
            new_str += line[-1]
        line = new_str
    return len(new_str)


counts = defaultdict()
for i in range(26):
    unit = chr(i + 97)
    cnt = soln(unit)
    print(f'{unit}: {cnt}')
    counts[unit] = cnt

unit_to_drop = min(counts, key=counts.get)
print(f'\n{unit_to_drop}: {counts[unit_to_drop]}\n')
