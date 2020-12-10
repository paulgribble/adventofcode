with open("day10_input.txt") as f:
	A = [int(r.strip('\n')) for r in f]

A.sort()
A.append(A[-1]+3)
AA = []
AA.append(0)
ii = 0
for i in range(len(A)-1):
	if (A[i]-AA[ii]) in [1,2,3]:
		AA.append(A[i])
		ii += 1
AA.append(AA[-1]+3)

d1,d2,d3 = 0,0,0
for i in range(len(AA)-1):
	if (AA[i+1]-AA[i])==1:
		d1 += 1
	elif (AA[i+1]-AA[i]==2):
		d2 += 1
	elif (AA[i+1]-AA[i]==3):
		d3 += 1

print("Part 1: {}".format(d1*d3))


# memoization
W = {}

def ways(i,AA,W):
	if i in W.keys():
		return W[i]
	if i==AA[-1]:
		W[i] = 1
		return 1
	if i not in AA:
		W[i] = 0
		return 0
	if i+1 not in W.keys():
		W[i+1] = ways(i+1,AA,W)
	if i+2 not in W.keys():
		W[i+2] = ways(i+2,AA,W)
	if i+3 not in W.keys():
		W[i+3] = ways(i+3,AA,W)
	W[i] = W[i+1] + W[i+2] + W[i+3]
	return W[i]

print("Part 2: {}".format(ways(0,AA,W)))

