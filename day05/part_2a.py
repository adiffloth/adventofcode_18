# Use a list of chars and join() at the end to avoid creating lots of new strings.
# Make a single pass: use pop() to look back and remove units that can newly react.

def react(polymer):
    reduced_polymer = ['']
    for unit in polymer:
        if unit == reduced_polymer[-1].swapcase():
            reduced_polymer.pop()
        else:
            reduced_polymer.append(unit)
    return ''.join(reduced_polymer)


line = [x for x in open('day05/1.in').read().splitlines()][0]
all_units = set(line.lower())

# Part 1
print(len(react(line)))

# Part 2
print(min(len(react(line.replace(candidate, '').replace(candidate.upper(), ''))) for candidate in all_units))
