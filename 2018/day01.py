# Advent of Code 2018 Day 1

# Part 1
freq = sum([int(line.strip('\n')) for line in open("day01_input.m")])
print('Day 1 Part 1: the frequency is {:d}'.format(freq))

# Part 2
freq = 0
fi = [int(line.strip('\n')) for line in open("day01_input.txt")]
n = len(fi)
i = 0
freqs_found = set()
while ((freq in freqs_found)==False):
	freqs_found.add(freq)
	freq = freq + fi[i]
	i = (i + 1) % n
print('Day 1 Part 2: {:d} is the first freq to repeat'.format(freq))

