
with open("input") as f:
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


# with help from reddit

from collections import defaultdict

manifold = open("input").read().strip().splitlines()
beams = defaultdict(int)
beams[manifold[0].index('S')] = 1
p1 = 0
for row in manifold[1:]:
    new_beams = defaultdict(int)
    for x, c in beams.items():
        if row[x] == '^':
            new_beams[x - 1] += c
            new_beams[x + 1] += c
            p1 += 1
        else:
            new_beams[x] += c
    beams = new_beams

print(f"Part 1: {p1}")
print(f"Part 2: {sum(beams.values())}")


