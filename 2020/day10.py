with open("day10_input.txt") as f:
	A = [int(r.strip('\n')) for r in f]

A.sort()
A.append(A[-1]+3)
AA = []
AA.append(0)
ii = 0
for i in range(len(A)-1):
	if (A[i]-AA[ii]) in [1,2,3]:
		AA.append(A[i])
		ii += 1
AA.append(AA[-1]+3)

d1,d2,d3 = 0,0,0
for i in range(len(AA)-1):
	if (AA[i+1]-AA[i])==1:
		d1 += 1
	elif (AA[i+1]-AA[i]==2):
		d2 += 1
	elif (AA[i+1]-AA[i]==3):
		d3 += 1

print("Part 1: {}".format(d1*d3))


# reddit helped here, to point me in the right direction.
# to develop my own recursive approach
# https://www.reddit.com/r/adventofcode/comments/ka8z8x/2020_day_10_solutions/gf9ot1i/

# for memoization
W = {}

def ways(i,AA,W):
	if i in W.keys():
		return W[i]
	elif i==AA[-1]:
		W[i] = 1
		return 1
	elif i not in AA:
		W[i] = 0
		return 0
	if i+1 not in W.keys():
		W[i+1] = ways(i+1,AA,W)
	if i+2 not in W.keys():
		W[i+2] = ways(i+2,AA,W)
	if i+3 not in W.keys():
		W[i+3] = ways(i+3,AA,W)
	W[i] = W[i+1] + W[i+2] + W[i+3]
#	print("{},{},{}\n{},{},{}\n".format(i+1,i+2,i+3,W[i+1],W[i+2],W[i+3]))
	return W[i]

print("Part 2: {}".format(ways(0,AA,W)))


# saw this one on reddit
# https://github.com/tymscar/Advent-Of-Code/blob/master/2020/day10/part2.py

from collections import defaultdict
file = open('day10_input.txt', 'r')
jolts = [0]
highest = 0

for line in file:
    line = line.strip("\n")
    jolts.append(int(line))
    highest = max(highest, int(line))

jolts.append(highest + 3)

jolts = sorted(jolts)

ways = defaultdict(lambda:0)
ways[0] = 1

for i in range(1, len(jolts)):
    ways[jolts[i]] = ways[jolts[i]-1] + ways[jolts[i]-2] + ways[jolts[i]-3]

print("Part 2: {}".format(ways[jolts[-1]]))



