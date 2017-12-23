
# Part 1

lines = [l.strip('\n') for l in open('day23_input.txt')]

R = {}
for i in range(8):
	R[chr(ord('a')+i)] = 0

def Rint(c):
	if ((ord(c[0])<=ord('z')) & (ord(c[0])>=ord('a'))):
		return R[c]
	else:
		return int(c)

i = 0
stop = False
count = 0
ll = len(lines)
while (stop==False):
	l = lines[i].split()
#	print(l)
	if (l[0]=='set'):
		R[l[1]] = Rint(l[2])
	elif (l[0]=='sub'):
		R[l[1]] -= Rint(l[2])
	elif (l[0]=='mul'):
		R[l[1]] *= Rint(l[2])
		count += 1
	if (l[0]=='jnz'):
		if ((Rint(l[1])==0)==False):
			i += Rint(l[2])
		else:
			i += 1
	else:
		i += 1
	if ((i<0) | (i>=ll)):
		stop = True

print('part 1: mul is invoked {} times'.format(count))


# Part 2

R = {}
for i in range(8):
	R[chr(ord('a')+i)] = 0

R['a'] = 1

i = 0
stop = False
count = 0
ll = len(lines)
ii = 0
while (stop==False):
	ii += 1
	l = lines[i].split()
#	print(i)
	print(R)
#	print(l)
#	print(R['h'])
	if (l[0]=='set'):
		R[l[1]] = Rint(l[2])
	elif (l[0]=='sub'):
		R[l[1]] -= Rint(l[2])
	elif (l[0]=='mul'):
		R[l[1]] *= Rint(l[2])
		count += 1
	if (l[0]=='jnz'):
		if ((Rint(l[1])==0)==False):
			i += Rint(l[2])
		else:
			i += 1
	else:
		i += 1
	if ((i<0) | (i>=ll)):
		stop = True

print('part 2: the value left in register h is '.format(R['h']))


