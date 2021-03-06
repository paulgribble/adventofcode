
bplist = []

with open("day05_input.txt") as f:
	for line in f:
		b = line.strip('\n')
		b = b.replace('F','0')
		b = b.replace('B','1')
		b = b.replace('L','0')
		b = b.replace('R','1')
		seatid = int(b,2) # the code is binary
		bplist.append(seatid)

bplist = sorted(bplist)

print("Part 1: {}".format(bplist[-1]))

i = 1
found = False
while i<len(bplist) and not found:
	if bplist[i]-bplist[i-1] == 2: # there's a gap
		found = True
	else:
		i += 1

print("Part 2: {}".format(bplist[i]-1))

