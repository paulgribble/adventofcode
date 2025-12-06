with open("input") as f:
	datafile = [line.strip().split(' ') for line in f]

for i in range(len(datafile)):
	datafile[i] = [item for item in datafile[i] if item != ""]

datafileT = [list(row) for row in zip(*datafile)]

total = 0
for line in datafileT:
	op = line[-1]
	tot = int(line[0])
	for e in line[1:-1]:
#		print(f"{tot} = {tot} {op} {e}")
		if (op=='*'):
			tot = tot * int(e)
		elif (op=='+'):
			tot = tot + int(e)
#	print(tot)
	total = total + tot

print(f"part 1: {total}")


with open("input2") as f:
	datafile = [list(line.rstrip('\n')) for line in f]

datafileT = [list(row) for row in zip(*datafile)]

rows = len(datafile)
cols = len(datafileT)

op_ind = [i for i,val in enumerate(datafile[-1]) if val in ('*','+')]
n_ops = len(op_ind)

total = 0
for i in range(n_ops):
	i1 = op_ind[i]
	i2 = cols if i==n_ops-1 else op_ind[i+1]-1
	print(datafileT[i1:i2])


