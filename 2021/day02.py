# Advent of Code 2021 Day 2
# https://adventofcode.com/2021/day/2

h,d = 0,0
aim = 0

with open("day02_input.txt") as f:
        for l in f:
            l = l.strip().split(' ')
            i,x = l[0],int(l[1])
            if (i=='forward'):
                h = h + x
            elif (i=='up'):
                d = d - x
            elif (i=='down'):
                d = d + x

print('Part 1: {:d}'.format(h*d))


h,d = 0,0
aim = 0

with open("day02_input.txt") as f:
        for l in f:
            l = l.strip().split(' ')
            i,x = l[0],int(l[1])
            if (i=='forward'):
                h = h + x
                d = d + (aim*x)
            elif (i=='up'):
                aim = aim - x
            elif (i=='down'):
                aim = aim + x

print('Part 2: {:d}'.format(h*d))



