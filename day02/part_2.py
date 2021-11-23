def solve(lines):
    pos = 0
    for line1 in lines:
        for line2 in lines[pos + 1:]:
            ans = ''.join(a for a, b in zip(line1, line2) if a == b)
            if len(ans) == 25:
                return ans


print(solve([x for x in open('day02/1.in').read().splitlines()]))
