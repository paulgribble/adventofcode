# Advent of Code 2021 Day 1
# https://adventofcode.com/2021/day/1

with open("day01_input.txt") as f:
        D = [int(x) for x in f]

n = len(D)

n_increases = 0
for i in range(1,n):
    if ((D[i]-D[i-1]) > 0):
        n_increases = n_increases + 1
    
print("Part 1: there were {:d} increases".format(n_increases))

n_increases = 0
for i in range(3,n):
    sum1 = D[i-3]+D[i-2]+D[i-1]
    sum2 = D[i-2]+D[i-1]+D[i]
    if ((sum2-sum1) > 0):
        n_increases = n_increases + 1
    
print("Part 2: there were {:d} increases".format(n_increases))

