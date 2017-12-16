# Day 1

moves = [m.strip('\n') for m in open("day16_input.txt")]
moves = moves[0]
moves = moves.split(',')

pa = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p']
pd = {}
for i in range(len(pa)):
	pd[pa[i]] = i

for m in moves:
	if (m[0]=='s'):
		n = int(m[1:])
		pa = pa[-n:] + pa[0:16-n]
		for i in range(len(pa)):
			pd[pa[i]] = i
	elif (m[0]=='x'):
		a,b = m[1:].split('/')
		a,b = int(a),int(b)
		tmp = pa[b]
		pa[b] = pa[a]
		pa[a] = tmp
		pd[pa[a]] = a
		pd[pa[b]] = b
	elif (m[0]=='p'):
		a,b = m[1:].split('/')
		a,b = int(pd[a]), int(pd[b])
		tmp = pa[b]
		pa[b] = pa[a]
		pa[a] = tmp
		pd[pa[a]] = a
		pd[pa[b]] = b

print('part 1: the programs are in order {}'.format(''.join(pa)))

# Day 2

moves = [m.strip('\n') for m in open("day16_input.txt")]
moves = moves[0]
moves = moves.split(',')

pa = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p']
pd = {}
for i in range(len(pa)):
	pd[pa[i]] = i

p1 = ''.join(pa)

# after some experimentation, found that sequence repeats every 60 reps
for irep in range(1000000000 % 60):
	for m in moves:
		if (m[0]=='s'):
			n = int(m[1:])
			pa = pa[-n:] + pa[0:16-n]
			for i in range(len(pa)):
				pd[pa[i]] = i
		elif (m[0]=='x'):
			a,b = m[1:].split('/')
			a,b = int(a),int(b)
			tmp = pa[b]
			pa[b] = pa[a]
			pa[a] = tmp
			pd[pa[a]] = a
			pd[pa[b]] = b
		elif (m[0]=='p'):
			a,b = m[1:].split('/')
			a,b = int(pd[a]), int(pd[b])
			tmp = pa[b]
			pa[b] = pa[a]
			pa[a] = tmp
			pd[pa[a]] = a
			pd[pa[b]] = b
	pirep = ''.join(pa)
	if (p1==pirep):
		print('same at rep {}'.format(irep))
		print(p1)
		print(pirep)


print('part 2: the programs are in order {}'.format(''.join(pa)))



