
with open("input2") as f:
	TM = [line.strip() for line in f]

l = len(TM)-1
beam0 = TM[0].index('S')
beams = set()
beams.add(beam0)

num_split = 0
for i in range(1,l):
	indices = [ix for ix, x in enumerate(TM[i]) if x == '^']
	for j in indices:
		if (j in beams):
			num_split += 1
			beams.remove(j)
			beams.add(j-1)
			beams.add(j+1)

print(f"part 1: {num_split}")


l = len(TM)-1
beam0 = TM[0].index('S')
beam = beam0
timelines = [[beam0]]

for i in range(1,l):
	indices = [ix for ix, x in enumerate(TM[i]) if x == '^']
	for j in indices:
		for t in timelines:
			if (t[-1]==j):
				tt = t.copy()
				t.append(j-1)
				tt.append(j+1)
				timelines.append(tt)

num_timelines = len(timelines)
print(f"part 2: {num_timelines}")


