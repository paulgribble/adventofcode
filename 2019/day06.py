# Part 1
orbits = {}
#f = open('day06_input_test1.txt')
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

# Part 2
# parts adapted from https://pastebin.com/xnj0H31V

data = [l.strip().split(')') for l in open('day06_input.txt').readlines()]

def makegraph(root, data, graph=None):
	if (graph==None):
		graph = {root:[]}
		for k in data:
			graph[k[1]] = []
	for c,o in data:
		if (c==root):
			graph[o] = graph[c] + [o]
			makegraph(o, data, graph)
	return graph

g = makegraph('COM',data)

count = 0
for o in g['YOU'][::-1][1:]:
	if o not in g['SAN']:
		count = count + 1
	else:
		break

for o in g['SAN'][::-1][1:]:
	if o not in g['YOU']:
		count = count + 1
	else:
		break

print("Part 2: answer is {:d}".format(count))
