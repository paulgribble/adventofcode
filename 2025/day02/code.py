
with open("input") as f:
	IDs = f.readline().strip().split(',')

thesum = 0
for idi in IDs:
	i1,i2 = idi.split('-')
	i1,i2 = int(i1), int(i2)
	for i in range(i1,i2+1):
		ii = str(i)
		l = len(ii)
		if ((l%2)==0):
			if (ii[:(l//2)] == ii[(l//2):]):
				thesum += i


