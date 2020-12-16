with open("day16_input.txt") as f:
	inp = [r.strip('\n') for r in f]

rules = {}
ok = set()

i = 0
while inp[i] != '':
	loc,nums = inp[i].split(': ')
	numa,numb = nums.split(' or ')
	amin,amax = map(int,numa.split('-'))
	bmin,bmax = map(int,numb.split('-'))
	rules[loc] = set()
	for ii in range(amin,amax+1):
		ok.add(ii)
		rules[loc].add(ii)
	for ii in range(bmin,bmax+1):
		ok.add(ii)
		rules[loc].add(ii)
	i += 1

i += 2
ticket = list(map(int,inp[i].split(',')))

i += 3

nrules = len(rules.keys())
nearby = [] # pos1 values, pos2 values, etc
for _ in range(nrules):
	nearby.append(set())

p1 = 0
while i < len(inp):
	nn = set(map(int,inp[i].split(',')))
	if not nn.issubset(ok):
		p1 += sum(nn.difference(ok))
	else:
		tmp = list(map(int,inp[i].split(',')))
		for ii in range(len(tmp)):
			nearby[ii].add(tmp[ii])
	i += 1

print("Part 1: {}".format(p1))


FP = []
for p in range(nrules):
	FP.append(set())
	for r in rules.keys():
		if nearby[p].issubset(rules[r]):
			FP[p].add(r)

n = len(FP)
while sum(map(len,FP)) > len(FP):
	for i in range(n):
		if len(FP[i])==1:
			for j in range(n):
				tmp = list(FP[i])[0]
				if i!=j and tmp in FP[j]:
					FP[j].remove(tmp)

x = 1
for i in range(n):
	if list(FP[i])[0][0:9]=='departure':
		x = x * ticket[i]

print("Part 2: {}".format(x))

