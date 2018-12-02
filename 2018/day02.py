
# Advent of Code 2018 Day 2

# Part 1
twice, thrice = 0, 0
for line in open("day02_input.txt"):
	box = line.strip('\n')
	A = [0] * 26
	for i in range(len(box)):
		A[ord(box[i])-ord('a')] += 1
	twice += 2 in A
	thrice += 3 in A
print("Day 2 Part 1: checksum is {:d}".format(twice*thrice))

# Part 2

boxes = [line.strip('\n') for line in open("day02_input.txt")]
n = len(boxes)
enough = False
i,j = -1,0
while (not enough):
	i = i + 1
	for j in range(1,n):
		A = [0] * 26
		for k in range(26):
			A[k] = boxes[i][k] == boxes[j][k]
		if sum(A) == 25:
			enough = True
			break
common = ''
for c in range(26):
	if (A[c]==True):
		common += boxes[i][c]
print("Day 2 Part 2: common letters are {:s}".format(common))


