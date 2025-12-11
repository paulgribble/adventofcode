from math import sqrt

boxes = []
with open("input2") as f:
	for line in f:
		boxes.append(tuple([int(x) for x in line.strip().split(',')]))

def distance3d(b1,b2):
	return sqrt((b2[2]-b1[2])**2 + (b2[1]-b1[1])**2 + (b2[0]-b1[0])**2)

rows,cols = len(boxes), len(boxes[0])

dists = []
for ir in range(1,rows):
	for ic in range(ir):
		dists.append([(boxes[ir],boxes[ic]),distance3d(boxes[ir],boxes[ic])])

dists = sorted(dists, key=lambda item: item[1])

circuits = []
i = 0
d = dists[i][0]
circuits.append([d[0], d[1]])
numConnections = 1
_ = dists.pop(0)
while (numConnections < 10):
	i += 1
	d = dists[i][0]	
	for c in circuits:
		if ((d[0] in c) and (d[1] in c)):
			newCircuitNeeded = False
			connectionMade = False
		elif (d[0] in c):
			c.append(d[1])
			newCircuitNeeded = False
			connectionMade = True
			numConnections += 1
		elif (d[1] in c):
			c.append(d[0])
			newCircuitNeeded = False
			connectionMade = True
			numConnections += 1

