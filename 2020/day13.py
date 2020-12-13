with open("day13_input.txt") as f:
	N = [l.strip('\n') for l in f]

time = int(N[0])
buses = N[1].split(',')

dmin = 9999999999999999
bid = 0
for b in buses:
	if b!='x':
		bb = (time//int(b))*int(b) + int(b)
		if bb < dmin:
			dmin = bb
			bid = int(b)

print("Part 1: {}".format((dmin-time)*bid))


# B = {}
# for i in range(len(buses)):
# 	if buses[i]!='x':
# 		B[int(buses[i])] = i

# bk = list(B.keys())
# bk.reverse()
# bv = list(B.values())
# bv.reverse()

# t = 100000000000000

# found = False
# while not found:
# 	ok = True
# 	i = 0
# 	while ok and i<len(bk):
# 		b  = bk[i]
# 		ib = (B[b])
# 		tmp = (t//b)*b+b-t if ib>0 else (t//b)*b-t
# #		print("{}:{},{}".format(t,tmp,ib))
# 		ok = tmp == ib
# 		if ok:
# 			i += 1
# 	found = ok
# 	if not found:
# 		t += bv[0]
# 		print("{}".format(t), end='\r')

# print("Part 2: {}".format(t))


# from Reddit, using Chinese Remainder Theorem
# https://brilliant.org/wiki/chinese-remainder-theorem/
# https://github.com/justinhsg/AoC2020/blob/master/13/solution.py

with open("day13_input.txt") as infile:
    lines = infile.read().split("\n")

depart = int(lines[0])

ids = []
delays  = []
for i, nums in enumerate(lines[1].split(",")):
    if(nums != 'x'):
        ids.append(int(nums))
        delays.append(i)

best = 1e100
for id in ids:
    delay = (-depart%id)
    if(delay < best):
        best = delay
        part1 = delay*id

t = [0 for _ in range(len(ids))]
prod = [id for id in ids]
for i in range(1, len(ids)):
    prod[i] *= prod[i-1]
    
for i in range(len(ids)-1):
    inv_prod = prod[i]**(ids[i+1]-2) % ids[i+1]
    f = ( (-t[i]-delays[i+1]) * inv_prod ) % ids[i+1]
    t[i+1] = t[i] + f*prod[i]
    
    
part2= t[-1]

print(part1)
print(part2)
