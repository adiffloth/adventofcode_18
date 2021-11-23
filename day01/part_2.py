def calibrate():
    freq = 0
    freqs = {0}
    while(True):
        lines = [int(x) for x in open('day01/1.in').read().splitlines()]
        for line in lines:
            freq += line
            if freq in freqs:
                return freq
            freqs.add(freq)


print(calibrate())
