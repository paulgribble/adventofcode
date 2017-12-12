

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
groups = 0
while (len(searchme)>0):
	s = searchme.pop()
	g = getgroup(s)
	groups += 1
	searchme -= g # delete those already in the found group

print('part 2: there are {} groups in total'.format(groups))



