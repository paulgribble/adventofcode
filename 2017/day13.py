

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

scanners = [0] * nlayers
severity = 0
rev = [False] * nlayers
print(layers)
for i in range(len(layers)):
#	print('{}: {}'.format(i,scanners))
	if (layers[i] > 0):
		if (scanners[i]==0):
			severity += (i * layers[i])
	for isc in range(nlayers):
		if (layers[isc]>0):
			if (rev[isc]==True):
				scanners[isc] = scanners[isc] - 1
			else:
				scanners[isc] = scanners[isc] + 1
			if ((scanners[isc]==(layers[isc]-1)) | (scanners[isc]==0)):
				rev[isc] = not rev[isc]

print('part 1: the severity of whole trip is {}'.format(severity))


# Part 2





