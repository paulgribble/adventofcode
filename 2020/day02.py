with open("day02_input.txt") as f:
	lines= [line for line in f]

n = len(lines)
valid1 = 0
valid2 = 0
for i in range(n):
	a,b,c = lines[i].strip('\n').split(' ')
	lo,hi = map(int,a.split('-'))
	ch = b[0]
	pw = c
	if pw.count(ch)>=lo and pw.count(ch)<=hi:
		valid1 += 1
	if (pw[lo-1]==ch) ^ (pw[hi-1]==ch): # XOR
		valid2 += 1

print("Part 1: {}".format(valid1))
print("Part 2: {}".format(valid2))

# OR: to avoid having to load the whole thing in memory at once
#     Instead proceess the file line by line:

valid1 = 0
valid2 = 0
with open("day02_input.txt") as f:
	for line in f:
		a,b,c = line.strip('\n').split(' ')
		lo,hi = map(int,a.split('-'))
		ch = b[0]
		pw = c
		if pw.count(ch)>=lo and pw.count(ch)<=hi:
			valid1 += 1
		if (pw[lo-1]==ch) ^ (pw[hi-1]==ch): # XOR
			valid2 += 1

print("Part 1: {}".format(valid1))
print("Part 2: {}".format(valid2))



