

lines = [line.strip('\n') for line in open("day13_input.txt")]

nlayers = int(lines[-1:][0].split(':')[0]) + 1
layers = [0] * nlayers
for l in lines:
	a,b = l.split(': ')
	a,b = int(a), int(b)
	layers[a] = b

#layers = [3,2,0,0,4,0,4]
#nlayers = 7

# Part 1

def state_advance(scanners,layers,rev):
	for isc in range(nlayers):
		if (layers[isc]>0):
			if (rev[isc]==True):
				scanners[isc] = scanners[isc] - 1
			else:
				scanners[isc] = scanners[isc] + 1
			if ((scanners[isc]==(layers[isc]-1)) | (scanners[isc]==0)):
				rev[isc] = not rev[isc]

scanners = [0] * nlayers
severity = 0
rev = [False] * nlayers
print(layers)
for i in range(len(layers)):
#	print('{}: {}'.format(i,scanners))
	if (layers[i] > 0):
		if (scanners[i]==0):
			severity += (i * layers[i])
	state_advance(scanners,layers,rev)

print('part 1: the severity of whole trip is {}'.format(severity))


# Parts 1 & 2
# ran out of time, adapted an idea found on reddit forum
# insight: we are caught when (layer % (2*depth-2)) == 0

lines = [line.strip('\n') for line in open("day13_input.txt")]

# part 1

firewall = {}
for li in lines:
    layer,depth = li.split(": ")
    layer,depth = int(layer), int(depth)
    firewall[layer] = depth

severity = 0
for layer in firewall.keys():
    depth = firewall[layer]
    if layer % (2*depth-2) == 0:
       severity += layer*depth

print('part 1: the severity of whole trip is {}'.format(severity))

# part 2

delay = 0
ok = False
while (ok == False):
    ok = True
    for layer in firewall.keys():
        depth = firewall[layer]
        if (layer+delay)%(2*depth-2) == 0:
           ok = False
           delay += 1
           break

print('part 2: the fewest number of picoseconds delay to not get caught is {}'.format(delay))





