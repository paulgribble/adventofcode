with open("day14_input.txt") as f:
	N = [l.strip('\n') for l in f]

# mask = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X'
# k,v = '8', '11'
# v = "{:b}".format(int(v)).zfill(36)
# v2 = maskadd(mask,v)
# mem[k] = v2

mem = {}

def maskadd(mask,v):
	v2 = list(v)
	for i in range(len(v)):
		if mask[i] != 'X':
			v2[i] = mask[i]
	v3 = ''.join(v2)
	return v3

for l in N:
	if l[1]=='a': # mask
		mask = l[7:]
	elif l[1]=='e': # mem
		k = l.split(']')[0][4:]
		mem[k] = maskadd(mask,"{:b}".format(int(l.split('= ')[-1])).zfill(36))

thesum = 0
for v in mem.values():
	thesum += int("0b"+v,2)

print("Part 1: {}".format(thesum))



def maskadd2(mask,v):
	v2 = list(v)
	for i in range(len(v)):
		if mask[i] == 'X':
			v2[i] = mask[i]
		elif mask[i] == '1':
			v2[i] = mask[i]
	v3 = ''.join(v2)
	return v3

def addressexpand(a,alist):
	i = a.find('X')
	if i == -1:
		alist.append(a)
	else:
		a1 = list(a)
		a1[i] = '0'
		a1 = ''.join(a1)
		a2 = list(a)
		a2[i] = '1'
		a2 = ''.join(a2)
		addressexpand(a1,alist)
		addressexpand(a2,alist)

mem = {}

for l in N:
	if l[1]=='a': # mask
		mask = l[7:]
	elif l[1]=='e': # mem
		k = l.split(']')[0][4:]
		a = "{:b}".format(int(k)).zfill(36)
		m = maskadd2(mask,a)
		alist = []
		addressexpand(m, alist)
		for a in alist:
			mem[a] = int(l.split('= ')[-1])

thesum = 0
for v in mem.values():
	thesum += v

print("Part 2: {}".format(thesum))


