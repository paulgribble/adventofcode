

#progs = {}
#progs[0] = [2]
#progs[1] = [1]
#progs[2] = [0,3,4]
#progs[3] = [2,4]
#progs[4] = [2,3,6]
#progs[5] = [6]
#progs[6] = [4,5]

lines = [line.strip('\n') for line in open("day12_input.txt")]
progs = {}
for l in lines:
	pin, pout = l.split(' <-> ')
	pout = pout.split(', ')
	pin = int(pin)
	pout = list(map(int,pout))
	progs[pin] = pout

numzero = 1
pkeys = list(progs.keys()).copy()
pconnectors = list(progs.values()).copy()
connectors = pconnectors[0].copy()
for i in range(len(progs)):
	if (pkeys[i] in connectors):
		connectors += pconnectors[i]

connectors = list(set(connectors))


