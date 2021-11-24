lines = [x for x in open('day05/1.in').read().splitlines()]
line = lines[0]

print(len(line))
new_str = ''
prev_len = len(line) + 1

while prev_len > len(line):
    prev_len = len(line)
    new_str = ''
    i = 0
    while i < len(line) - 1:
        if ((line[i].lower() == line[i + 1].lower()) & (line[i] != line[i + 1])):
            i += 2
        else:
            new_str += line[i]
            i += 1
    new_str += line[-1]
    line = new_str

print(len(new_str))
