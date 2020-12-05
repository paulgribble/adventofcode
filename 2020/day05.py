
bplist = []

idmax = 0
with open("day05_input.txt") as f:
	for line in f:
		b = line.strip('\n')
		bb = b.replace('F','0').replace('B','1').replace('L','0').replace('R','1')
		seatid = int(bb,2) # the code is binary
		bplist.append(seatid)
		if seatid>idmax:
			idmax = seatid

print("Part 1: {}".format(idmax))

bplist = sorted(bplist)

i = 1
found = False
while i<len(bplist) and not found:
	if bplist[i]-bplist[i-1] == 2: # there's a gap
		found = True
	else:
		i += 1

print("Part 2: {}".format(bplist[i]-1))

