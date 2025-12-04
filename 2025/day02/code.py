
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
print(f"day1: {thesum}")


def isInvalid(i):
	ii = str(i)
	l = len(ii)
	segmax = l//2
	for j in range(1,segmax+1):
		if ((l%j)==0):
			pool = set()
			k=0
			while (((k+1)*j)<=l):
				i1,i2 = k*j, (k+1)*j
#				print(f"{i1},{i2}")
				pool.add(ii[i1:i2])
				k += 1
#			print(pool)
			if len(pool)==1:
				return True
	return False


thesum = 0
for idi in IDs:
	i1,i2 = idi.split('-')
	i1,i2 = int(i1), int(i2)
	for i in range(i1,i2+1):
		if isInvalid(i):
#			print(f"invalid: {i}")
			thesum += i

print(f"day2: {thesum}")


