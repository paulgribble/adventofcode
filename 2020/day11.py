with open("day11_input.txt") as f:
	x = [r.strip('\n') for r in f]

S = []
for r in range(len(x)):
	S.append([c for c in x[r]])

def printS(S):
	print('')
	nr, nc = range(len(S)), range(len(S[0]))
	for r in nr:
		print(''.join(S[r]))
	print('')

def num_occ_adj(S,r,c):
	nr, nc = range(len(S)), range(len(S[0]))
	n = 0
	ii = ((0,-1),(0,+1),(1,0),(-1,0),(-1,-1),(+1,+1),(-1,+1),(+1,-1))
	for i in ii:
		ri, ci = r+i[0], c+i[1]
		if ((ri in nr) and (ci in nc)):
			if S[ri][ci] == '#':
				n += 1
	return n

def same(S1,S2):
	r = 0
	while r < len(S1):
		if S1[r] != S2[r]:
			return False
		r += 1
	return True

def num_occ(S):
	nr, nc = range(len(S)), range(len(S[0]))
	n = 0
	for r in nr:
		for c in nc:
			if S[r][c]=='#':
				n += 1
	return n

nr, nc = range(len(S)), range(len(S[0]))
done = False
rounds = 0
while not done:
	rounds += 1
	Sc = [s.copy() for s in S]
	for r in nr:
		for c in nc:
			if S[r][c]=='L' and num_occ_adj(S,r,c)==0:
				Sc[r][c]='#'
			elif S[r][c]=='#' and num_occ_adj(S,r,c)>=4:
				Sc[r][c]='L'
	done = same(S,Sc)
	S,Sc = Sc,S

print("Part 1: {}".format(num_occ(S)))

########

def num_occ_dir(S,r,c,dir):
	nr, nc = range(len(S)), range(len(S[0]))
	n = 0
	stop = False
	r, c = r+dir[0], c+dir[1]
	while (r in nr) and (c in nc) and not stop:
		if S[r][c]=='L':
			stop = True
		elif S[r][c]=='#':
			n += 1
			stop = True
		r, c = r+dir[0], c+dir[1]
	return n

def num_occ_see(S,r,c):
	nr, nc = range(len(S)), range(len(S[0]))
	n = 0
	dirs = ((0,-1),(0,+1),(1,0),(-1,0),(-1,-1),(+1,+1),(-1,+1),(+1,-1))
	for dir in dirs:
		n += num_occ_dir(S,r,c,dir)
	return n


S = []
for r in range(len(x)):
	S.append([c for c in x[r]])

nr, nc = range(len(S)), range(len(S[0]))
done = False
rounds = 0
while not done:
	rounds += 1
	Sc = [s.copy() for s in S]
	for r in nr:
		for c in nc:
			if S[r][c]=='L' and num_occ_see(S,r,c)==0:
				Sc[r][c]='#'
			elif S[r][c]=='#' and num_occ_see(S,r,c)>=5:
				Sc[r][c]='L'
	done = same(S,Sc)
	S,Sc = Sc,S

print("Part 2: {}".format(num_occ(S)))

