

def knothash(string_in):
	listlen = 256
	Llist = list(range(listlen))
	Bytes = []
	for c in string_in:
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
		tmp = hex(h)[2:]
		if (len(tmp) < 2):
			tmp = '0' + tmp
		H2 = H2 + tmp
	return H2


# Part 1

p = 'uugsqrei'
#p = 'flqrgnkx'

G = [[0]*128]*128
for i in range(128):
	pp = p + '-' + str(i)
	b = ''
	h = knothash(pp)
	for hc in h:
		b = b + bin(int(hc,16))[2:].zfill(4)
	G[i] = [int(bi) for bi in b]

used = 0
for i in range(128):
	for j in range(128):
		used += G[i][j]

print('part 1: {} squares are used'.format(used))


# Part 2

from scipy.ndimage.measurements import label

items, numitems = label(G)

print('part 2: there are {} regions'.format(numitems))



