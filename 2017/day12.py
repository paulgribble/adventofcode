

#pipes = {}
#pipes[0] = [2]
#pipes[1] = [1]
#pipes[2] = [0,3,4]
#pipes[3] = [2,4]
#pipes[4] = [2,3,6]
#pipes[5] = [6]
#pipes[6] = [4,5]

# part 1

lines = [line.strip('\n') for line in open("day12_input.txt")]
pipes = {}
for l in lines:
	pin, pout = l.split(' <-> ')
	pout = pout.split(', ')
	pin = int(pin)
	pout = set(map(int,pout))
	pipes[pin] = pout


def getgroup(root):
	group, new = {root}, {root}
	while (len(new)>0):
		addme = set()
		for item in new:
			addme.update(pipes[item])
		new = addme - group
		group.update(addme)
	return group

g0 = getgroup(0)
g0len = len(g0)
print('part 1: {} programs are in the group that contains 0'.format(g0len))


# part 2

searchme = set(pipes.keys()) # a set of the keys
numgroups = 0
while (len(searchme)>0):
	s = searchme.pop()            # simultaneously get the next one to search and remove it from the set
	g = getgroup(s)               # get all programs in that group
	numgroups = numgroups + 1     # increment the numgroups counter
	searchme = searchme - g       # delete programs in the latest found group, from the searchme list

print('part 2: there are {} groups in total'.format(numgroups))



