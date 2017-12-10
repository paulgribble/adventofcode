import csv

# Part 1

listlen = 256
Llist = list(range(listlen))
with open("day10_input.txt") as f:
	Llens = [list(map(int,rec)) for rec in csv.reader(f, delimiter=',')]
Llens = Llens[0]

#listlen = 5
#Llist = list(range(listlen))
#Llens = [3, 4, 1, 5]

curpos = 0
skipsize = 0
for l in Llens:
	sublist = [0] * l
	for ii in range(l):
		sublist[ii] = Llist[(curpos+ii) % listlen]
	sublist = list(reversed(sublist))
	for ii in range(l):
		Llist[(curpos+ii) % listlen] = sublist[ii]
	curpos = (curpos + l + skipsize) % listlen
	skipsize += 1

print("Part 1: the product of the first 2 values is {0}".format(Llist[0]*Llist[1]))


# Part 2

listlen = 256
Llist = list(range(listlen))

Llens = [l.strip('\n') for l in open("day10_input.txt")]
Llens = Llens[0]
Bytes = []

#Llens = ''
for c in Llens:
	Bytes.append(ord(c))
for a in [17, 31, 73, 47, 23]:
	Bytes.append(a)

curpos = 0
skipsize = 0

for i64 in range(64):
	for l in Bytes:
		sublist = [0] * l
		for ii in range(l):
			sublist[ii] = Llist[(curpos+ii) % listlen]
		sublist = list(reversed(sublist))
		for ii in range(l):
			Llist[(curpos+ii) % listlen] = sublist[ii]
		curpos = (curpos + l + skipsize) % listlen
		skipsize += 1

H = [0] * 16
for i in range(16):
	i1, i2 = i*16, ((i+1)*16)-1
	h = Llist[i1]
	for ii in range(15):
		h = h ^ Llist[i1+ii+1]
	H[i] = h

H2 = ''
for h in H:
	tmp = hex(h).strip('0x')
	if (len(tmp) < 2):
		tmp = '0' + tmp
	H2 = H2 + tmp

print("Part 2: the hash is {0}".format(H2))



