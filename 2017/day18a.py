
# Part 1

lines = [l.strip('\n') for l in open('day18_input.txt')]

R = {}
Rf = {}
for i in range(26):
	R[chr(ord('a')+i)] = 0
	Rf[chr(ord('a')+i)] = 0

def Rint(c):
	if ((ord(c[0])<=ord('z')) & (ord(c[0])>=ord('a'))):
		return R[c]
	else:
		return int(c)

i = 0
stop = False
lastfreq = 0
ll = len(lines)
while (stop==False):
	l = lines[i].split()
	if (l[0]=='set'):
		R[l[1]] = Rint(l[2])
	elif (l[0]=='add'):
		R[l[1]] += Rint(l[2])
	elif (l[0]=='mul'):
		R[l[1]] *= Rint(l[2])
	elif (l[0]=='snd'):
		Rf[l[1]] = Rint(l[1])
		lastfreq = Rint(l[1])
	elif (l[0]=='mod'):
		R[l[1]] = R[l[1]] % Rint(l[2])
	elif (l[0]=='rcv'):
		print('freq of last sound played is {}'.format(lastfreq))
	if (l[0]=='jgz'):
		if (Rint(l[1])>0):
			i += Rint(l[2])
		else:
			i += 1
	else:
		i += 1
	if ((i<0) | (i>=ll)):
		stop = True






