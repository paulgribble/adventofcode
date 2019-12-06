
orbits = {}
f = open('day06_input.txt')
for l in f:
	o = l.strip('\n').split(')')
	orbits[o[1]] = o[0]

f.close()

def child(o,orbits):
	if (o=='COM'):
		return(0)
	else:
		return(1 + child(orbits[o],orbits))

count = 0
for k in orbits.keys():
	count = count + child(k,orbits)

print("Part 1: answer is {:d}".format(count))


