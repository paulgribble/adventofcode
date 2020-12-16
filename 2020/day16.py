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
nearby = [] # stores positions of fields
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


