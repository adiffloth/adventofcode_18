from collections import defaultdict
import numpy as np

lines = [x for x in open('day04/1_sorted.in').read().splitlines()]

guard = ''
start_sleep = 0
guards = defaultdict()
guard_mins = defaultdict()

for line in lines:
    time = int(line[15:17])
    desc = line[19:]

    if desc.startswith('Guard'):
        guard = int(desc.split()[1].removeprefix('#'))
    elif desc.startswith('falls'):
        start_sleep = time
    elif desc.startswith('wakes'):
        sleep_array = np.zeros(60, int)
        sleep_array[start_sleep:time] = 1
        if guard in guards:
            guards[guard] = guards[guard] + sleep_array
            guard_mins[guard] = guard_mins[guard] + sum(sleep_array)
        else:
            guards[guard] = sleep_array
            guard_mins[guard] = sum(sleep_array)
    else:
        raise(ValueError("unexpected desc " + desc))

sleepiest_guard = max(guard_mins, key=guard_mins.get)
print(sleepiest_guard)
sleepiest_minute = guards[sleepiest_guard].argmax()
print(sleepiest_minute)
print(sleepiest_guard * sleepiest_minute)

# Part 2
max_g_idx = max_m_idx = max_m_val = -1
for g, ms in guards.items():
    print(ms)
    for k, m in enumerate(ms):
        if m > max_m_val:
            max_m_val = m
            max_m_idx = k
            max_g_idx = g
print(max_g_idx, max_m_idx, max_g_idx * max_m_idx)
print(max_m_val)
