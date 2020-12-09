with open("day09_input.txt") as f:
	code = [int(r.strip('\n')) for r in f]

def test(code, i, prev):
	n1,n2 = i-prev,i-prev
	valid = False
	while (not valid) and (n1<i):
		n2 = i-prev
		while (not valid) and (n2<i):
#			print("{},{},{},{},{}".format(i,n1,n2,code[n1]+code[n2]==code[i],n1!=n2))
			if (code[n1]+code[n2]==code[i]) and (n1!=n2):
				valid = True
			else:
				n2 += 1
		if (not valid):
			n1 +=1
	return valid,i,n1,n2

i = 25
prev = 25
valid = True
while valid:
	valid,ii,n1,n2 = test(code, i, prev)
	if valid:
		i += 1

print("Part 1: {}".format(code[i]))

tgt = code[i]
n = len(code)
found = False
n1 = 0
nmin,nmax = 0,0
while (not found) and (n1<n):
	n2 = n1+1
	nsum = code[n1]
	while (not found) and (n2<n):
		nsum += code[n2]
#		print("{},{},{},{}".format(code[n1],code[n2],nsum,tgt))
		if (nsum==tgt):
			found = True
		else:
			n2 += 1
	if not found:
		n1 += 1

nmin,nmax = code[n1],code[n1]
for i in range(n2-n1+1):
#	print("{},{},{}".format(code[i+n1],nmin,nmax))
	nmin = code[i+n1] if code[i+n1]<nmin else nmin
	nmax = code[i+n1] if code[i+n1]>nmax else nmax

print("Part 2: {}".format(nmin+nmax))
